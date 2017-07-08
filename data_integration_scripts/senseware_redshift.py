from __future__ import print_function

import json
import urllib
import boto3
import datetime
import psycopg2
import linecache

print('Loading function')


def lambda_handler(event, context):
    try:
        packet = json.loads(event['body'])
    except KeyError:
        packet = event

    # establish connection to the db

    connection = psycopg2.connect(dbname="senseware", host="sensewarecluster.cz6saalxbzqr.us-east-1.redshift.amazonaws.com", port="5439", user="blocpower", password="6ZViU7JcbN")
    cursor = connection.cursor()

    site = packet['site']
    location = packet['location']
    unit = packet['unit']
    measurements = packet['name']
    firstdata = 0
    sqlcommand=""
    # for each measurements in the event
    for record in packet['data']:
        time = record['ts']
        time = datetime.datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
        value = record['value']
        # check if there is already a record that has the same data
        sqlcheck = "select * from living_hope where measurements_time = '"+ time+"' and type = '" + measurements + "' and location = '" + location + "'"
        cursor.execute(sqlcheck)
        data = cursor.fetchall()
        if not data:
            print ('no data')
            # if it is new data, add it into the sqlcommand for excute later
            if (firstdata == 0):
                sqlcommand = 'INSERT INTO living_hope Values '
                firstdata = 1
            sqlcommand = sqlcommand + "('" + time + "','" + measurements + "','" + site + "','" + location + "','" + unit + "','" + str(value) + "'),"
        else:
            print ('yes data')

        print(sqlcommand)

    if(firstdata == 1):
        sqlcommand = sqlcommand[:-1] + ';'
        print(sqlcommand)
        cursor.execute(sqlcommand)



