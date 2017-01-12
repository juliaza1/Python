from cython_mandelbrot import mandelbrot
import matplotlib.pyplot as pl



def compute_mandelbrot(xmin, xmax, ymin, ymax, nx, ny, max_escape_time=1000, plot_filename=None):

    image = mandelbrot(xmin, xmax, ymin, ymax, nx, ny, max_escape_time)
    
    if plot_filename:
        fig = pl.imshow(image, origin='lower')
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        pl.axis('off')
        pl.savefig(plot_filename, dpi=300, bbox_inches='tight')
        pl.clf()
    
    return image
