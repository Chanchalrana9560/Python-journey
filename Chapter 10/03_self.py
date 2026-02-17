class Employee:
  language = "Python" # This is a class attribute
  salary = 1200000

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")

  @staticmethod
  def greet():
    print("Good morning")  

chanchal = Employee()
# chanchal.language = "Javascript" # This is an object instance attribute
chanchal.getInfo()
chanchal.greet()
# Employee.getInfo(chanchal)