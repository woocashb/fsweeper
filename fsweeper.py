#!/usr/bin/python

# Desc: file sweeper - organize files by their extension in given directory 
import os
from os.path import join
import sys
# os.rename does not support cross filesystem file moving as opposed to shutil.move
import shutil


workdir = "./messy_dir"

known_extensions = ('mp3', 'avi', 'pdf')
files = os.listdir(workdir)

for extension in known_extensions:
    for file in files:
        # Check if any file has known extension and create dir for that extension in workdir if it doesnt exist already
        if extension in file:
          if not os.path.exists(join(workdir, extension)):
            os.mkdir(join(workdir, extension))
          shutil.move(join(workdir, file), join(workdir, extension))

    
