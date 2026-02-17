class FoodItem:
  category= "Snacks"
  def __init__(self, name):
   self.name= name
   print(self.name)
  

fooditem1 = FoodItem("Samosa")
print("Food item is -", fooditem1)
fooditem2 = FoodItem("GulabJamun")
print(fooditem2)

