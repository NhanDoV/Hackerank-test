#!/bin/python3
import math
import random
import sys
print("A Smith number is a composite number, the sum of whose digits is the sum of the digits of its prime factors obtained as a result of prime factorization")
def solve(n):
    prime_factors = []
    N = n 
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

    if sum_of_input == sum_digit_of_num:
        print(f"{n} is a Smith number")
        return 1
    else:
        return 0

N = int(input("Input the upper bound to limit the Smith-number: "))
for n in range(2, N):
    x = solve(n)