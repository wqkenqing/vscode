#!python3
# -*- coding: UTF-8 -*-j
from datetime import datetime

## datetime created
now=datetime.now()
print(now)

##指定时间创建

# dt = datetime(2015, 4, 19, 12, 20)

# print(dt.timestamp())

dt=datetime(2020,5,23,12,32)
print(dt)

# datetime转换为timestamp

print(datetime.fromtimestamp(1429417200.0))


#  datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

#

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))