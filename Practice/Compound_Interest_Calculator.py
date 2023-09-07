#複利計算機
#複利公式 : 總金額 = 本金 * (1 + 利率/100) ** 時間
money = 0
rate = 0
time = 0

while money <= 0 :
    money = int(input("請輸入你的本金："))
    if money <= 0 :
        print("本金不得<=0")

while rate <= 0 :
    rate = float(input("請輸入利率："))
    if rate <= 0 :
        print("利率不得<=0")

while time <= 0 :
    time = float(input("請輸入欲存放時間："))
    if time <= 0 :
        print("時間不得<=0")

total = round(money * (1 + rate / 100) ** time, 2)
print(f"原來的本金為{money}，存放{time}年後，您的金額會變{total}")