def ListofEvenOdds():
  l1 = [x for x in range(0,21) if x % 2 == 0] # list of even numbers
  l2 = [x for x in range(0,21) if x % 2 != 0] # list of odd numbers 
  return [l1, l2]

[l1,l2] = ListofEvenOdds()
print(l1,l2)