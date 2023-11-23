#!/bin/python3

import math
import os
import random
import re
import sys

def is_prime(x):
    prime_factors = []
    for k in range(2, 1 + x//2):
        if x % k == 0:
            prime_factors.append(k)
    if len(prime_factors) == 0:
        print(f"{x} is a prime number")
        return 1
    else:
        print(f"{x} is not a prime because it had more than 2 factors lower itself: {prime_factors}")
        return 0
    
def is_twin(x, y):
    check_x = is_prime(x)
    check_y = is_prime(y)

    if (check_x == check_y) & check_y == 1:
        if abs(x - y) == 2:
            print(f"both the prime.numbers {x} and {y} is a twin")
        else:
            print(f"Both of this prime.numbers {x} and {y} is not a twin")
    else:
        print("Not satisfy a twin!!")

if __name__ == '__main__':
    x = int(input("Input the first number: "))
    y = int(input("Input the second number: "))

    is_twin(x, y)