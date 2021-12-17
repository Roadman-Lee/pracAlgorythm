warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("회사 이름: ")
for i in range(len(warn_investment_list)):
    if warn_investment_list[i] == user:
        print("투자 경고 종목이 아닙니다")
        break
    print("투자 경고 종목입니다")
    break    