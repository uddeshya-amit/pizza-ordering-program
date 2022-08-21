
#rates provided for different pizzas

def Margerita():

      bill = 0
      if size == "S":
          bill += 150
      elif size == "M":
          bill += 199
      else:
         bill += 249
      if extra == "Y":
         if size == "S":
            bill += 20
         elif size == "M":
             bill += 30
         else:
           bill += 50

      if coke == "yes":
         bill += 25
      print(f"your final bill is {bill}")

      print("Thank you order again")


def Onion():

      bill = 0
      if size == "S":
          bill += 99
      elif size == "M":
          bill += 150
      else:
         bill += 200
      if extra == "Y":
         if size == "S":
            bill += 20
         elif size == "M":
             bill += 30
         else:
           bill += 50

      if coke == "yes":
         bill += 25
      print(f"your final bill is {bill}")

      print("Thank you order again")


def Sweet_corn():

      bill = 0
      if size == "S":
          bill += 130
      elif size == "M":
          bill += 160
      else:
         bill += 200
      if extra == "Y":
         if size == "S":
            bill += 20
         elif size == "M":
             bill += 30
         else:
           bill += 50

      if coke == "yes":
         bill += 25
      print(f"your final bill is {bill}")

      print("Thank you order again")

def Special():

      bill = 0
      if size == "S":
          bill += 170
      elif size == "M":
          bill += 249
      else:
         bill += 300
      if extra == "Y":
         if size == "S":
            bill += 20
         elif size == "M":
             bill += 30
         else:
           bill += 50

      if coke == "yes":
         bill += 25
      print(f"your final bill is {bill}")

      print("Thank you order again")


#starting of the program

print("WELCOME  TO  THE  PIZZA  HUB ")


print("MENU!\n1.Margerita pizza\n2.Onion pizza\n3.Sweet Corn pizza\n4.Special pizza")


pizza = input("Enter your choice ")

size=input("What size do you prefer 'S' 'M' 'L' ")
extra=input("Want some extra cheese? 'Y' or 'N' ")
coke=input("Do you preffer coca cola? 'yes' or 'no' ")

#Calling the function according to the order

if pizza == "Margerita":
   print (Margerita())

if pizza == "Onion":
    print(Onion())

if pizza == "Sweet Corn":
    print(Sweet_corn())

if pizza == "Special":
    print(Special())













