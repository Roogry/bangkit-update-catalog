# Automate updating catalog information
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

## What we'll do :
1. Fetching supplier data
2. Working with supplier images
3. Uploading images to web server
4. Uploading the descriptions
5. Generate a PDF report and send it through email
6. Health check

### 1. Fetching Supplier Data
In this step we need to **download data** that supplier added into Google Drive.
The data contains large images with an associated description of the products 
in two files (**.TIF** for the image and **.txt** for the description). 
Run code below to do that. 

`sudo chmod +x ~/download_drive_file.sh`

`./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz`

`tar xf ~/supplier-data.tar.gz`

That code will creates a directory named supplier-data, that contains 
subdirectories named images and descriptions.

For the description .txt file will be formated with the first line contains 
the name of the fruit followed by the weight of the fruit and 
finally the description of the fruit.

### 2. Working with supplier images
In this section, you will write a Python script named ==changeImage.py== to 
process the supplier images. You will be using the PIL library to update 
all images within ==~/supplier-data/images== directory to the 
following specifications:
- **Size**: Change image resolution from **3000x2000** to **600x400** pixel
- **Format**: Change image format from **.TIFF** to **.JPEG**

### 4. Uploading the descriptions
To add fruit images and their descriptions from the supplier on the fruit 
catalog web-server, Python script will automatically POST the fruit images 
and their respective description in JSON format.

The json data should be looks like:
=={"name": "Test Fruit", "weight": 100, "description": "This is the 
description of my test fruit", "image_name": "icon.sheet.png"}==

Script named ==run.py== to process the text files (001.txt, 003.txt ...) 
from the ==supplier-data/descriptions== directory. The script should turn 
the data into a JSON dictionary by adding all the required fields, 
including the image associated with the fruit (image_name), and 
uploading it to ==http://[linux-instance-external-IP]/fruits== 
using the Python **requests** library.

