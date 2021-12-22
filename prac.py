import random

def turn():
    turn = random.randint(0, 1)
    return turn


def enter():
    user = int(input(""))
    i = [1,2,3]
    while user in i:
        return user
    else:
        print("다시 입력하세요")
        enter()
        
    
def ply_turn(lst, enter):
    try:
        for i in range(enter):
            print(lst.pop())
    except IndexError:
        print("test")
        
    # if enter == 1:
    #     print(lst.pop())

    # elif enter == 2:
    #     print(lst.pop())
    #     print(lst.pop())
            
    # elif enter == 3:
    #     print(lst.pop())
    #     print(lst.pop())
    #     print(lst.pop())
    
  
def com_turn(lst):
    com_answer = random.randint(1, 3)
    if com_answer == 1:
        print(lst.pop())
        
    elif com_answer == 2:
        print(lst.pop())
        print(lst.pop())
            
    elif com_answer == 3:
        print(lst.pop())
        print(lst.pop())
        print(lst.pop())


def sequence():
    lst = (list(range(1,32)))
    lst.reverse()
    # print(type(lst))
    turned = turn()
    for count in range(len(lst)):
        while turned == 1:
            print("당신의 순서입니다.")
            answer = enter()
            if answer > len(lst):
                return print("test")    
            ply_turn(lst, answer)
            com_turn(lst)
        

        else:
            print("당신의 순서입니다.") 
            com_turn(lst)
            answer = enter()
            ply_turn(lst, answer)
        
sequence()

