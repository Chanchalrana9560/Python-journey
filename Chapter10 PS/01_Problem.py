class Programmer:
  company = "Microsoft" 
  def __init__(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin

p = Programmer("Chanchal",1500000,201008)    
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan",1200000,201008)    
print(r.name, r.salary, r.pin, r.company)