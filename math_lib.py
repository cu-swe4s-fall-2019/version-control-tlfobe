"""
This module contains basic math operations
"""

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
        return None
    else:
        return a/b
