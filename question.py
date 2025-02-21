import random
import time

memo = dict()

def fibonacci_recursion(n) -> int:
    """
    피보나치 수 계산함수 (재귀함수 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)


def fibonacci_loop(n) -> int:
    """
    피보나치 수 계산함수 (반복문 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]


def fibonacci_memo(n) -> int:
    if n in memo:  # 딕셔너리에 이미 계산된 결과가 있으면 그 값을 리턴
        return memo[n]
    elif n <= 1:  # 0이나 1이 오면 그 값을 바로 리턴
        return n
    else:
        memo[n] = fibonacci_memo(n-2) + fibonacci_memo(n-1)  # 딕셔너리에 계산된 결과 값이 없을 경우 딕셔너리에 추가
        return memo[n]


# n = int(input())
# print(fibonacci_loop(n))
# print(fibonacci_recursion(n))
# print(fibonacci_memo(n))


# 3가지 형식의 피보나치 함수 코드 시간재기
print("# loop")
st = time.time()
for i in range(1000000):
    fibonacci_loop(10)
et = time.time()
print(f"duration: {et - st}")

print("# memo")
st = time.time()
for i in range(1000000):
    fibonacci_memo(10)
et = time.time()
print(f"duration: {et - st}")



# 왜 재귀함수코드는 실행이 이상하게 나올까?
print("# recu")
st = time.time()
for i in range(1000000):
    fibonacci_recursion(10)
et = time.time()
print(f"duration: {et - st}")
print("%.5f" % (et-st))