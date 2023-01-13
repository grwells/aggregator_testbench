#!/usr/bin/python3 
import context  # Ensures paho is in PYTHONPATH
import datetime
import paho.mqtt.subscribe as subscribe

filename = './mqtt_log.csv'
# datetime.datetime.now()

def write_to_file(datetime, topic_str, message_str):
    file = open(filename, 'a')

    file.write(f"{datetime.datetime.now()}, {topic}, {message}\n")
    file.close()

def msg_receiver(client, userdata, message):
    ts = datetime.datetime.now()
    print("[", ts, "] %s : %s" % (message.topic, message.payload))
    write_to_file(ts, message.topic, message.payload)


subscribe.callback(msg_receiver, "#", hostname="192.168.50.10")
