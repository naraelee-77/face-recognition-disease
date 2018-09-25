def five_digits(number):
    num_str = "00000" + str(number)
    return num_str[-5:]

path1 = "/Volumes/ChenLab3TB1/colorferet/dvd1/data/ground_truths/name_value"
path2 = "/Volumes/ChenLab3TB1/colorferet/dvd2/data/ground_truths/name_value"

allfile = open("/Volumes/ChenLab3TB1/colorferet/myinfo/masterfile.txt", "w")
males = females = total = unavailable = 0

for i in range(1, 1209):
    idnum = five_digits(i)
    pathname = ""
    if i < 740:
        pathname += path1
    else:
        pathname += path2
    pathname += "/" + idnum + "/" + idnum + ".txt"
    
    try:
        file = open(pathname)
        contents = file.readlines()
        gender = contents[1].split("=")[1].strip("\n")
        yob = contents[2].split("=")[1].strip("\n")
        race = contents[3].split("=")[1].strip("\n")
        allfile.write(idnum + "\t" + gender + "\t" + yob + "\t" + race + "\n")
        if gender == "Male":
            males += 1
        else:
            females += 1
        total += 1
        file.close()
    except FileNotFoundError:
        unavailable += 1

allfile.write("\nSummary:" +
              "\nMales: " + str(males) +
              "\nFemales: " + str(females) +
              "\nTotal: " + str(total) +
              "\nUnavailable: " + str(unavailable))

allfile.close()
