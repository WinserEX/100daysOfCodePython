#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("How much was the bill? \n")

people = input(f"How many people are paying for the ${bill}? \n")

split = round(float(bill)/int(people), 2)

tip = input(f"Each person should pay ${split}, what percentage would you like to give as a tip? \n")

tipPer = int(tip)/100 

print(f"Since you want to tip {tip}%, each person should pay ${round(split * (tipPer + 1), 2)}")
