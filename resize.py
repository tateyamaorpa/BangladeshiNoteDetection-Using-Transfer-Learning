
from PIL import Image
import os, sys

path = "../data/note_dataset/twohundred/"
dirs = os.listdir( path )
print(dirs)
def resize():
    print("working")
    for item in dirs:

        if os.path.isfile(path+item):
            print('hello')
            im = Image.open(path+item)
            print(os.listdir(path))
            f, e = os.path.splitext(path+item)
            imResize = im.resize((256,117), Image.ANTIALIAS)
            imResize.save(f+ ' resized.png', 'PNG', quality=90)

resize()


