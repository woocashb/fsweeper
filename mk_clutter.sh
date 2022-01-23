#!/bin/bash

extensions=("mp3" "avi" "PDF")
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
