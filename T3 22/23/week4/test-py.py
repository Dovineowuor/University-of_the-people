def sum_even_numbers(numbers):
 """
 Return the sum of even numbers in the list. 
 numbers: list of integers.
 returns: int. 
 
 """
 total = 0 
 for number in numbers:
    if number % 2 == 0:
       total += number
 return total

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
print(sum_even_numbers([7, 8, 9, 10, 11, 12]))
print(sum_even_numbers([1, 5, 3, 9, 5, 8]))
print(sum_even_numbers([1, 9, 3, 7, 5, 4]))
