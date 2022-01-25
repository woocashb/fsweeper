#!/bin/bash

extensions=("mp3" "avi" "PDF" "doc" 'mp4' 'wav' 'txt' 'torrent' 'mkv')
workdir=./messy_dir

if [[ $1 == 'rm' ]];then
   rm -rf ${workdir}/*
   echo "Cleaned up sandbox directory"
   exit 0
fi


for extension in ${extensions[@]};do
  for num in {1..10};do
    touch "$workdir/plik${num}.${extension}"
  done
done
