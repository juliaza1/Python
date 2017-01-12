#mandelbrot.pyx
import cython
cimport numpy as np 
import numpy as np

# compile with: python cython_setup build_ext --inplace


@cython.profile(False)
cdef inline int iterate(double x, double y, int niter):
    '''
    x -- x coordinate of pixel
    y -- y coordinate of pixel
    niter -- maximum number of iterations
    Returns the number of iterations needed to 
    exceed 2 
    '''
    cdef double freal = 0, fimag = 0
    cdef int n

    for n in range(niter):
        # f = f^2 + C
        freal, fimag = freal*freal - fimag*fimag + x, 2*freal*fimag + y
        if fimag*fimag + freal*freal > 4.0:
            break
    return n
    

@cython.boundscheck(False)
def mandelbrot(double xmin, double xmax, double ymin, double ymax, int nx, int ny, int niter=1000):
    '''
    nx -- x resolution
    nx -- y resolution
    niter -- maximum number of iterations
    
    Returns mandelbrot image on the rectangle
    defined by xmin .. xmax, ymin .. ymax with
    the resolution nx x ny
    '''
    # 2d array of zeros
    cdef np.ndarray image = np.zeros((nx, ny))

    cdef double dx = (xmax - xmin) / nx # x step
    cdef double dy = (ymax - ymin) / ny # y step
    
    for i in range(ny):
        y = ymin + i*dy
        for j in range(nx):
            x = xmin + j*dx
            # calculate the value of each pixel
            image[i, j] = iterate(x, y, niter)
    
    return image    
    
