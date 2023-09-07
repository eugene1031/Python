#print1~10
for x in range(1, 11) : 
    print(x)    

#print10~1
for x in reversed(range(1, 11)) :
    print(x)

#print number
num = "0123456789"
for x in num :
    if x == "5" :
        #continue    #跳過5
        break        #到5就結束
    else:
        print(x)

#dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print("key:", key)
    print("value:", value)    