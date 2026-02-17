class Employee:
  language = "Py" # This is a class attribute
  salary = 1200000

chanchal = Employee()
chanchal.name = "Chanchal" # This is an object attribute
print(chanchal.name, chanchal.language, chanchal.salary)  

piyush = Employee()
piyush.name = "Piyush"
print(piyush.name,piyush.language, piyush.salary) 

# Here name is object attribute and salary and language are class attributes as they directly belong to the class