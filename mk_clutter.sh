#!/bin/bash

extensions=("mp3" "avi" "pdf")
workdir=./messy_dir


for extension in ${extensions[@]};do
  for num in {1..10};do
    touch "$workdir/plik${num}.${extension}"
  done
done
