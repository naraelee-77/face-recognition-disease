import face_recognition as frec

path = "/Volumes/ChenLab3Tb1/FDDB_benchmark/"

with open("fddb_benchmark.csv", "w") as fddb:
    for i in range(1,11):
        if i < 10:
            num = "0%d" % i
        else:
            num = "%d" % i
#    num = "01"
        with open("%sFDDB-folds/FDDB-fold-%s.txt" % (path, num)) as fold:
            file = fold.readline()
            while file:
#            for l in range(10):
                file = file.strip("\n")
                try:
                    image = frec.load_image_file("%sFDDB_originalPics/%s.jpg" \
                                                 % (path, file))
                    face_array = frec.face_encodings(image)
                    for j in range(len(face_array)):
                        fddb.write("%s,%s,%s,?" % (num, file[:10], \
                                                   file[file.index("_")+1:]))
                        for k in range(len(face_array[j])):
                            fddb.write(",%s" % face_array[j][k])
                        fddb.write("\n")
                except Exception:
                    print("%s, %s" % (num, file))
                    
                file = fold.readline()
