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

trueScore = t + r + u + e;
loveScore = l + o + v + e;

print(trueScore)
print(loveScore)


