#次方
a = 2
a **= 3
print(a)

# 最大值最小值
x = 1
y = 2
z = 3
print(max(x,y,z))
print(min(x,y,z))

# 四捨五入
a = 5.556
print(round(a))
print(round(a,2))    #到小數點第二位

## 無條件進位、無條件捨去
import math

x = 9.5
print(math.ceil(x))     #無條件進位 = 10
print(math.floor(x))    #無條件捨去 = 9