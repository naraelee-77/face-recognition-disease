import genderize
from genderize import Genderize

lfwgender = open("lfw-gender.txt")
unknowngender = open("unknown-gender.txt", "w")

nextline = lfwgender.readline()
while nextline:
#for i in range(3):
    firstname, gender = nextline.split()
    if gender == "?":
        result = Genderize().get([firstname])[0]
        unknowngender.write(firstname + "\t")
        if result["gender"] == None:
            unknowngender.write("?")
        else:
            unknowngender.write(result["gender"] + "\t" + str(result["probability"]))
        unknowngender.write("\n")
        
    nextline = lfwgender.readline()

lfwgender.close()
unknowngender.close()
