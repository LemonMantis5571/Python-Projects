def evenSquareSum():
  even = [x * x for x in range(0, 21, 2)]
  return sum(even)
  
print(evenSquareSum())