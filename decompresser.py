##########################################
# This is a tool used to unzip all zip files in distributed subfolders.
# File construction:
# rootfolder -- subfolder -- file
# Last update on 2020 Dec 19
# Written by Minghao
##########################################


from os import listdir
import zipfile
import rarfile
import os


def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)  # get unzipped file
    # write the unzipped file in the original folder
    if os.path.isdir(file_name.replace(".zip", "")):
        pass
    else:
        os.mkdir(file_name.replace(".zip", ""))
    for names in zip_file.namelist():
        zip_file.extract(names, file_name.replace(".zip", ""))
    zip_file.close()


# un_rar function has some problems. Check later.
def un_rar(file_name):
    """unrar rar file"""
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(file_name.replace(".rar", "")):
        pass
    else:
        os.mkdir(file_name.replace(".rar", ""))
#     os.chdir(file_name.replace(".rar", ""))
    rar.extractall()
    rar.close()


rootfolder = "THE ROOT PATH"
for subfolder in listdir(rootfolder):
    print(subfolder)
    for f in listdir(rootfolder+subfolder+"/"):
        if ".zip" in f:
            un_zip(rootfolder+subfolder+"/"+f)
        if ".rar" in f:
            un_rar(rootfolder+subfolder+"/"+f)
