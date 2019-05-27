#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import requests
from time import sleep
con = mdb.connect('192.168.168.38', 'root', 'test12', 'openmrs');
with con: 
    cur = con.cursor()
    cur.execute("SELECT person_id,gender,'+254724416275' FROM person limit 1")
    rows = cur.fetchall()
    for row in rows:

        print row[2]
r =requests.post('https://textit.in/api/v2/broadcasts.json, array(Authorization = Token 49e9070bad723213e7ece63042da2449863a7096), array(urns=>array(tel:+254724416275),text=>SMS Here')

print r.json
time.sleep(5)
#print r.status_code
