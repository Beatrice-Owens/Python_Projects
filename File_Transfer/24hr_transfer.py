

import shutil
import os
import time
import datetime as dt

#defining source & destination
source = '/Users/point/Desktop/FolderA/'

destination = '/Users/point/Desktop/FolderB/'
files = os.listdir(source)
#for every file in "files" var
for i in files:
    mod_time = os.path.getmtime(source+i) #getting modified time in epoch time
    creation_time = os.path.getctime(source+i) #getting creation time in epoch time
    current_time = time.time()
    time_since_mod = current_time - mod_time #determining if the files were modified in the last 24 hrs
    if time_since_mod <= 86400:
        shutil.copy2(source+i, destination)
