# Digit factorials
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

factorials = {}
def factorial(number):
  if number <= 2:
    return number
  elif number in factorials:
    return factorials[number]
  else:
    factorials[number] = number * factorial(number - 1)
    return factorials[number]


