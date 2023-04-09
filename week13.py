#!/usr/bin/env python3.7

import os

#working directory
current_dir = os.getcwd()

#empty list to store file info
file_info = []

# walk through directory tree and get file info 
for dirpath, dirnames, filenames in os.walk(current_dir):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_size = os.path.getsize(file_path)
        file_info.append({"name": file, "size": file_size})

#Print list of file information
for file in file_info:
    print(file)
