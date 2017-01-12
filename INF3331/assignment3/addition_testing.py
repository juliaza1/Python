#!/usr/bin/python

from my_unit_testing import UnitTest

def better_addition(a, b, num_rechecks=2):
    """Returns sum of a, b, but double checks answer several times."""
    sum_computations = [a + b for n in range(num_rechecks)]
    
    for n in range(num_rechecks):
        if sum_computations[n] != sum_computations[n-1]:
            print("Hang on, let me recheck that")
            return better_addition(a, b, num_rechecks)
    # if all computations match, return whichever
    return sum_computations[0]  

num_tests = 0
num_passed = 0
for a, b, n, r in [(4, 7, 0, 11), (4, 7, 4, 11), (2, 2, 2, 4)]:
    # UnitTest() calls the __init__ method
    test = UnitTest(better_addition, [a, b], {"num_rechecks": n}, r)
    num_tests+= 1

    # calls the __call__ method
    if test():                           
        num_passed += 1



print("{}/{} tests passed".format(num_passed, num_tests))

