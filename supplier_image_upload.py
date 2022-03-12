#!/usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"

image_path = 'supplier-data/images/'
jpeg_images = [image_file for image_file in os.listdir(image_path) if image_file.endswith(".jpeg")]

for image in jpeg_images:
    with open(image_path + image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})