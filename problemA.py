import matplotlib.pyplot as pl
import numpy as np
import math

def slmake(b, h, w):
    
    #Creates an array with values 0 representing opacity and higher values
    #some degree of transparency. The variable 'w' determines the width. 'b' determines
    #how left-centre the slit begins. 'h' determines the hight of the slit.
    
    slit = []
    for i in range(0, 500):
        slit.append(0)
        if i > 250 - b - math.ceil(w/2) and i <= 250 - b + math.ceil(w/2):
            slit[i] = h
    return slit

def dft(slit):

    #This function performs the discrete fourier transform on the slit created
    #above. RF is the real part; IF is the imaginary part.
    #The return value of this function is a 2D array, [RF, IF].
    
    RF = []
    IF = []
    
    for i in range(0, 500):
        RF.append(0)
        IF.append(0)
    
    for k in range(0, 500):
        #iterate through wavenumbers
        
        for j in range(0, 500):
            #iterate through x-values
            
            x = j - 250

            #these lines discretise the integral
            RF[k] += 1/500 * slit[j] * math.cos( (math.pi * x * (k-250))/250 )
            IF[k] += 1/500 * slit[j] * math.sin( (math.pi * x * (k-250))/250 )

    
    return (RF, IF)

def convolution(a, b):
    #simple algorithm to perform a discrete convolution of a and b
    
    con = []
    for _x in range(0, 500):
        con.append(0)
        for x in range(0, 500):
            con[_x] += a[x]*b[_x-x]

    return con

def main():
    
    r = []
    x = range(0, 500)
    for i in range(0,500):
        r.append(i - 250)
    

    #here I create a slit of height 1, left-shifted by 0, with width 10.
    slit = slmake(0, 1, 10)
    pl.plot(r, slit)
    pl.axis([-250, 250, 0, 12])
    pl.show()
    
    
    F = dft(slmake(10, 1, 10))
    for m in range(0, 500):
        F[0][m] = F[0][m]*F[0][m] + F[1][m]*F[1][m]

    #these lines of code are just to make the plots of each part of the Fourier transform.
    #real part:
    pl.subplot(2, 1, 1)
    pl.plot(r, F[0])
    pl.ylabel("Real part")
    pl.axis([-250, 250, -0.02, 0.02])

    #imaginary part:
    pl. subplot(2, 1, 2)
    pl.plot(r, F[1])
    pl.ylabel("Imaginary part")
    pl.axis([-250, 250, -0.005, 0.005])
    pl.show()

    #this section of code is for the convolution exercise
    #I create a slit of height 1, left-shifted by 0, with width 10.
    slit = slmake(0, 1, 10)
    conslit = convolution(slit, slit)
    F2 = dft(conslit)
    #here I take the absolute value of the convolution's Fourier transform
    for m in range(0, 500):
        F2[0][m] = 1/500 * abs(F2[0][m])

    #this code is to plot the convolution's Fourier transform
    pl.subplot(2, 1, 1)
    pl.plot(r, F2[0])
    pl.title("Fourier transform of convolution")
    pl.axis([-250, 250, 0, 0.0005])

    #here I square the Fourier transform of the slit
    for k in range(0, 500):
        F[0][k] = F[0][k] * F[0][k]

    #now I plot it
    pl.subplot(2, 1, 2)
    pl.plot(r, F[0])
    pl.title("Square of the Fourier transform")
    pl.axis([-250, 250, 0, 0.0005])

    pl.show()
    

if __name__ == '__main__':
    #start the program
    main()
    
