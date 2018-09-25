with open("lfw-gender.txt") as lfwgender, open("unknown-gender.txt") as unknowngender, open("lfw-gender2.txt", "w") as newfile:
    nextline = lfwgender.readline()
    while nextline:
        firstname, gender = nextline.split()
        if gender != "?":
            newfile.write(nextline)
        else:
            unline = unknowngender.readline().split()
            unfirstname = unline[0]
            ungender = unline[1]
            try:
                unprob = float(unline[2])
            except Exception:
                pass
            
            if firstname != unfirstname:
                print("Error: %s, %s don't match up" % firstname, unfirstname)
            elif ungender == "?" or unprob < 0.8:
                newfile.write(nextline)
            else:
                newfile.write("%s\t%s\n" % (unfirstname, ungender))

        nextline = lfwgender.readline()
    
