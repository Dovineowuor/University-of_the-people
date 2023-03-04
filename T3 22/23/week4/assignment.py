# Part 1
def my_sqrt(a):
  x = a
  while True:
    y = (x + a/x) / 2.0
    if y == x:
      break
    x = y
  return x

#Part 2
def test_sqrt():
  import math
  a = 1
  while a <= 25:
    b = my_sqrt(a)
    c = math.sqrt(a)
    diff = abs(c - b)
    print('a =', a, '|my_sqrt(a) =', b, '|math.sqrt(a) =', c, '| diff =', diff)
    a += 1
  return 0

test_sqrt()
