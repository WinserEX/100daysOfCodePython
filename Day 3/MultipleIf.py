print("Welcome")
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age "))
    if age < 12:
        bill = 5
        print("Please pay $5")
    
    elif age <= 18:
        bill = 7
        print("please pay $7")
   
    else: 
        bill = 12
        print("You may pay $12")   

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry")