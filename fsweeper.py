#!/usr/bin/python

# Desc: file sweeper - organize files by their extension in given directory
import os
from os.path import join
import sys
# os.rename does not support cross filesystem file moving as opposed to shutil.move
import shutil



def usage():
    print("Usage: {} DIR".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
    usage()


workdir = sys.argv[1]

archive_formats = ['zip', 'gz', 'tar', '7z', 'lzma']
audio_formats = ['mp3', 'ogg', 'mp4a', 'wav']
video_formats = ['mp4', 'avi', 'mkv', 'webm', 'mpg', 'mpeg']
image_formats = ['gif', 'jpeg', 'jpg', 'bmp', 'png']
text_formats = ['pdf', 'doc', 'docx', 'xls', 'odf', 'txt', 'xlsx']

known_extensions = { 'archive': archive_formats, 'audio': audio_formats, 'video': video_formats, 'image': image_formats, 'torrent': ['torrent'], 'text': text_formats }

workdir_entries = os.listdir(workdir)
files = []

# sift through directory and save only files
for workdir_entry in workdir_entries:
    if os.path.isfile(join(os.getcwd(), workdir, workdir_entry)):
      files.append(workdir_entry)


for category, extensions in known_extensions.items():
    for file in files:
        for extension in extensions:
            if extension.lower() in file.lower():
              if not os.path.exists(join(workdir, category)):
                os.mkdir(join(workdir, category))
              shutil.move(join(workdir, file), join(workdir, category))
