import unittest
import numpy as np
import mandelbrot

class TestMandelbrot(unittest.TestCase):

    def test_outside(self):
        '''
        Check if all values are outside the mandelbrot set --
        all pixels are zeros
        '''
        image = mandelbrot.compute_mandelbrot(3, 4, 3, 4, 256, 256, 1000)
        self.assertEqual(image.all(), 0)

    def test_isde(self):
        '''
        Check if all values are outside the mandelbrot set --
        all pixels are non zeros
        '''
        image = mandelbrot.compute_mandelbrot(-0.5, 0.5, -0.5, 0.5, 256, 256, 1000)
        self.assertTrue(image.all() > 0)

if __name__ == '__main__':
    unittest.main()

