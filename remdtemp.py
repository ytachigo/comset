import numpy as np

def get_remdtemp():
    n = int(input('Replica number: '))
    mintmp = int(input('Minimum temperature (K): '))
    maxtmp = int(input('Maximum temperature (K): '))
    const = np.log(maxtmp / mintmp) / (n - 1)
    filename = 'temperatures.dat'
    open_file = open(filename, 'a')

    for i in range(0, n):
        temp = mintmp * np.exp(const * i)
        open_file.write(str(temp))
        open_file.write('\n')
    open_file.close()

##### Main Routine #####
get_remdtemp()
