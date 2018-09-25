import face_recognition as frec

def three_digits(number):
    num_str = "000" + str(number)
    return num_str[-3:]

path = "/Volumes/ChenLab3TB1/malformation/22q11.2_deletion/"

with open(path + "22q11.2_encodings.csv", "w") as file:
    for i in range(1, 139):
        try:
            image = frec.load_image_file("%s%s.jpg" % (path, three_digits(i)))
            enc = frec.face_encodings(image)[0]
            file.write("%d" % i)
            for j in range(128):
                file.write(",%f" % enc[j])
            file.write("\n")
        except Exception as e:
            print("%d\n%s\n" % (i, str(e)))
    for i in range(1, 16):
        try:
            image = frec.load_image_file("%salt%s.jpg" % (path, i))
            enc = frec.face_encodings(image)[0]
            file.write("alt%d" % i)
            for j in range(128):
                file.write(",%f" % enc[j])
            file.write("\n")
        except Exception as e:
            print("alt%d\n%s\n" % (i, str(e)))
        
