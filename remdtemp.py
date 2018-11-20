import numpy as np

def get_remdtemp():
    n = input('Replica number: ')
    mintmp = input('Minimum temperature (K): ')
    maxtmp = input('Maximum temperature (K): ')
    const = np.log(maxtmp / mintmp) / (n - 1)
    filename = 'temperatures.dat'
    f = open(filename, 'a')

    for i in range(0, n):
        temp = mintmp * np.exp(const * n)
        f.write(temp)

##### Main Routine #####
convert_1lto3l()