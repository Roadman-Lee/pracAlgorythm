# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# 실행 예
# p t
letters = 'python'
print(letters[0],letters[2])
# 정답 확인
# lang = 'python'
# print(lang[0], lang[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210
license_plate = "24가 2210"
print(license_plate[4:])
# 정답 확인
# license_plate = "24가 2210"
# print(license_plate[-4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀
string = "홀짝홀짝홀짝"
print(string.replace('짝',''))
# 정답 확인
# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.
# string = "홀짝홀짝홀짝"
# print(string[::2])

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
# 실행 예:
# NOHTYP
string2 = "PYTHON"
# print(string2[::-1])
변수=reversed(string2)
print(변수)
print(''.join(변수))
# 정답 확인
# string = "PYTHON"
# print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))
# # 정답 확인
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-", " ")
# print(phone_number1)

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예
# 01011112222
print(phone_number.replace('-',''))

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예:
# kr
url = "http://sharebook.kr"
print(url[-2:])
# 정답 확인
# url = "http://sharebook.kr"
# url_split = url.split('.')
# print(url_split[-1])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
# lang = 'python'
# lang[0] = 'P'
# print(lang)
#정답확인
# 문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A
string3 = 'abcdfe2a354a32a'
print(string3.replace('a','A'))
# 정답 확인
# string = 'abcdfe2a354a32a'
# string = string.replace('a', 'A')
# print(string)

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
string = 'abcd'
string.replace('b', 'B')
print(string) # aBcd 
# 정답 확인
# abcd가 그대로 출력됩니다. 
# 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. 
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.

#알고리듬
a = int(input())  # 횟수
b = []  # 백업
for i in range(a):
    s = int(input())  # 선택
    if s == 0:
        if len(b) < 10:
            n = int(input())  # 입력
            b.append(n)
        else:
            print('overflow')
    elif s == 1:
        if len(b) > 0:
            b.pop(-1)
        else:
            print('underflow')
    else:
        break
for j in b:
    print(j, end=' ')