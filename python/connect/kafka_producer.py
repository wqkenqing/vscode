#!python3
# -*- coding: UTF-8 -*-
from kafka import KafkaProducer
# 创建生产者
producer = KafkaProducer(bootstrap_servers='jd_cloud:32770')
count=1
while(True):
    # 指定topic发送bytes类型的数据
    count=count+1
    countb=bytes(count)
    print('send info at %d times',count)
    producer.send('test_topic5',b'Hello kafka'+countb)
