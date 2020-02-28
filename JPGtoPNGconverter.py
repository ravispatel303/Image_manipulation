# command: python JPGtoPNGconverter.py Pokedex outputs

# Following code converts all images in folder from JPG to PNG

import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}/{filename}')
	clean_image = os.path.splitext(filename)[0]
	img.save(f'{output_folder}/{clean_image}.png','png')
	print('all done')
