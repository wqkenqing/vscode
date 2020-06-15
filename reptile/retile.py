#!/bin/python
# coding=utf-8

import requests
import ssl
path = "https://api.github.com/events"

r = requests.get(path,verify=False)

r.encoding="gbk"

print(r.json())
