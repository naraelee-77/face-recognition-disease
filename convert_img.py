from PIL import Image

malespath = "/Volumes/ChenLab3TB1/colorferet/myinfo/males/"
femalespath = "/Volumes/ChenLab3TB1/colorferet/myinfo/females/"

masterfile = open("/Volumes/ChenLab3TB1/colorferet/myinfo/masterfile.txt")
fafile = open("/Volumes/ChenLab3TB1/colorferet/dvd1/doc/partitions/fa.txt")

faline = fafile.readline()

while faline:
    idnum = faline.split()[0]
    pathname = ""
    gender = masterfile.readline().split()[1]
    
    if gender == "Male":
        pathname += malespath + faline.split()[1].strip("\n")
    else:
        pathname += femalespath + faline.split()[1].strip("\n")

    Image.open(pathname).save(pathname.replace(".ppm", ".jpg"))
            
    faline = fafile.readline() 
        
fafile.close()
masterfile.close()
