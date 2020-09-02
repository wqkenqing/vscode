#!python3
# -*- coding: UTF-8 -*-
import time

import kafka
from kafka import KafkaConsumer

consumer = KafkaConsumer('test-topic2', group_id='consumer001', auto_offset_reset='earliest'
                         , bootstrap_servers=['tengxun2:9092'])
print("star consumer ....")
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)
