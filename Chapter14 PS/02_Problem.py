# Create a class Laptop with attributes: brand, RAM, price. Create 2 object with diffrent values.

class Laptop:
  brand = "default"
  RAM = "default 8GB"
  prices = "default 1 Lakh"

obj1 = Laptop()
obj1.brand = "Lenovo"
obj1.RAM = "16GB"
print("Laptop1 Brand -", obj1.brand)
obj2 = Laptop()
obj2.brand = "Macbook"
print("Laptop2 Brand -", obj2.brand)



