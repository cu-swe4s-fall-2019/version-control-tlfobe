"""
This module contains basic math operations
"""

import warnings

def div(a, b):
    """
    Takes the quotient of two numbers

    Argumnets
    ---------
    a : int, float
    b : int, float

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

def add(a, b):
    """
    Takes the sum of two numbers

    Arguments
    ---------
    a : int, float
    b : int, float

    Returns
    -------
    s : float
        sum of a and b
    """
    return a + b

def diff(a, b):
    """
    Takes the difference of two numbers

    Arguments
    ---------
    a : int, float
    b : int, float

    Returns
    -------
    d : float
        difference between a and b
    """"

    return a - b

def multiply(a, b):
    """
    Takes the product of two numbers
    
    Arguments
    ---------
    a : int, float
    b : int, float
    
    Returns
    -------
    m : float

    """

    return a * b