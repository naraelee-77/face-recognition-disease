import face_recognition as frec

path = '/Volumes/ChenLab3TB1/imdb/'

with open(path + 'age_bins/age4-12bin.csv') as rfile, \
     open(path + 'age_bins/age4-12encodings.csv', 'w') as wfile:
    nextline = rfile.readline()
    while nextline:
##    for n in range(10):
        nextline = nextline.strip()
        index, _, age, gender, fullpath = nextline.split(',')
        try:
            image = frec.load_image_file(path + 'imdb_crop/' + fullpath)
            enc = frec.face_encodings(image)[0]
            wfile.write(age + ',' + gender)
            for i in range(128):
                wfile.write(',%f' % enc[i])
            wfile.write('\n')
        except Exception as e:
            print(index + ', ' + fullpath + '\n' + str(e) + '\n')
        nextline = rfile.readline()
