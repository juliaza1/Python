#!/usr/bin/python

"""This module runs unit test for functions"""
class UnitTest(object):
    """Main"""
    def __init__(self, func, args, kwargs, res):    # make test
        """	Argumenter: 
        func er selve funksjonen som skal kalles
		args er input-argumentene til funksjonen
		kwargs er keyword arguments til funksjonen
		res er forventet resultat		
    """
        self.func = func
        self.res = res
        self.args = args
        self.kwargs = kwargs          
    
    
    def __call__(self):                             # run test
       	"""Kaller funksjonen og sjekker resultatet"""
        try:
            if self.res==self.func(*self.args, **self.kwargs):
                return True
            else:
                return False
        except: 
            return False