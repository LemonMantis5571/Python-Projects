def sum_N_Numbers (n):
  Suma = n * (n+1)/ 2

  for x in range(n+1):
      Suma = Suma + x
      return Suma

Suma = sum_N_Numbers(10)
print(Suma)  
    
#recursion 
def sum_N_Numbers (n):
  if n <= 1:
    return n
  else:
    return n + sum_N_Numbers (n - 1)
    
print(sum_N_Numbers(5))