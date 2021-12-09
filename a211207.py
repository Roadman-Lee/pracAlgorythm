from itertools import combinations

nums = [1, 2, 3, 4]

def isPrime(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


def solution(nums):
    answer = 0
    a = list(combinations(nums, 3))
    for i in a:
        c = sum(i)
        if isPrime(c):
            print(c)
            answer += 1

    return answer


print(solution(nums))
# from itertools import combinations
# from primePy import primes


# def solution(nums):
#     answer = 0
#     a = list(combinations(nums, 3))
#     for i in a:
#         print(i)
#         c = sum(i)
#         if primes.check(c):
#             print(primes.check(c))
#             answer += 1
#     return answer


# solution(nums)
