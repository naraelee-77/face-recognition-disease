with open('2DMOT2015Labels/train/PETS09-S2L1/gt/gt.txt') as mult_gt, \
     open('2DMOT2015Labels/train/PETS09-S2L1/gt/sing_gt.txt', 'w') as sing_gt:
    nextline=mult_gt.readline()
    idnum=15

    while nextline:
        line=nextline.split(',')
        if line[1]==idnum:
            sing_gt.write(','.join(line[2:6])+'\n')
        nextline=mult_gt.readline()
