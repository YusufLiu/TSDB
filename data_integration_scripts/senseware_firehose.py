'use strict';
from __future__ import print_function
import httplib, urllib2
import json
import uuid
import base64
import ssl
import boto3

console.log('Loading function');

print('Loading function')

def lambda_handler(event, context):
    output = []
    try:
        packet = json.loads(event['body'])
    except KeyError:
        packet = event

    site = packet['site'].replace(' ','_')
    location = packet['location'].replace(' ','_')
    unit = packet['unit'].replace(' ','_')
    measurements = packet['name'].replace(' ','_')
    measurements = packet['name'].replace('.','_')
    data = ''
    #for each measurements in the event
    for record in packet['data']:
        time = record['ts'] * 1000000000
        value = record['value']
        data += tempdata
        # insert into the database

    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data'])

        # Do custom processing on the payload here

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload)
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
