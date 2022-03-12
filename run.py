#!/usr/bin/env python3
import os
import requests
import re

fruit_catalogs = []
image_path = 'supplier-data/images/'
desc_path = 'supplier-data/descriptions/' 

jpeg_images = sorted([image_file for image_file in os.listdir(image_path) if image_file.endswith(".jpeg")])
text_files = sorted(os.listdir(desc_path))

# Process each data file
for file in text_files:
    keys = ['name', 'weight', 'description']

    with open(desc_path + file, 'r') as opened:
        img_counter = 0
        fruit_data = {}

        for i, line in enumerate(opened, 1):
            if not line.strip():
                continue
            
            if i == len(keys):
                # skip if the length of file more than data that we need
                break
            elif i == 1:
                # add only the number value of fruit weight
                fruit_data[keys[i]] = int(re.search(r'\d+', "100 libs").group())
            else:
                fruit_data[keys[i]] = line
        
        fruit_data['image_name'] = jpeg_images[img_counter]
        img_counter += 1

        fruit_catalogs.append(fruit_data)

# Post catalog to webserver
for fruit_data in fruit_catalogs:
    r = requests.post('http://127.0.0.1:80/fruits/', json=fruit_data)