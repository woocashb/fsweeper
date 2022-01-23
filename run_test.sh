#!/bin/bash

workdir=./messy_dir
./mk_clutter.sh rm && ./mk_clutter.sh && ./fsweeper.py

ls $workdir 

