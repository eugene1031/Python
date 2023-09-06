age = int(input("Enter your age:"))
if age > 100 :
    print("You are too old!")
elif 0 <= age < 18:
    print("You are not old enough!")
elif age < 0:
    print("You are not born yet!")
else :
    print("It's ok!")