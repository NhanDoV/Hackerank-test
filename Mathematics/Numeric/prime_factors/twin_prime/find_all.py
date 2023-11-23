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
        return 1
    else:
        return 0

for num in range(3, 100):
    check_1 = is_prime(num)
    if check_1:
        check_2 = is_prime(num + 2)
        if check_2:
            print(f"Bot {num} and {num + 2} are a twin!!")