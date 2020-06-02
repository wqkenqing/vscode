#--*-- encoding:utf8 --*--
import logging

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    # print('except:', e)
    logging.exception(e)
finally:
    print('finally...')
print('END')