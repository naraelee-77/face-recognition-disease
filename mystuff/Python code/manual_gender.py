import os

if not os.path.exists("manual"):
    os.makedirs("manual")
    
with open("unknown-gender.txt") as unknown, \
     open("lfw-names.txt") as names, \
     open("manual-gender.txt", "w") as manual:
    nextline = unknown.readline()
    firstname = ""
    
    while nextline:
        array = nextline.split()
        if len(array) == 2:
            first, gender = array
        elif len(array) == 3:
            first, gender, prob = array
            prob = float(prob)
        else:
            print("Error: %s" % nextline)

        if gender == "?" or prob < 0.8:
            manual.write("%s\t\n" % first)
    
        nextline = unknown.readline()
