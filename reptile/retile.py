#!python3
# coding=utf-8
import requests
import beautifulsoup4

path="https://wqkenqing.github.io/2020/05/25/%E6%97%A5%E5%B8%B8%E6%80%BB%E7%BB%93/%E7%BC%96%E7%A8%8B/python/"

req=requests.get(url=path)
print(req.text)
