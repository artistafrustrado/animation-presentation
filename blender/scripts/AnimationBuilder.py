#!/usr/bin/python

import os, sys
import json

file = open("../../media.json","r")
json_str = file.read()
file.close()

#print(json_str)

images = json.loads(json_str)

print(images)
