import datetime

x = datetime.datetime.now()

name = input("Enter Your Name :- ")
age = input("Enter Your Age :- ")

age = int(age)

print(f"Name {name}.")
print(f"Age {age}.")

remainingAge = 100 - age
yearsTurn = x.year + remainingAge

print(f"You are turn 100 on year of  {yearsTurn}.")




# name = input("Tell me Your Name: ")
# print(name)
#
# age = input("Please enter your age: ")
# print(age)
#
# year=2019+(100-int(age))
# print(f"{name} will 100 years old in,{year}")