#!/usr/bin/env python3
import os
from PIL import Image

image_path = 'supplier-data/images/'

for image_file in os.listdir(image_path):
    if image_file.endswith(".tiff"):
        img = Image.open(image_path + image_file).convert("RGB")
        filename = os.path.splitext(image_file)[0]

        img.resize((600, 400)).save(image_path + filename + '.jpeg' , 'jpeg')