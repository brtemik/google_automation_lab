#! /usr/bin/env python3

import os
import requests

'''
This script will upload images and descriptions of fruits that were provided.
The script reads .txt files that contain info about fruits, makes dictionaries with that
info and uploads it to Django endpoint.

###################
Description example:

Mango
300 lbs as integer
Description info...

###################
Dictionary example:

{"name": "Test Fruit",
 "weight": 100,
 "description": "This is the description of my test fruit",
 "image_name": "icon.sheet.png"}
'''

jsons = []
descriprions = os.listdir('/home/student-00-b0c51666e7f0/supplier-data/descriptions/')
for desc in descriprions:
    path = '/home/student-00-b0c51666e7f0/supplier-data/descriptions/' + desc
    json = {}
    with open(path, 'r') as file:
        content = file.readlines()
        json["name"] = content[0][:-1]
        json["weight"] = int(content[1].split(' ')[0])
        description = ''
        for line in content[2:]:
            description +=line
        json["description"] = description
        json["image_name"] = '/home/student-00-b0c51666e7f0/supplier-data/images/' + desc.split('.')[0] + '.jpeg'
    jsons.append(json)

for json in jsons:
    r = requests.post('http://localhost/fruits/', json=json)
    print(r.raise_for_status())
