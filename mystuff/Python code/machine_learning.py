import face_recognition
import os

path = "/Volumes/ChenLab3TB1/colorferet/myinfo/"

wfile = open(path + "machinelearning.txt", "w")

marray = os.listdir(path + "males")

for i in range(0, len(marray)):
    image = face_recognition.load_image_file(path + "males/" + marray[i].strip("._"))
    face_array = face_recognition.face_encodings(image)[0]
    wfile.write("M")
    for j in range(0, len(face_array)):
        wfile.write("\t" + str(face_array[j]))
    wfile.write("\n")

farray = os.listdir(path + "females")

for i in range(0, len(farray)):
    image = face_recognition.load_image_file(path + "females/" + farray[i].strip("._"))
    face_array = face_recognition.face_encodings(image)[0]
    wfile.write("F")
    for j in range(0, len(face_array)):
        wfile.write("\t" + str(face_array[j]))
    wfile.write("\n")

wfile.close()
