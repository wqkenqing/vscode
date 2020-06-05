#!python3
# coding=utf-8

import json
import logging
logging.basicConfig(level="INFO")

def objtojson(objects):
    jobj=json.dumps(objects)
    print(jobj.keys())
    logging.info("the json object is {}".format(jobj))

if __name__ == '__main__':
    dicts={"name":"joe","age":12}
    objtojson(str(dicts).replace("'", '"'))


