'''
Convert Images from a Directory to png and saves them to new directory
Should be run through CommandLine

Command Line Query::::

  python jpgtopng.py ImageDirectoryName ConverterImageDirectoryName
  

'''
import sys
import os

from PIL import Image,ImageFilter


sys.argv

image_folder = 'Pokedex'
new_folder = 'PokedexNew'
li = []
li = os.listdir('./'+image_folder)

for i in li:
    if '.jpg' in i:
        img = Image.open(f'./{image_folder}/{i}')
        img.thumbnail((200,200))
        cleanpath = os.path.splitext(i)[0]
        if not os.path.exists(new_folder):
            try:
                os.makedirs(new_folder)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        img.save(f'./{new_folder}/{cleanpath}.png','png')

