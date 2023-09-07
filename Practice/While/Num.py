num = int(input("請輸入一個1~10的整數:"))
while num < 1 or num > 10 :
    print(f"你輸入的值{num}是無效的")
    num = int(input("請輸入一個1~10的整數:"))
print(f"你輸入的值是{num}")