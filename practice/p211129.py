# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
# >> a = "3"
# >> b = "4"
# >> print(a + b)
a = "3"
b = "4"
print(a + b) # 34 : a, b가 문자열이기 때문에

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
# >> print("Hi" * 3)
print("Hi" * 3) # HiHiHi 

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
print("-" * 80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예:
# python java python java python java python java
t1 = 'python'
t2 = 'java'
print((t1, t2) * 3)  # 오답
# 정답 확인
# t1 = "python"
# t2 = "java"
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# 정답 확인
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
# 정답 확인
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 정답 확인
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
상장주식수 = "5,969,782,550"
a = 상장주식수.replace(",","")
b = int(a)
print(b, type(b))
# 정답 확인
# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",", "")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# 정답확인
# 문자열에서 슬라이싱을 사용하면 여러 글자를 접근할 수 있습니다.
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# data = "   삼성전자    "
data = "   삼성전자    "
print(data.strip(" "))
# 정답확인
# 문자열에서 strip( ) 메서드를 사용하면 좌우의 공백을 제거할 수 있습니다. 
# 이때 원본 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환됩니다.
# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)