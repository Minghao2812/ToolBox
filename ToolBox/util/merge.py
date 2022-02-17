"""
Read multiple large files in chunks, user can then process them in chunks, and get a merged output.
"""
#TODO: make this tool a generator-like or decorator. So that it can be embedded elsewhere.

import os
from os import listdir
from os.path import isdir, isfile, join, splitext
import pandas as pd


def get_file_extensions(*paths) -> 'set':
    """
    # Arguments
    paths: tuple[str]; path to folders or single files.
    # Return
    fileExtensions: set[str]; file extensions (e.g. .csv, .json)
    """
    # Parse folder/file directory.
    filePaths = []
    try:
        for path in paths:
            # If one path is a folder.
            if isdir(path):
                folderPath = path
                filePaths += [
                    join(folderPath, f) for f in listdir(folderPath)
                    if isfile(join(folderPath, f))
                ]
            # If one path is a file.
            elif isfile(path):
                filePaths.append(path)
    except:
        raise TypeError("Not a folder of file:", paths)

    # Collect all kinds of file extensions into a set.
    fileExtensions = {splitext(filePath)[1] for filePath in filePaths}
    return fileExtensions


def read_file(filePath, fileExtension):
    """Read file in chunks.
    filePath: str; path to a single file.
    fileExtension: str; extension to a file. 
    """
    # CSV file
    if fileExtension == '.csv':
        #TODO: check the best chunksize
        for chunk in pd.read_csv(filePath,
                                 chunksize=100000,
                                 low_memory=False,
                                 encoding='utf-8'):
            pass
            # Process a chunk.

    # JSON file
    elif fileExtension == '.json':
        #TODO: check the best way to read_json
        for chunk in pd.read_json(filePath, chunksize=100000,
                                  encoding='utf-8'):
            pass
            # Process a chunk.

    # Pickle file