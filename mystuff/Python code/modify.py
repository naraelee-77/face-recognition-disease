import os

def three_digits(number):
    num_str = "000" + str(number)
    return num_str[-3:]

path = "/Volumes/ChenLab3TB1/colorferet/myinfo/"
race_tuple = ("White", "Black-or-African-American", "Asian", "Asian-Middle-Eastern", "Asian-Southern", "Pacific-Islander", "Hispanic", "Native-American", "Other")

rfile = open(path + "machinelearning2.txt")
wfile = open(path + "machinelearning4.txt", "w")

wfile.write("@relation face_rec_modified\n\n")
#wfile.write("@attribute ID string\n")
#wfile.write("@attribute Image string\n")
wfile.write("@attribute Gender {Male,Female}\n")
wfile.write("@attribute YOB integer\n")

wfile.write("@attribute Race_Class {")
for race in race_tuple:
    wfile.write(race)
    if race != "Other":
        wfile.write(",")
wfile.write("}\n")

wfile.write("@attribute race_bool relational\n")
for race in race_tuple:
    wfile.write("  @attribute Race_" + race + " {+,-}\n")
wfile.write("@end race_bool\n")

wfile.write("@attribute encodings relational\n")
for i in range (1, 129):
    wfile.write("  @attribute At" + three_digits(i) + " numeric\n")
wfile.write("@end encodings\n\n")
wfile.write("@data\n")

rfile.readline()
nextline = rfile.readline()
while nextline:
#for i in range(20):
    linearray = nextline.split()
    gender = linearray[4]
#    for i in range(0, 2):
#        wfile.write("\"" + linearray[i] + "\",")
    for i in range(2, 5):
        wfile.write(linearray[i] + ",")

    wfile.write("\"")
    for race in race_tuple:
        if gender == race:
            wfile.write("+")
        else:
            wfile.write("-")
        if race != "Other":
            wfile.write(",")
    wfile.write("\",\"")
    for i in range(-128, -1):
        wfile.write(linearray[i] + ",")
    wfile.write(linearray[-1] + "\"\n")
    
    nextline = rfile.readline()

rfile.close()
wfile.close()
