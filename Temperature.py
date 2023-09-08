#溫度轉換器
tem = float(input("請輸入溫度："))
unit = input("請輸入單位(C or F)：")

if unit == "C" :
    print(f"溫度為{round(tem * 9 / 5 +32, 2)}F")
elif unit == "F" :
    print(f"溫度為{round(tem - 32 * 5 / 9, 2)}C")
else :
    print("單位有誤")