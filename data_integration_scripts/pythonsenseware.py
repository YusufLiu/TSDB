from __future__ import print_function
import boto3
import json
import uuid
import httplib, urllib2
import base64
import ssl
from decimal import *


def lambda_handler(event, context):
    # check if the event has content
    try:
        packet = json.loads(event['body'])
    except KeyError:
        packet = event

    site = packet['site'].replace(' ', '_')
    site = site.replace('(', '_')
    site = site.replace(')', '_')
    site = site.replace('[', '_')
    site = site.replace(']', '_')
    location = packet['location'].replace(' ', '_')
    location = location.replace('(', '_')
    location = location.replace(')', '_')
    location = location.replace('[', '_')
    location = location.replace(']', '_')
    unit = packet['unit'].replace(' ', '_')
    measurements = packet['name'].replace(' ', '_')
    measurements = measurements.replace('.', '_')
    measurements = measurements.replace('(', '_')
    measurements = measurements.replace(')', '_')
    measurements = measurements.replace('[', '_')
    measurements = measurements.replace(']', '_')
    url = 'https://52.206.6.10:8086/write?db=Senseware'
    data = ''
    # for each measurements in the event
    for record in packet['data']:
        time = record['ts']*1000000000
        value = record['value']
        tempdata = measurements + ',site='+site+',location='+location+',unit='+unit+' value='+str(value)+' '+str(time) + ' \n'
        req = urllib2.Request(url, tempdata, {'Content-Type': 'application/octet-stream'})
        base64string = base64.b64encode('%s:%s' % ('blocpower', 'I4yrvbtSiw'))
        req.add_header("Authorization", "Basic %s" % base64string)
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        f = urllib2.urlopen(req, context=gcontext)
        response = f.read()
        print (tempdata)
        f.close()
