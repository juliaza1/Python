import argparse
import matplotlib.pyplot as pl 

# import all mandelbrot implementations
from mandelbrot_1 import mandelbrot as mandel1
from mandelbrot_2 import mandelbrot as mandel2
from cython_mandelbrot import mandelbrot as mandel3


# create a parser for command-line arguments
parser = argparse.ArgumentParser(description='Create Mandelbrot Fractal Image')
parser.add_argument('--xmin', type=float, default=-1.5, help="(default: %(default)s)")
parser.add_argument('--xmax', type=float, default=1.5 , help="(default: %(default)s)")
parser.add_argument('--ymin', type=float, default=-1.5, help="(default: %(default)s)")
parser.add_argument('--ymax', type=float, default=1.5 , help="(default: %(default)s)")
parser.add_argument('--nx',    type=int, default=256 , help="(default: %(default)s)")
parser.add_argument('--ny',    type=int, default=256 , help="(default: %(default)s)")
parser.add_argument('--niter', type=int, default=1000, help="(default: %(default)s)")
parser.add_argument('--output_filename', default='mandelbrot.png', help="(default: %(default)s)")
parser.add_argument('--colormap', default='Set1', help='One of matplotlib colormaps (default: %(default)s)')
parser.add_argument('--implementation', choices=['python','numpy','cython'], default='cython', help="(default: %(default)s)")

args = parser.parse_args()

# mapping from implementation string to the function
map_func = {'python': mandel1,'numpy': mandel2,'cython': mandel3}
mandel = map_func[args.implementation]

# calculate image
image = mandel(args.xmin, args.xmax, args.ymin, args.ymax, args.nx, args.ny, args.niter)

fig = pl.imshow(image, origin='lower', cmap=pl.get_cmap(args.colormap))
# disable x and y axis
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
pl.axis('off')
pl.savefig(args.output_filename, dpi=300, bbox_inches='tight')
pl.clf()
    
# values used to calculate contest_image  
# xmin: -0.46846
# xmax: -0.46544
# ymin: -0.59392
# ymax: -0.59091
# color map: Set1
