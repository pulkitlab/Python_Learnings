print("Welcome to the Rollercoaster")
height = int(input("Whats your height?"))

if height >=120:
    print("you can ride the rollercoaster")
    age = int(input("Whats your age?"))

    if age <12:
        bill = 5
    elif age <18:
        bill = 7
    else:
        bill =10
    want_photo = input("Do you want the photo?, Press 'Y' for yes and 'N' for No")
    if want_photo == "Y":
        total_bill = bill +3
    else:
        total_bill = bill
    print(total_bill)

else:
    print("You cannot ride the rollercoaster, grow a bit taller, sorry")