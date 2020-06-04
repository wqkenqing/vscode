#!python3
# -*- coding: UTF-8 -*-
import logging

try:
    logging.info("starting....")
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    # print('except:', e)
    logging.exception(e)
finally:
    print('finally...')
print('END')