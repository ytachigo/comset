import numpy as np

def get_getgroupatoms():
    firstatom = int(input('First number of atoms: '))
    lastatom = int(input('Last number of atoms: '))
    filename = 'groupatoms.dat'
    open_file = open(filename, 'a')

    for i in range(firstatom, lastatom + 1):
        atomnum = '%d, ' % i
        open_file.write(atomnum)
    open_file.close()

##### Main Routine #####
get_getgroupatoms()
