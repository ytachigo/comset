import re

def convert_1lto3l():
    get_file = input('Filename: ')
    amino_dict = { 
        'A': ' ALA ', 'B': ' ASX ', 'C': ' CYS ',
        'D': ' ASP ', 'E': ' GLU ', 'F': ' PHE ',
        'G': ' GLY ', 'H': ' HIS ', 'I': ' ILE ',
        'K': ' LYS ', 'L': ' LEU ', 'M': ' MET ',
        'N': ' ASN ', 'P': ' PRO ', 'Q': ' GLN ',
        'R': ' ARG ', 'S': ' SER ', 'T': ' THR ',
        'U': ' SEC ', 'V': ' VAL ', 'W': ' TRP ',
        'X': ' XAA ', 'Y': ' TYR ', 'Z': ' GLX '
         }

    for line in open(get_file, 'r'):
        output = 'convertedto3l.dat'
        open_file = open(output, 'a')

        if line[0] != '#':
            new_line = 'sequence {'
            for str in list(line):
                if re.match('[A-Z]', str):
                    new_line += amino_dict[str]
                else:
                    new_line += str
            open_file.write(new_line+'}\n\n')
        else:
            open_file.write(line)
    open_file.close() 
    
##### Main Routine #####
convert_1lto3l()