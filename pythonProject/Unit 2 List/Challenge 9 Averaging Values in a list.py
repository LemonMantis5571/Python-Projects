def getAverage():
  l1 = [1, 4, 9, 10, 23]
  l2 = sum(l1) / len(l1)
  avg = round(l2,2)
  return avg

avg = getAverage()
print (avg)