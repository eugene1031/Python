#驗證使用者輸入的合法性
user_name = input("請輸入使用者名稱（須小於12位元、不能包含空格、不能包含數字）")
length = len(user_name)

if length > 12 :
    print("使用者名稱不得超過12位元！")
elif " " in user_name :
    print("使用者名稱不得包含空格！")
elif not user_name.isalpha() :
    print("使用者名稱不得包含數字！")
else :
    print(f"歡迎{user_name}") 