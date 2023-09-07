#字串索引
abc = "123-456-789"
first_char = abc[0]
first_three = abc[0:3]    #1~3字元
last_one = abc[-1]        #最後一個字元
last_two = abc[-2]
print(first_char)
print(first_three)
print(last_one)

#email字串分析
email = "eugene2165@gmail.com"
index = email.index("@")
print(email[:index])        #eugene2165
print(email[index+1:])      #gmail.com

#f-string字串格式化
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
print(f"price1:{price1:^10.2f}\n"
      f"price2:{price2:^10.2f}\n"
      f"price3:{price3:^10.2f}\n")    #空格為10位並置中對齊

#混用不同符號
print(f"price1:{price1:<+.2f}\n"
      f"price2:{price2:<+.2f}\n"
      f"price3:{price3:<+.2f}\n")     #靠左對齊、要加正負號、小數點到第二位