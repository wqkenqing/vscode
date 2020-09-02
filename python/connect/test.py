#!python3
# -*- coding: UTF-8 -*-
import kafka
# from kafka import SimpleClient
from kafka import KafkaAdminClient


def deleteAll():
    # client = SimpleClient("tengxun2:9092")
    admin=KafkaAdminClient(bootstrap_servers="tengxun2:9092", client_id='test')
    admin._convert_new_topic_request("test-topic2")
    for tp in admin.list_topics():
        print(tp)
        

if __name__ == '__main__':
    deleteAll()


