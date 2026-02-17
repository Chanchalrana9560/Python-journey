try:
  a = int(input("Enter a: "))
  b = int(input("Enter a: "))
  print(a/b)
except ZeroDivisionError as v:
  print("Infinite")

