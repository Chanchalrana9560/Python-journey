from functools import reduce
l = [1, 2, 3423, 53, 54, 547, 98, 888,55,50, 55,11]

def greater(a, b):
  if(a>b):
    return a
  return b

print(reduce(greater,l))