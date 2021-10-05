import matplotlib.pyplot as pl
import numpy as np
import math

def makeslit(b1, b2, h, r):
    #b1: position of the centre of the first aperture
    #b2: position of the centre of the second aperture
    #h: height of each aperture
    #r: 'radius' of each aperture
    
    aperture_array = np.zeros((50, 50))

    #in the following code I simply iterate through and set all points within
    #the aperture to 1. In this case I create two square sources.
    
    for i in range(0, 50):
        
        for j in range(0, 50):

            if i == 25 - b1[0] and j == 25 - b1[1]:

                for k in range(0, r):
                    for l in range(0, r):
                        aperture_array[i-k][j-l] = 1
                        aperture_array[i+k][j-l] = 1
                        aperture_array[i-k][j+l] = 1
                        aperture_array[i+k][j+l] = 1
                        
            elif i == 25 - b2[0] and j == 25 - b2[1]:
                for k in range(0, r):
                    for l in range(0, r):
                        aperture_array[i-k][j-l] = 1
                        aperture_array[i+k][j-l] = 1
                        aperture_array[i-k][j+l] = 1
                        aperture_array[i+k][j+l] = 1
            

    return aperture_array

def dft(arr):
    
    RF = np.zeros((50,50))
    IF = np.zeros((50, 50))
    F = np.zeros((50, 50))

    #this is a simple 2D, real Fourier transform of a 2D array, 'arr'.
    #the algorithm is the one I covered in the introduction of this report.
    
    for m in range(0, 50):
        k = m - 25
        for n in range(0, 50):
            l = n - 25
            for i in range(0, 50):
                for j in range(0, 50):
                    x = i - 25
                    y = j - 25
                    
                    RF[n][m] += 1/(4*25^2) * arr[j][i] * math.cos( (math.pi*(x*k + y*l))/25)
                    IF[n][m] += 1/(4*25^2) * arr[j][i] * math.sin( (math.pi*(x*k + y*1))/25)
                        
    #set the Fourier transform to its absolute values
    for M in range(0, 50):
        for N in range(0, 50):
            RF[n][m] = abs(RF[n][m])
            F[n][m] = RF[n][m] * RF[n][m] + IF[n][m] * IF[n][m]
            
    return(F)

def main():
    #here all the busywork is done: mostly, plotting.
    
    z = np.zeros((50,50))
    d = np.zeros((50,50))
    for i in range(0, 50):
        for j in range(0, 50):
            z[i][j] = i + j - 50
            d[i][j] = i + j - 50

    Sl = makeslit([0, 0], [15, 9], 1, 5)

    F = dft(Sl)

    #here I plot F with a red-blue colour map to represent its amplitude.
    
    fig, ax = pl.subplots()
    t = pl.imshow(F, cmap=pl.cm.RdBu, vmin=F.min(), vmax=F.max(), extent=[-25,25,-25,25])
    t.set_interpolation('bilinear')
    c = fig.colorbar(t)
    pl.show()

    #here I plot the aperture, also with a red-blue colour map.
    
    tt = pl.imshow(Sl, cmap=pl.cm.RdBu, vmin = Sl.min(), vmax=Sl.max(), extent=[-25, 25, -25, 25])
    tt.set_interpolation('bilinear')
    cc = fig.colorbar(tt)
    pl.show()

if __name__ == '__main__':
    #start the program.
    main()
