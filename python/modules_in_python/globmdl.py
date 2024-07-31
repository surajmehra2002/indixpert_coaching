import glob
import os
path=r"D:\Development\C\GitHub\FullstackDeveloper_Indixpert\batch-2"
listoffiles=glob.glob("*.docx",root_dir=path)

print(listoffiles)

print("************************")

print(__file__)

print(os.getcwd())