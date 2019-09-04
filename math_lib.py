"""
This module contains basic math operations
"""

import warnings

def div(a, b):
    """
    Takes the quotient of two numbers

    Argumnets
    ---------
    a : float
    b : float

    Returns
    -------
    q : float
        quotient of a and b.
    """
    if b == 0:
        warnings.warn('Cannot Divide by 0! Returning None')
        return None
    else:
        return a/b
