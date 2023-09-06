#kglb轉換
weight = float(input("輸入你的體重："))
kglb = input("輸入單位為kg還是lb:")
if kglb == "kg" :
    weight *= 2.2
    newkglb = "LB"
elif kglb == "lb" :
    weight /= 2.2
    newkglb = "KG"
print(f"你的體重是{round(weight, 2)}{newkglb}")