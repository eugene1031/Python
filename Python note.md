# Python Study Note
## Print
```
print("Hello Python")
```
### f 後面為字串
```
age = 23
print("我今年"+ str(age) + "歲")
等同於
print(f"我今年{age}歲")
```

## 型別轉換
與C++相同

## 輸入
name = input("請輸入名字：")
print(f"你的名字是：{name}")

## 次方
```
a = 3
a = a ** 3   #a^3
a **= 3      #a^3
```
## 最大值最小值
```
print(max(x,y,z))
print(min(x,y,z))
```
## 四捨五入
```
print(round(a))
print(round(a,2))    #到小數點第二位
```
## 無條件進位、無條件捨去
```
import math

x = 9.5
print(math.ceil(x))     #無條件進位 = 10
print(math.floor(x))    #無條件捨去 = 9
```

## If Else
elif = else if
ex.
```
age = int(input("Enter your age:"))
if age > 100 :
    print("You are too old!")
elif 0 <= age < 18:
    print("You are not old enough!")
elif age < 0:
    print("You are not born yet!")
else :
    print("It's ok!")
```
## 邏輯運算子
```
C++ / Python
&&  / and
||  / or
```
## 字串方法
```
help(str)    #搜尋方法

len()        #字串長度
find()       #找某字or符號or空格
capitalize() #第一個字母大寫
upper()      #全部大寫
lower()      #全部小寫
count()      #數某字or符號or空格數量
replace()    #把括號後面的東西取代前面的
isalpha()    #全部都是英文
```
## 字串索引
```
abc = "123-456-789"
first_char = abc[0]
first_three = abc[0:3]    #1~3字元
last_one = abc[-1]        #最後一個字元
last_two = abc[-2]
```
## email字串分析
email = "eugene2165@gmail.com"
index = email.index("@")
print(email[:index])        #eugene2165
print(email[index+1:])      #gmail.com
## f-string字串格式化
```
price1 = 3.234
price2 = -77
price3 = 15.11

#小數點精確度 (.?f)
print(f"price1:{price1:.2f}\n"
      f"price2:{price2:.2f}\n"
      f"price3:{price3:.2f}\n")    #皆取到小數點後兩位

#加上正或負號 (+)
print(f"price1:{price1:+.2f}\n"
      f"price2:{price2:+.2f}\n"
      f"price3:{price3:+.2f}\n")

#對齊 (< > ^)
print(f"price1:{price1:<10.2f}\n"
      f"price2:{price2:<10.2f}\n"
      f"price3:{price3:<10.2f}\n")    #空格為10位並靠左對齊

#混用不同符號
print(f"price1:{price1:<+.2f}\n"
      f"price2:{price2:<+.2f}\n"
      f"price3:{price3:<+.2f}\n")     #靠左對齊、要加正負號、小數點到第二位
```
## While
ex.1
```
name = ""
while name == "" :
    name = input("請輸入你的名字：")
print(f"你好！ {name}!")
```

ex.2
```
food = input("請輸入你喜歡的食物：")
while food != "q" : 
    print(f"你喜歡的食物是{food}")
    food = input("請輸入你喜歡的食物：")
print("再見")
```

ex.3
```
num = int(input("請輸入一個1~10的整數:"))
while num < 1 or num > 10 :
    print(f"你輸入的值{num}是無效的")
    num = int(input("請輸入一個1~10的整數:"))
print(f"你輸入的值是{num}")
```
## For loop
#print 1~10
```
for x in range(1, 11) : 
    print(x)            
```
#print10~1
```
for x in reversed(range(1, 11)) :
    print(x)
```
#print number
```
num = "0123456789"
for x in num :
    if x == "5" :
        #continue    #跳過5
        break        #到5就結束
    else:
        print(x)
```
#dictionary
#key: value
```
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print("key:", key)
    print("value:", value)
```
