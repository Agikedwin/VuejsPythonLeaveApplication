#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import datetime
import logging

try:
	logging.basicConfig(filename='/opt/textit/logs/myapp.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
	logger=logging.getLogger(__name__)
	logger.info('TextIt Is Up and Running')


	headers = {'Authorization': 'Token de84bede91a07c5038708dc155c0079866dfad9d','content-type': 'application/json'}
	url = 'https://textit.in/api/v2/broadcasts.json'
	data = {"urns": ["tel:+254723452222"],"text": "TextIT Platform is up and running."}
	params = {'Authorization': 'Token de84bede91a07c5038708dc155c0079866dfad9d'}
	print requests.post(url, params=params, data=json.dumps(data), headers=headers)
	print json.dumps(data)

	# Write Something
	print 'Working Output'
except requests.Timeout as e:
	logger.error('Timeout :-%s' %str(e))
	# continue
except requests.RequestException as e:
	logger.error('RequestException :- %s' %str(e))
	# continue
except KeyboardInterrupt as e:
	logger.error('KeyboardInterrupt :- %s' %str(e))
	# continue