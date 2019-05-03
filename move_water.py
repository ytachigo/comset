import numpy as np

def move_water(): # Move water molecules
    maxcoord = 40
    mincoord = -40
    addcoord = 100

    filename = input('Filename(pdb): ')
    open_infile = open(filename, 'r')

    for kline in open_infile.readlines():
        output = 'move_water.pdb'
        open_outfile = open(output, 'a')

        if kline[0:4] == 'ATOM' or kline[0:6] == 'HETATOM':
            if str(kline[16:20].strip()) == 'TIP3' and \
            maxcoord >= float(kline[47:54]) and mincoord <= float(kline[47:54]):
                newcoord = str(round((float(kline[47:54]) + addcoord), 3))
                for i in range(0, 7 - len(newcoord) + 1):
                    newcoord = ' ' + newcoord
                nline = kline[:46] +  newcoord + kline[54:]
                open_outfile.write(nline)

            else: open_outfile.write(kline)
        else: open_outfile.write(kline)
    open_outfile.close()
    open_infile.close()

##### Main Routine #####
move_water()
