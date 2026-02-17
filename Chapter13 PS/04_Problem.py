def divisible5(n):
  if(n%5 == 0):
    return True
  return False

a = [1, 2, 3423, 53, 54, 547, 98, 888,55,50]
f = list(filter(divisible5, a))
print(f)