class Employee:
  language = "Python" # This is a class attribute
  salary = 1200000

chanchal = Employee()
chanchal.language = "Javascript" # This is an object instance attribute
print(chanchal.language, chanchal.salary)