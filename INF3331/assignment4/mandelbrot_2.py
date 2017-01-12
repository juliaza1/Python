import matplotlib.pyplot as pl
import numpy as np


def iterate(x, y, niter):
    '''
    x -- x coordinate of pixel
    y -- y coordinate of pixel
    niter -- maximum number of iterations
    Returns the number of iterations needed to 
    exceed 2 
    '''
    f = 0
    C = complex(x, y)
    for n in range(niter):
        f = f**2 + C
        if f.imag**2 + f.real**2 > 4.0:
            break
    return n


def mandelbrot(xmin, xmax,ymin, ymax, nx, ny, niter=1000):
    '''
    nx -- x resolution
    nx -- y resolution
    niter -- maximum number of iterations
    
    Returns mandelbrot image on the rectangle
    defined by xmin .. xmax, ymin .. ymax with
    the resolution nx x ny
    '''
    # make a function that can be applied to each
    # element of array in a vectorized way
    vfunc  = np.vectorize(iterate)  
    xarr   = np.linspace(xmin, xmax, nx) # equaly spaced array of x values
    yarr   = np.linspace(ymin, ymax, ny) # equaly spaced array of y values
    # make 2 2d arrays that contain x and y grids for the image
    XX, YY = np.meshgrid(xarr, yarr)
    image  = vfunc(XX, YY, niter)
    
    return image
    

if __name__ == '__main__':    
    # calculate 256x256 image limited by the rectangle -1.5..1.5 -1.5..1.5 
    image = mandelbrot(-1.5, 1.5, -1.5, 1.5, 256, 256)

    fig = pl.imshow(image, origin='lower')
    # disable x and y axis
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    pl.axis('off')
    pl.savefig('mandelbrot2.png', dpi=300, bbox_inches='tight')
    pl.clf()

