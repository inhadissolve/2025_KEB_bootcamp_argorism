# guess number 예제
# 이 문제를 자동화하고 로그파일을 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록 한다.
# with open('guess.txt', 'w') as fp
# fp.write()

import random


def getnext(low, high):
    return (low + high) // 2


if __name__ == "__main__":
    low = 1
    high = 100
    chance = 7
    answer = random.randint(low, high)
    with open('guess.txt', 'w') as fp:
        while chance != 0:
            guess = getnext(low, high)
            if guess == answer:
                print(f'You win. Answer is {answer}')
                fp.write(f'You win. Answer is {answer}\n')
                break
            elif guess > answer:
                chance = chance - 1
                print(f'{guess} is bigger than answer. Chance left : {chance}')
                fp.write(f'{guess} is bigger than answer. Chance left : {chance}\n')
                high = guess
                guess = getnext(low, high)
            else:
                chance = chance - 1
                print(f'{guess} is lower than answer. Chance left : {chance}')
                fp.write(f'{guess} is lower than answer. Chance left : {chance}\n')
                low = guess
                guess = getnext(low, high)
        else:
            print(f'You lost. Answer is {answer}')