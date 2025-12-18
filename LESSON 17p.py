print("Welcome to Python pizza Deliveries!")

bill = 0

size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    size =="L"
    bill =25
pepperoni = input("Do you want pepperoni on you Pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3
    
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill = bill + 1
print(f"you final bill is ${bill}")
