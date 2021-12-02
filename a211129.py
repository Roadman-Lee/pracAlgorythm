# Queue
# FIFO (First in First Out) 
# EnQueue, DeQueue 를 통해 자료 입출력 구현
# 큐가 꽉 차서 더 이상 자료를 넣을 수 없을때 Overflow,
# 큐가 비어 있어 자료를 꺼낼 수 없는 경우 Underflow 라고한다.

# 큐는 최대 10개 자료가 들어갈 수 있고, 10개를 넘으면 Overflow 출력.
# 큐가 비어있는 상태에서 Dequeue을 실행하면 underflow를 출력.
# 프로그래밍 언어에서 제공하는 라이브러리 사용 x

# 첫 줄에 입출력 횟수를 입력.
# 다음 줄부터 입력 또는 출력 여부 (d 또는 D)를 입력하고 입력(e 또는 E)일 경우는 자료 내용까지 입력
# e(E) 또는 d(D) 이외의 입력이 들어올 경우 큐의 최종 상태를 출력하여 프로그램 종료
# 입출력 횟수가 끝나거나 프로그램이 중간에 종료되면 큐의 최종 상태를 출력

a = input()
lst = []

for i in range(int(a)):
    s = input()
    
    if s == 'e' or 'E':
        if len(lst) < 10:
            d = input()
            lst.append(d)
            print(lst)
        else:
            print("overflow")
    
    if s == 'd' or 'D':
        if len(lst) == 0:
            print("underflow")
        else:
            lst.pop()

            
        
