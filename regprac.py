def solution(phone_number):
    answer = ""
    nums = len(phone_number) - 4
    answer = (nums * "*") + phone_number[-4:]
    return answer


print(solution("01074564442"))
