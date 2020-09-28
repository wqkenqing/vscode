#!python3
# -*- coding: UTF-8 -*-
import configparser
import datetime
import os
import sys
import time
import logging
import schedule
from kafka import KafkaConsumer, TopicPartition
from kafka.client import SimpleClient
from kafka.structs import OffsetRequestPayload

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)


def initConfig(path):
    """
    加载配置文件
    :return:
    """
    cf = configparser.ConfigParser()
    # file = open(path).read().encode("utf-8")
    cf.read(path, encoding="utf-8-sig")
    initmap = {}
    for item in cf.items("kafka"):
        initmap.__setitem__(item[0], item[1])
    return initmap


def initConfigN(path):
    """
    加载配置文件
    :return:
    """
    initmap = {}
    with open(path, "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            rows = line.split(" ")
            initmap.__setitem__(rows[0], rows[1])
    return initmap


def get_topic_offset(brokers, topic):
    """
    获取一个topic的offset值的和
    """
    client = SimpleClient(brokers)
    partitions = client.topic_partitions[topic]
    offset_requests = [OffsetRequestPayload(topic, p, -1, 1) for p in partitions.keys()]
    offsets_responses = client.send_offset_request(offset_requests)
    return sum([r.offsets[0] for r in offsets_responses])


def get_group_offset(brokers, group_id, topic):
    """
    获取一个topic特定group已经消费的offset值的和
    """
    consumer = KafkaConsumer(bootstrap_servers=brokers,
                             group_id=group_id,
                             )
    pts = [TopicPartition(topic=topic, partition=i) for i in
           consumer.partitions_for_topic(topic)]
    result = consumer._coordinator.fetch_committed_offsets(pts)
    return sum([r.offset for r in result.values()])


def getTopics(brokers):
    """
    获取topics
    :param brokers:
    :return:
    """
    client = SimpleClient(brokers)
    tps = client.topics
    return tps


def InitGroupOffsetInfo(path):
    """
    初始化kafka offset信息
    :param path:
    :return:
    """
    infoMap = {}
    with open(path, "r", encoding="utf8") as f:
        infolines = f.readlines()
        for info in infolines:
            info = info.replace("\n", "")
            infos = info.split(" ")
            infoMap.__setitem__(infos[0], info.replace("11", "12"))
    logging.info("初始化信息加载完成....")
    return infoMap


def writeMapInfoIntoFile(infoMap, path):
    imap = infoMap
    """
    将最新的initInfoMap 写入file中
    :return: 
    """
    with open(path, "w", encoding="utf8") as f:
        for item in imap.items():
            f.write(item[1])
            f.write("\n")

    logging.info("map has wrote into  files")


def writeIsRestartTagIntoFile(path):
    with open(path, "w", encoding="utf8")as f:
        f.write("true")


def monitor(path):
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    logging.info('monitor time is : %s', ts)
    initmap = initConfig(path)
    # 加载初始化文件
    imap = InitGroupOffsetInfo(initmap.get("offset_record"))
    # 获取topic 对应offset信息
    # 获取topics
    topics = getTopics(initmap.get("brokers"))
    for topic in topics:
        if (topic == "__consumer_offsets"):
            continue
        offset = get_group_offset(initmap.get("brokers"), initmap.get("group_id"), topic)
        if not imap.get(topic):
            info = topic + " " + str(offset) + " " + "0"
            imap.__setitem__(topic, info)
        else:
            info = imap.get(topic)
            infos = info.split(" ")
            old_offset = infos[1]
            threshold = infos[2]
            if (int(old_offset) == int(offset)):
                threshold = int(threshold) + 1
                info = topic + " " + str(offset) + " " + str(threshold)
                imap.__setitem__(topic, info)
                if (threshold >= int(initmap.get("threshold"))):
                    logging.info("kafka is going to restart!")
                    os.system(initmap.get("command1"))
                    # os.system(initmap.get("command2"))
                    ts = now.strftime('%Y-%m-%d %H:%M:%S')
                    logging.info("the time of restart is %s", ts)
                    # 重置心跳文件
                    imap = {}
                    writeMapInfoIntoFile(imap, initmap.get("offset_record"))
                    # 重启Kafka需要时间
                    time.sleep(120)
                    ts = now.strftime('%Y-%m-%d %H:%M:%S')
                    logging.info("kafka restart is completed! %s", ts)
    # 文件写回
    writeMapInfoIntoFile(imap, initmap.get("offset_record"))


if __name__ == '__main__':
    path = "/Users/kuiqwang/Desktop/temp_key/kafka.conf"
    ##参数conf地址

    print("kafka monitor job is running!")
    # if len(sys.argv) != 2:
    #     logging.error("运行参数有误..")
    #     exit(1)
    # path = sys.argv[1]
    schedule.every(30).seconds.do(monitor, path)
    while (True):
        schedule.run_pending()
        time.sleep(2)
    # print(initConfig(path))
