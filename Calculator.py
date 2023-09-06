a = float(input("Please enter the first number: "))
operator = input("Please enter the operator: ")
b = float(input("Please enter the second number: "))

if operator == "+" :
    print(f"{a + b}")
elif operator == "-" :
    print(f"{a - b}")
elif operator == "*" :
    print(f"{a * b}")
elif operator == "/" :
    if b!= 0 :
        print(f"{a / b}")
    else :
        print(f"分子不能為0")
else : 
    print("運算無效！")


