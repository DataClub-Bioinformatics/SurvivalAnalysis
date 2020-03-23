#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#TODO: do a script that 
#1  unpacks the downloaded zip gdc_downloaded_xxxxxxxxxx
#2  Loops through all folders and extract the file and copy the expression value
#   row and id into a new file in our data folder in which the first column is the
#   engsId row of all files.

import os

directory = r"Scripts/TCGA/gdc_download_20200322_231046.742505"
RUNS = 1

def get_files_in_directory(path):
    # Get the root dir (in your case: test)
    rootDir = path.split('\\')[-1]

    # Walk through all subfolder/files
    for root, subfolder, fileList in os.walk(path):
        for file in fileList:
            # Skip empty dirs
            if file != '':
                # Get the full path of the file
                fullPath = os.path.join(root,file)

#                # Split the path and the file (May do this one and the step above in one go
#                path, file = os.path.split(fullPath)

                # For each subfolder in the path (in REVERSE order)
                subfolders = []
                for subfolder in path.split('\\')[::-1]:

                    # As long as it isn't the root dir, append it to the subfolders list
                    if subfolder == rootDir:
                        break
                    subfolders.append(subfolder)

                # Print the list of subfolders (joined by '-')
                # + '-' + file
                print('{}-{}'.format( '\n'.join(subfolders), file) )
                
def run_os_scandir():
    for i in range(RUNS):
        fu = [f.path for f in os.scandir(directory) if f.is_dir()]
    print(fu)

run_os_scandir()
#path=sys.argv[1]
#print(path)
#get_files_in_directory(path)