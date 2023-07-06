#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:34:54 2023

@author: mayabuggs
"""

import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term.
    
    Parameters:
    n (int): The number of Fibonacci terms to generate.
    
    Returns:
    numpy.ndarray: Array containing the Fibonacci sequence.
    """
    fib_sequence = np.zeros(n, dtype=int)
    fib_sequence[0] = 1
    fib_sequence[1] = 1

    for i in range(2, n):
        fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]

    return fib_sequence

def calculate_ratios(fib_sequence):
    """
    Calculate the ratios d[n] = f[n+1] / f[n] for the Fibonacci sequence.
    
    Parameters:
    fib_sequence (numpy.ndarray): Fibonacci sequence.
    
    Returns:
    numpy.ndarray: Array containing the ratios d[n].
    """
    n = len(fib_sequence)
    ratios = np.zeros(n-1, dtype=float)

    for i in range(1, n-1):
        ratios[i] = fib_sequence[i+1] / fib_sequence[i]

    return ratios

# Generate the first 100 Fibonacci numbers
F = fibonacci(100)

# Calculate the ratios d[n]
D = calculate_ratios(F)

# Plot the ratios
plt.plot(D)
plt.xlabel('n')
plt.ylabel('d[n]')
plt.title('Fibonacci Ratio Plot')
plt.show()
