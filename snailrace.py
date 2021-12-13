"""Snail Race, by Al Sweigart al@inventwithpython.com
Fast-paced snail racing action!
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, beginner, game, multiplayer"""

import random, time, sys

# 상수 설정하기:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40  # (!) 이 숫자를 변경해 보자.

print('''Snail Race, by Al Sweigart al@inventwithpython.com

    @v <-- snail

''')

# 몇 마리의 달팽이가 경주를 하는지 묻는다:
while True:  # 플레이어가 숫자를 입력할 때까지 계속 요청한다.
    print('How many snails will race? Max:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)

# 각 달팽이에 이름을 입력한다:
snailNames = []  # 달팽이 이름 문자열의 리스트
for i in range(1, numSnailsRacing + 1):
    while True:  # 플레이어가 유효한 이름을 입력할 때까지 계속 요청한다.
        print('Enter snail #' + str(i) + "'s name:")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break  # 입력된 이름이 유효하다.
    snailNames.append(name)

# 출발선에 각 달팽이를 표시한다.
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)  # 경주 시작 직전에 일시 중지한다.

while True:  # 메인 프로그램 루프
    # 전진할 달팽이를 무작위로 고른다:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        # 달팽이가 결승선에 도착했는지 확인한다:
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    # (!) 실험: 만약에 달팽이 이름들 중에 여러분의 이름이 있다면,
    # 그 달팽이의 진행 상황을 증가시키는 치트를 여기에 추가하자.

    time.sleep(0.5)  # (!) 실험: 이 값을 바꿔 보자.

    # (!) 실험: 이 코드를 주석 처리하면 어떻게 되나?
    print('\n' * 40)

    # 출발선과 결승선 표시하기:
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # 이름 태그가 있는 달팽이를 표시한다:
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')
