#!/usr/bin/python

import os, sys
import json

path = "../../images"
dirs = os.listdir( path )

images = []

for file in dirs:
    #print(file)
    image = {
            "image" :       file,
            "subtitle" :    "Subtitle",
            "duation" :     72,
            "type" :        "image"
            }
    images.append(image)

#print(images)

json_str = json.dumps(images, indent=2)

file = open("../../media.json","w")
file.write(json_str)
file.close()

