import face_recognition
import os

def three_digits(number):
    num_str = "000" + str(number)
    return num_str[-3:]

path = "/Volumes/ChenLab3TB1/colorferet/myinfo/"

masterfile = open("/Volumes/ChenLab3TB1/colorferet/myinfo/masterfile.txt")
fafile = open("/Volumes/ChenLab3TB1/colorferet/dvd1/doc/partitions/fa.txt")
wfile = open(path + "machinelearning2.txt", "w")

wfile.write("ID\tImage Name\tGender\tYOB\tRace")
for i in range (1, 129):
    wfile.write("\tAt" + three_digits(i))
wfile.write("\n")

faline = fafile.readline()

while faline:
    idnum, img = faline.split()
    img = img.strip("\n").replace(".ppm", ".jpg")

    idnumber, gender, yob, race = masterfile.readline().split()
    race = race.strip("\n")

    if idnum != idnumber:
        print("Mismatch: " + idnum + ", " + idnumber)
        continue

    wfile.write(idnum + "\t" + img + "\t" + gender + "\t" + yob + "\t" + race)
    
    intermediate = ""
    if gender == "Male":
        intermediate = "males/"
    elif gender == "Female":
        intermediate = "females/"

    image = face_recognition.load_image_file(path + intermediate + img)
    face_array = face_recognition.face_encodings(image)[0]
    for j in range(0, len(face_array)):
        wfile.write("\t" + str(face_array[j]))
        
    wfile.write("\n")
    faline = fafile.readline()

wfile.close()
fafile.close()
masterfile.close()
