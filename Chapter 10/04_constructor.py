class Employee:
  language = "Python" # This is a class attribute
  salary = 1200000
 
  def __init__(self, name, salary, language): # dunder method which is automatically called
    self.name = name
    self.salary = salary
    self.language = language
    print("I am creating an object")
    
  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")

  @staticmethod
  def greet():
    print("Good morning")  

chanchal = Employee("Chanchal", 1300000, "Javascript")
# chanchal.name = "Chanchal"
print(chanchal.name, chanchal.salary, chanchal.language)