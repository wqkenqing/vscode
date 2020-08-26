#!python3
# coding=utf-8
import csv

# path = "/Users/wqkenqing/Desktop/文档/公司文稿/yanggu/hy_traffic_city_tour_bus.csv"
path = "/Users/wqkenqing/Desktop/out/tmp.csv"
import logging

logging.basicConfig(level="INFO")


def csv_operate(path):
    with open(path, encoding="utf8")as cf:
        reader = csv.reader(cf)
        for row in reader:
            print(row[0])
            if (row[0] == 'id'):
                print("ok")
                continue
            if (int(row[0]) % 2 == 0):
                print("the number is {}".format(row[0]))


def csv_output(path, row):
    csv_files = open(path, 'w', newline='')
    writer = csv.writer(csv_files)
    for a in row:
        writer.writerow(a)


def csv_transform(from_path, topath):
    csv_reader = open(from_path, "r", encoding="utf8")
    from_reader = csv.reader(csv_reader)
    csv_writer = open(topath, "w", encoding="utf8")
    to_writer = csv.writer(csv_writer)

    for row in from_reader:
        to_writer.writerow(row)

    logging.info("all files have sent!")

def csv_getHeader(frompath):
    csv_reader=open(from_path,"r",encoding="utf8")
    reader=csv.reader(csv_reader)
    for row in reader :
        print(row)



if __name__ == '__main__':
    # csv_operate(path)
    # row=[['name','age']]
    # csv_output(path,row)
    from_path = "/Users/wqkenqing/Desktop/文档/公司文稿/yanggu/hy_travel_related_enterprises_view.csv"
    # to_path = "/Users/wqkenqing/Desktop/临时文件/out.csv"
    # csv_transform(from_path, to_path)
    csv_getHeader(from_path)