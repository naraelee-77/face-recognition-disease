with open("lfw-gender-0.80.txt") as lfwgender, \
     open("manual-gender.txt") as manual, \
     open("lfw-gender-final.txt", "w") as final:
    nextline = lfwgender.readline()
    
    while nextline:
        firstname, gender = nextline.split()
        if gender != "?":
            final.write(nextline)
        else:
            manualline = manual.readline()
            first, gen = manualline.split()
            
            if firstname != first:
                print("Error: %s, %s don't match up" % firstname, first)
            else:
                final.write(manualline)

        nextline = lfwgender.readline()
    
