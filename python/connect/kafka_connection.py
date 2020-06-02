#!python3
#--*-- encoding:utf8 --*--
# import kafka
from kafka import KafkaConsumer
consumer=KafkaConsumer('test_topic5',group_id='consumer001',auto_offset_reset='earliest'
,bootstrap_servers=['jd_cloud:32770'])
print("start")
for msg in consumer:  
     recv = "%s:%d:%d: key=%s value=%s" %(msg.topic,msg.partition,msg.offset,msg.key,msg.value)  
     print(recv)  