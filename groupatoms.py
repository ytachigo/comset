import numpy as np

def get_getgroupatoms():
    firstatom = int(input('First number of atoms: '))
    lastatom = int(input('Last number of atoms: '))
    filename = 'groupatoms.dat'
    f = open(filename, 'a')

    for i in range(firstatom, lastatom + 1):
        atomnum = '%d, ' % i
        f.write(atomnum)
    f.close()

##### Main Routine #####
get_getgroupatoms()
