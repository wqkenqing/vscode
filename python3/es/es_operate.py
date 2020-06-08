#!python3
# coding=utf-8
from elasticsearch import Elasticsearch
import json

class esOperate(object):
    def getEsConnect(self, host, port):
        hosts=[]
        hosts.append('{}:{}'.format(host,port))
        es = Elasticsearch(hosts)
        return es

    def ouput(self, content):
        print(json.loads(content))

    def search(self, es, index, body):
        response = es.search(
            index=index,
            body=body
        )
        return response

if __name__ == '__main__':
    operate=esOperate()
    es=operate.getEsConnect("jd_cloud","9200")

    # res=operate.search(es,'people',body=query)
    # print(json.dumps(res,indent=4))




