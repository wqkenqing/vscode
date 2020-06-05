#!python3
# coding=utf-8
from elasticsearch import Elasticsearch
import json
import redis
import logging


class esTest(object):
    logging.basicConfig(level="INFO")

    def es_connect(self):
        es = Elasticsearch(['jd_cloud:9200'])
        return es

    def getIndexStore(self, content):
        cons = content.split("\n")
        dict = {}
        for row in cons:
            rows = row.split(" ")
            if (len(rows) > 2):
                dict.__setitem__(rows[2], rows[len(rows) - 1])
                print("{} {}".format(rows[2], rows[len(rows) - 1]))
        return dict

    def ouput(self, content):
        print(json.loads(content, indent=4))

    ##send es info into redis
    def infoIntoRedis(self, info):
        pool = redis.ConnectionPool(host="jd_cloud", port="6380", password="test123", db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        for k, v in info.items():
            r.hset("es_info", str(k), str(v))

        logging.info("info store was stored in redis ! ")

    def showMethod(self, operate):
        print(json.dumps(dir(operate), indent=4))

    def search(self, es, index, body):
        response = es.search(
            index=index,
            body=body
        )
        return response


if __name__ == '__main__':
    test = esTest()
    # 获取es实例对象
    es = test.es_connect()
    # 输出es健康状态
    # test.ouput(es.cluster.health())
    ## 输出索引数
    # print(es.cat.indices())
    # dict = test.getIndexStore(es.cat.indices())
    # test.infoIntoRedis(dict)

    ## view the mehtod info !
    # print(json.dumps(es.info(), indent=4))

    ## elasticsearch query
    # print(json.dumps(es.cat.indices(),indent=4))
    # test.getIndexStore(es.cat.indices())

    index = 'tourist_minute_local_data'
    body = '''{"from": 0,"size": 2}'''
    response = test.search(es, index, body)
    for resp in response['hits']['hits']:
        for k, v in resp:
            logging.info("==========this is the resp result ==========")
            print("the key is {},the val is {}".format(k, v))
            logging.info("============================================")
