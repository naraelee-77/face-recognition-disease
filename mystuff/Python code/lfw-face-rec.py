import face_recognition as frec

with open("lfw-gender-final.txt") as lfwgender, \
open("lfw-names.txt") as lfwnames, \
open("face-rec.csv", "w") as facerec:
    nextline = lfwnames.readline()
    first = gender = ""
    while nextline:
#    for n in range(50):
        fullname = nextline.split()[0]
        firstname = fullname.split("_")[0]
        if firstname != first:
            first, gender = lfwgender.readline().split()
            if firstname != first:
                print("Error: %s, %s do not match" % (firstname, first))
                break

        try:
            image = frec.load_image_file("lfw-deepfunneled/%s/%s_0001.jpg" % (fullname, fullname))
            facearray = frec.face_encodings(image)[0]
            facerec.write("%s,%s" % (fullname, gender))
            for i in range(len(facearray)):
                facerec.write(",%f" % facearray[i])
            facerec.write("\n")
        except Exception:
            print("Error: %s" % fullname)
        
        nextline = lfwnames.readline()
