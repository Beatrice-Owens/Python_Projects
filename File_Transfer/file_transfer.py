

import shutil
import os

#source of the files
source = '/Users/point/Desktop/FolderA/'


#destination of the files
destination = '/Users/point/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    #moving files represented by i to a new destination
    shutil.move(source+i, destination)

