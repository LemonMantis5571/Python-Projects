
def removeList():
  l1 = [1, 4, 9, 10, 23]
  
  l2 = [4, 9]
  
  l3 = list(set(l1) - set(l2))

  ## Write your code here
  return l3

l3 = removeList()
print (l3)