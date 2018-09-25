#import requests
#import json
import genderize
from genderize import Genderize

#path = "/Volumes/ChenLab3TB1/LFW_data/"
#path = "/Users/Narae/Documents/face_recognition-master/mystuff/"

def find_gender(firstname):
    result = Genderize().get([firstname])[0]
    lfwgender.write(firstname + "\t")
    try:
        if result["gender"] == None:
            lfwgender.write("?")
        elif float(result["probability"]) > 0.9:
            lfwgender.write(result["gender"])
        else:
            lfwgender.write("?")
    except Exception:
        lfwgender.write("?")
        print("Error: " + firstname)
    lfwgender.write("\n")

lfwnames = open("lfw-names2.txt")
lfwgender = open("lfw-gender.txt", "a")

nextline = lfwnames.readline()
firstname_prev = nextline.split()[0].split("_")[0]

while nextline:
#for i in range(10):
    firstname = nextline.split()[0].split("_")[0]
    if firstname != firstname_prev:
        find_gender(firstname_prev)
        firstname_prev = firstname
    nextline = lfwnames.readline()

find_gender(firstname)

lfwnames.close()
lfwgender.close()
