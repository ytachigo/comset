import numpy as np

def get_remdtemp():
    n = int(input('Replica number: '))
    mintmp = int(input('Minimum temperature (K): '))
    maxtmp = int(input('Maximum temperature (K): '))
    const = np.log(maxtmp / mintmp) / (n - 1)
    filename = 'temperatures.dat'
    f = open(filename, 'a')

    for i in range(0, n):
        temp = mintmp * np.exp(const * i)
        f.write(str(temp))
        f.write('\n')
    f.close()

##### Main Routine #####
get_remdtemp()
