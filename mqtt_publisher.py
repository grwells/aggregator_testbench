#!/usr/bin/python3 
import context
import datetime
import paho.mqtt.publish as publish

topic = "topic"
message = "message"
hostname = "192.168.50.10"

# QoS 0 is best effort, QoS 1 is "delivered at least once".

publish.single(topic=topic, payload=message, hostname=hostname, qos=1)
