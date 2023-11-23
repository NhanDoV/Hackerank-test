#!/bin/python3

import math
import random
import sys

# Smith number: 4, 27, 58, 22, 121, 378, 2050918644
def solve(n):
    prime_factors = []
    N = n 
    #for i in range(2, 1+int(math.sqrt(n))):
    for i in range(2, 1+n//2):        
        while N%i == 0:
            prime_factors.append(i)
            N = N // i
        if i < N:
            i = i + 1
        else:
            break
    def sum_digit(n):
        str_num = str(n)
        digit_of_num = [str_num[idx] for idx in range(len(str_num))]
        return sum([int(u) for u in digit_of_num])
    
    sum_of_input = sum_digit(n)
    sum_digit_of_num = sum([sum_digit(primef) for primef in prime_factors])

    print(f"Sum of all digits in {n} is {sum_of_input}")
    print(f"The prime.factor of {n} are {prime_factors}")
    print(f"Sum of all digits of all prime.factor of {n} is {sum_digit_of_num}")
    if sum_of_input == sum_digit_of_num:
        print(f"{n} is a Smith number")
        return 1
    else:
        print(f"{n} is not a Smith number")
        return 0

if __name__ == '__main__':

    print("Nhap gia tri n:")
    n = int(input().strip())
    result = solve(n)