#!python3
# coding=utf-8
from elasticsearch import Elasticsearch

import json


class esOperate(object):
    def getEsConnect(self, host, port):
        hosts = []
        hosts.append('{}:{}'.format(host, port))
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

    def operate(self, es, index, body):
        response = es.search
        return response


if __name__ == '__main__':
    operate = esOperate()
    es = operate.getEsConnect("jd_cloud", "9200")
    index = 'hy_gather_weather'
    body = '''{
"query": {
    "bool": {
      "must": [
        {"range": {
          "gatherTime": {
            "gte": "2020-02-15 10:42:00"
          }
        }}
      ]
    }
  }
}'''

    response = operate.search(es, index, body)
    print(json.dumps(response, indent=4))

