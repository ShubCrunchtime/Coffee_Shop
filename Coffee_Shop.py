x=input("What is your name? ")
print("Welcome "+x+",good morning")
print("What would you like to have?")
Coffee=("$20")
Tea=("$15")
Breakfast=("$5")
print("Coffee      $20")
print("Tea         $15")
print("Breakfast   $5")
c=input("")
if c==("Coffee")or c==("coffee"):
  print("A "+c+" would be"+("$20"))
if c==("Tea")or c==("tea"):
  print("A "+c+" would be"+("$15"))
if c==("Breakfast")or c==("breakfast"):
  print("A "+c+" would be"+("$5"))
elif c!=("Tea")and c !=("tea")and c!=("Coffee")and c!=("coffee")and c!=("Breakfast")and c!=("breakfast"):
  print("Sorry we do not offer that.")

