from pathlib import Path # verify paths
from shutil import copy, copy2

'''path="D:\\ankit.txt" # also use "D:/ankit.txt"
path1="D:\\ankit1.txt"
fw = open(path1, 'w')
with open(path) as ft:
    for lines in ft:
        fw.write(lines)

fw.close()

with open(path1) as fr:
    for line1 in fr:
        print(line1.rstrip())
'''
#--------------------------------
# copying with all verifications and taking inputs from user.

source_path = input('Please enter the path: ')
des_path = input('Please enter the path: ')
sobj = Path(source_path)
dobj = Path(des_path)
#print(sobj.exists()) # to check if file exist.
#print(sobj.is_file()) # to check if file or not

if sobj.exists() and dobj.exists():
    if sobj.is_file():
        if dobj.is_dir():
            #copy(source_path, des_path) # copy function does not preserve metadat of file like creadtion date and time etc.
            copy2(source_path, des_path) # it preserve metadata
            print("Coping Done!")
            '''
            source_file_name = sobj.name #it will return the last name. 
            #print(source_file_name)
            with open(source_path) as fs:
                with open(des_path+'\\'+source_file_name, mode='wt') as fsw:
                    for lines in fs:
                        fsw.write(lines)
                    print("Coping Done!")
            '''
        else:
            print('Destination path must be a directory.')
    else:
        print('Source path must be a file.')
else:
    print('Source path does not exist')


