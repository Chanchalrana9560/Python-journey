
def greatest(a, b, c):
  if(a>b and a>c):
    return a
  elif(b>a and b>c):
    return b
  elif(c>b and c>a):
    return a
  

a = 1 
b = 45
c = 3
print(greatest(a,b,c))