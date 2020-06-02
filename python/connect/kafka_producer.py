#!python3
#--*-- encoding:utf8 --*--
from kafka import KafkaProducer
# 创建生产者
producer = KafkaProducer(bootstrap_servers='jd_cloud:32770')  
for _ in range(3):  
    # 指定topic发送bytes类型的数据
    producer.send('test_topic5',b'Hello kafka')