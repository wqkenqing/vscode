#!python3
# -*- coding: UTF-8 -*-
from kafka import SimpleClient, KafkaConsumer
from kafka.common import OffsetRequestPayload, TopicPartition

import logging
import datetime
import schedule
import time


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
            # infoMap.items()
    return infoMap


def writeMapInfoIntoFile(infoMap, path):
    imap = {}
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
    with open(path,"w",encoding="utf8")as f:
        f.write("true")

if __name__ == '__main__':
    # topic_offset = get_topic_offset("tengxun2:9092", "test-topic1")
    #
    # group_offset = get_group_offset("tengxun2:9092", "consumer002", "test-topic1")
    # print("the topic_number is %d",topic_offset)
    # print("the group_number is %d",group_offset)

    # tps = getTopics("tengxun2:9092")
    # tpps = []
    # for tp in tps:
    #     offset = get_group_offset("tengxun2:9092", "consumer002", tp)
    #     tpps.append(offset)
    # print(tpps)
    brokers = "tengxun2:9092"
    group_id = "consumer002"

    path = "/Users/wqkenqing/Desktop/temp_key/demo1.txt"
    path1 = "/Users/wqkenqing/Desktop/temp_key/is_restartKafa"

    # 加载初始化文件
    imap = InitGroupOffsetInfo(path)
    # 获取topic 对应offset信息
    # 获取topics
    topics = getTopics(brokers)
    for topic in topics:
        if (topic == "__consumer_offsets"):
            continue
        offset = get_group_offset(brokers, group_id, topic)
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
                info = topic + " " + str(offset) +" "+ str(threshold)
                imap.__setitem__(topic, info)
                if (threshold == 4):
                    print("重启标识")
                    #重启标识
                    writeIsRestartTagIntoFile(path)
    # 文件写回
    writeMapInfoIntoFile(imap, path)
