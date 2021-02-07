#!/usr/bin/env python3
from PIL import Image
import sys
import os
import requests

'''
This script changing pictures' format from .tiff to .jpeg
and resizes them from 3000x2000 to 600x400. Then saves modified
files near originals in the same directory. Also uploads jpegs
connecting to Django endpoint via requests lib.
'''

images = os.listdir('/home/student-00-b0c51666e7f0/supplier-data/images/')
for image in images:
    path = '/home/student-00-b0c51666e7f0/supplier-data/images/' + image
    im = Image.open(path)
    new_path = '/home/student-00-b0c51666e7f0/supplier-data/images/' + image.split('.')[0] + '.jpeg'
    new_im = im.resize((600,400)).convert('RGB').save(new_path)

images = os.listdir('/home/student-00-b0c51666e7f0/supplier-data/images/')
for image in images:
    if '.jpeg' in image:
        path = '/home/student-00-b0c51666e7f0/supplier-data/images/' + image
        with open(path, 'rb') as file:
            r = requests.post('http://localhost/upload/', files = {'file': file})
        print(r.raise_for_status())

