import math
def my_sqrt(a):
    x = a/2.0   # Choosing the starting value for x
    while True:
         y = (x + a/x) / 2.0
         if y == x:
             break
         x = y
    return x
 
 #The function takes one parameter "a" and starts with an initial value of "x" equal to half of "a". It then repeatedly calculates the average of "x" and "a/x", updates the value of "x" with this average, and checks if the new value of "x" is the same as the previous value of "x". If it is, the function exits the loop and returns the estimate of the square root of "a" (which is stored in "x").


def test_sqrt():
     a = 1
     while a <= 25:
         my_sqrt_val = my_sqrt(a)
         math_sqrt_val = math.sqrt(a)
         diff = abs(my_sqrt_val - math_sqrt_val)
         print("a = {} | my_sqrt(a) = {} | math.sqrt(a) = {} | diff = {}".format(a, my_sqrt_val, math_sqrt_val, diff))
         a += 1
 
#The function starts by defining "my_sqrt" function, which takes "a" as input and returns an estimate of the square root of "a" using the algorithm provided in Section 7.5.    


#The "test_sqrt" function initializes "a" to 1 and loops through values of "a" up to 25. For each value of "a", it calls both "my_sqrt" and "math.sqrt" functions to obtain the estimated square root using both methods. It then calculates the absolute difference between the two estimates and prints a formatted string containing the values of "a", "my_sqrt(a)", "math.sqrt(a)", and "diff".
test_sqrt() #This will print a table of values for the square root of "a" from 1 to 25 using both "my_sqrt" function and "math.sqrt" function, along with the absolute difference between them.

