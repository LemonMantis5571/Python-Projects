def getSquare():
  ##Write your code here
  l1 = [] ##Create the list here
  l1 = [x * x for x in range (0,21,2) if x % 3 !=0]
  return l1

l1 = getSquare()
print(l1)