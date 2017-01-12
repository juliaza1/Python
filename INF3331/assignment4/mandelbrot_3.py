import matplotlib.pyplot as pl
import numpy as np
from cython_mandelbrot import mandelbrot 


if __name__ == '__main__':   
    # calculate 256x256 image limited by the rectangle -1.5..1.5 -1.5..1.5  
    image = mandelbrot(-1.5, 1.5, -1.5, 1.5, 256, 256)

    fig = pl.imshow(image, origin='lower')
    # disable x and y axis
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    pl.axis('off')
    pl.savefig('mandelbrot3.png', dpi=300, bbox_inches='tight')
    pl.clf()

