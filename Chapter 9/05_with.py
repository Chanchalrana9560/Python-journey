f = open("this.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("this.txt") as f:
  print(f.read())

# you dont have explicity close the file 