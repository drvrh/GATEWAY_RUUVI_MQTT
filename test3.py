# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt #import the client1
import time
import os
from datetime import datetime

from ruuvitag_sensor.ruuvitag import RuuviTag

mac = 'FC:CC:85:B4:C5:E5'
broker_address="192.168.88.233"

print('Starting')

client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker

sensor = RuuviTag(mac)

while True:
    data = sensor.update()

    line_sen = str.format('Sensor - {0}', mac)
    line_tem = str.format('Temperature: {0} C', data['temperature'])
    line_hum = str.format('Humidity:    {0}', data['humidity'])
    line_pre = str.format('Pressure:    {0}', data['pressure'])

    # Clear screen and print sensor data
    os.system('clear')
    print('Press Ctrl+C to quit.\n\r\n\r')
    print(str(datetime.now()))
    print(line_sen)
    print(line_tem)
    print(line_hum)
    print(line_pre)
    print('\n\r\n\r.......')
    client.publish("RUUVI/temperature",line_tem) #publish
#    client.publish("RUUVI/humidity",line_hum) #publish

    # Wait for 2 seconds and start over again
    try:
        time.sleep(2)
    except KeyboardInterrupt:
        # When Ctrl+C is pressed execution of the while loop is stopped
        print('Exit')
        break

