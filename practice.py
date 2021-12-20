def com_up_down():
    max_num = 100
    min_num = 1
    user = int(input("1~100사이의 수를 입력하시오 : "))
    while True:
        com_num = min_num +((max_num-min_num) // 2) 
        print(com_num)
        if com_num == user:
            return print("정답")
        elif com_num > user:
            userAnswer = str(input())
            while userAnswer != "다운":
                print("다시 입력하시오.")
                userAnswer = str(input())
            max_num = com_num 
        else:
            userAnswer = str(input())
            while userAnswer != "업":
                print("다시 입력하시오.")
                userAnswer = str(input())
            min_num = com_num 
            
com_up_down()