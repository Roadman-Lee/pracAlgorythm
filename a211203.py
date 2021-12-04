# # 아이디 규칙에 맞지 않는 아이디를 입력했을때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것
# # 규칙
# # 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# # 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# # 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# import re

# # 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천
# # 신규 유저가 입력한 아이디가 new_id 라고 한다면,
# # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
# #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


# def solution(new_id):
#     answer = ""
#     new_id = new_id.lower()  # 1단계
#     new_id = re.sub("[^a-zA-Z0-9-_.]", "", new_id)  # 2단계
#     new_id = re.sub("[..]+", ".", new_id)  # 3단계
#     new_id = re.sub("^[.]|[.]$]+", "", new_id)  # 4단계
#     if new_id == "":  # 5단계
#         new_id = "a"
#     if len(new_id) >= 16:  # 6단계
#         new_id = new_id[:15]
#     new_id = re.sub("[.]$", "", new_id)
#     while len(new_id) < 3:
#         new_id += new_id[-1]
#     answer = new_id
#     return answer


# print(solution("z-+.....^."))

# def solution(phone_number):
#     answer = ""
#     nums = len(phone_number) - 4
#     answer = (nums * "*") + phone_number[-4:]
#     return answer


import re

# re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)


def solution(new_id):
    new_id = new_id.lower()  # 1단계
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)  # 2단계
    new_id = re.sub("(([.])\\2{1,})", ".", new_id)  # 3단계
    new_id = re.sub("[^\.|\.$]", "", new_id)  # 4단계
    if len(new_id) == 0:
        new_id = "a"  # 5단계
    new_id = re.sub("\.$", "", new_id[:15])  # 6단계
    while len(new_id) < 3:
        new_id += new_id[-1]  # 7단계

    return new_id


print(solution("=.="))
