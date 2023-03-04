#!/bin/ env Python 3
import math

def my_sqrt(a):
    x = a/2.0
    while True:
        y = (x + a/x) / 2.0
        if abs(y - x) < 1e-14:
            break
        x = y
    return x
print("Below are tests of the function my_sqrt")
print("The squareroot of 64 =", my_sqrt(64))
print("The squareroot of 25 =", my_sqrt(25))
print("The squareroot of 36 =", my_sqrt(36))
def test_sqrt():
    for a in range(1, 26):
        my_s = my_sqrt(a)
        math_s = math.sqrt(a)
        diff = abs(my_s - math_s)
        print(f"a = {a} | my_sqrt(a) = {my_s:.11f} | math.sqrt(a) = {math_s:.11f} | diff = {diff:.11f}")

test_sqrt()
