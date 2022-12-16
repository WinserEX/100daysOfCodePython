# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
#print(f"Step 1: {bill}")

if add_pepperoni == "Y" and size == "M":
    bill += 3
elif add_pepperoni == "Y" and size == "L":
    bill += 3
elif add_pepperoni == "Y" and size == "S":
    bill += 2
else:
    bill += 0

#print(f"Step 2: {bill}")

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0
#print(f"Step 3: {bill}")

print(f"Your final bill is: ${bill}.")