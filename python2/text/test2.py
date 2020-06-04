#!python3
# -*- coding: UTF-8 -*-
##json test
import json
test_obj={   "name":"ken","age":12,"sex":"boy"}

str=json.dumps(test_obj,indent=4 )
print(str)
