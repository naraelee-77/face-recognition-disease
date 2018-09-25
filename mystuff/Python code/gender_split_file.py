import shutil
from shutil import copyfile
import bz2
import os

path1 = "/Volumes/ChenLab3TB1/colorferet/dvd1/data/images/"
path2 = "/Volumes/ChenLab3TB1/colorferet/dvd2/data/images/"
malespath = "/Volumes/ChenLab3TB1/colorferet/myinfo/males/"
femalespath = "/Volumes/ChenLab3TB1/colorferet/myinfo/females/"

shutil.rmtree(malespath[:-1])
shutil.rmtree(femalespath[:-1])
os.mkdir(malespath[:-1])
os.mkdir(femalespath[:-1])

masterfile = open("/Volumes/ChenLab3TB1/colorferet/myinfo/masterfile.txt")
fafile = open("/Volumes/ChenLab3TB1/colorferet/dvd1/doc/partitions/fa.txt")

faline = fafile.readline()

while faline:
    idnum = faline.split()[0]
    pathname = ""
    if int(idnum) < 740:
        pathname = path1
    else:
        pathname = path2
    pathname += faline.replace(" ", "/").strip("\n") + ".bz2"
    dest = faline.split()[1].strip("\n") + ".bz2"

    gender = masterfile.readline().split()[1]
    if gender == "Male":
        destination = malespath + dest
    else:
        destination = femalespath + dest
    newfile = open(destination, "w")
    copyfile(pathname, destination)
        
    faline = fafile.readline()
    
fafile.close()
masterfile.close()
