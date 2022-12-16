# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower1 = name1.lower()
lower2 = name2.lower()

names = lower1 + lower2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

trueScore = t + r + u + e
loveScore = l + o + v + e

score = f"{str(trueScore) + str(loveScore)}"

scoreInt = int(score)

if scoreInt < 10 or scoreInt > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif scoreInt >= 40 and scoreInt <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
   print(f"Your score is {score}.") 



# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."


