#用符號做出長方形
cols = int(input("請輸入請輸入行數："))
rows = int(input("請輸入請輸入列數："))
symbol = input("請輸入符號：")
for i in range(rows) :
    for j in range(cols) :
        print(symbol, end = " ")
    print() #換行
