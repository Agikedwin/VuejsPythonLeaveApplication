#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import requests
import json
import datetime
import logging

# Setup Logging
# filename= 'C:\\Users\\Danet\\Desktop\\PROJECTS\\TextIT\\textit-reminder-script\\textit_reminder.log'
filename = '/opt/textit/logs/textit_reminder.log'
# Log Info
logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)
try:
	mylist = []
	myday  = []
	today1  = datetime.date.today()
	today  = datetime.date.today()+ datetime.timedelta(days=1)
	mylist.append(today)
	myday.append(today1)

	con = mdb.connect('192.168.168.38', 'root', 'test12', 'openmrs');
	logger.info('TextIt Connected To Database Successfully')

	sql="select " + \
	"e.patient_id," + \
	"pi.identifier as FACES_ID," + \
	"pn.given_name as Patient_Name," + \
	"MAX(IF(o.concept_id IN(5096,1938,7469),DATE(o.value_datetime),NULL)) AS TCA," + \
	"concat_ws('','+254',min(IF(o.concept_id IN(6497),'+'+ o.value_text,NULL))) AS Phone_Number, " + \
	"l.name as Site, " + \
	"e.location_id  " + \
	"FROM encounter e " + \
	"JOIN patient_identifier `pi` ON pi.patient_id=e.patient_id AND pi.identifier_type IN(3) AND pi.voided=0 " + \
	"JOIN location l ON l.location_id = e.location_id " + \
	"JOIN person p on p.person_id=e.patient_id " + \
	"JOIN person_name pn on pn.person_id=e.patient_id " + \
	"LEFT OUTER JOIN obs o ON o.encounter_id = e.encounter_id AND o.voided = 0 AND o.concept_id IN (5096,1938,7469,6497) " + \
	"where  e.location_id in (2) " + \
	"group by e.patient_id " + \
	"having TCA ='"+ str(mylist[0]) +"'" 	

	logger.info('TextIt Is Running Query: %s' %sql)
	cur  = con.cursor()
	curr = con.cursor()
	cur.execute(sql)

	numrows = cur.rowcount
	logger.info('TextIt Fetched %s Patients' %numrows)

	if numrows > 0:
		logger.info('TextIt Is Processing Messages')
		for x in range(0, numrows):
			row = cur.fetchone()

			tel = str(row[4])
			msg = 'Hujambo '+row[2]+', kumbuka kuwa siku yako ya cliniki ni kesho '+ str(row[3])+', hakikisha usichelewe. Twajali maslahi yako. Ukiwa na swali lolote tupigie simu kwa nambari 0704381445 '+ str(row[5]) +'.'
			
			headers = {'Authorization': 'Token de84bede91a07c5038708dc155c0079866dfad9d','content-type': 'application/json'}
			url = 'https://textit.in/api/v2/broadcasts.json'
			data = {"urns": ["tel:"+ tel +""],"text": ""+msg+""}
			params = {'Authorization': 'Token de84bede91a07c5038708dc155c0079866dfad9d'}

			if str(row[4]) =="+254":
				code = '400'
				comm='''Not Sent - Missing Phone Number'''
			else:
				code = '201'
				comm='''Sent'''

			sql1 = "insert into textit_notifigation_log (patient_id,identifier,TCA,Phone_Number,Site,respones_code,comment,location_id,reminder_date,facility_number,msg) value('%s', '%s', '%s','%s', '%s', '%s','%s','%s','%s','%s','%s')"  % \
			 ( str(row[0]), str(row[1]) , str(row[3]), str(row[4]) , str(row[5]) ,str(code),str(comm),str(row[6]),str(myday[0]),str('0704381445'),str(msg))
			curr.execute(sql1)
			con.commit()
			print requests.post(url, params=params, data=json.dumps(data), headers=headers)
			print json.dumps(data)
		# Close the connection
		con.close()
		headers = {'Authorization': 'Token de84bede91a07c5038708dc155c0079866dfad9d','content-type': 'application/json'}
		url = 'https://textit.in/api/v2/broadcasts.json'
		data = {"urns": ["tel:+254716098339", "tel:+254732994592", "tel:+254724416275", "tel:+254722179264", "tel:+254721744059", "tel:+254707621658",],"text": "TextIT SMS reminders sent successfully, Login to OpenMRS and run TCA Reminders via TextIt Report"}
		logger.info('TextIt Processed %s Messages Successfully' %numrows)	
		params = {'Authorization': 'Token de84bede91a07c5038708dc155c0079866dfad9d'}
		print requests.post(url, params=params, data=json.dumps(data), headers=headers)
		print json.dumps(data)
	else:
		logger.info('TextIt Unable To Send Messages.Zero Patients With TCA %s' %today)
except Exception as err:
	logger.error(err)



