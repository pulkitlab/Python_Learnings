print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size =="S":
    bill = 15
elif size =="M":
    bill = 20
else:
    bill = 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" and size == "S":
    total_bill = bill +2
elif pepperoni =="Y" and size =="M":
    total_bill = bill +3
elif pepperoni == "Y" and size == "L":
    total_bill = bill +3
else:
    total_bill = bill

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese =="Y":
    total_bill = total_bill +1
else:
    total_bill = total_bill

print("Your final bill is" , total_bill)