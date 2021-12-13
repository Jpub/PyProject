"""Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com
A water pouring puzzle.
More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, math, puzzle"""

import sys


print('Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com')

GOAL = 4  # 문제를 풀기 위해 물통에 있어야 할 정확한 물의 양
steps = 0  # 문제를 풀기 위해 플레이어가 몇 번을 수행했는지 추적한다.

# 각 물통에 있는 물의 양:
waterInBucket = {'8': 0, '5': 0, '3': 0}

while True:  # 메인 게임 루프
    # 버킷의 현재 상태를 표시한다:
    print()
    print('Try to get ' + str(GOAL) + 'L of water into one of these')
    print('buckets:')

    waterDisplay = []  # 물 또는 빈 공간에 대한 문자열을 담는다.

    # 8리터 물통을 위한 문자열을 얻는다:
    for i in range(1, 9):
        if waterInBucket['8'] < i:
            waterDisplay.append('      ')  # 빈 공간을 추가한다.
        else:
            waterDisplay.append('WWWWWW')  # 물을 추가한다.

    # 5리터 물통을 위한 문자열을 얻는다:
    for i in range(1, 6):
        if waterInBucket['5'] < i:
            waterDisplay.append('      ')  # 빈 공간을 추가한다.
        else:
            waterDisplay.append('WWWWWW')  # 물을 추가한다.

    # 3리터 물통을 위한 문자열을 얻는다:
    for i in range(1, 4):
        if waterInBucket['3'] < i:
            waterDisplay.append('      ')  # 빈 공간을 추가한다.
        else:
            waterDisplay.append('WWWWWW')  # 물을 추가한다.

    # 각 물통의 물의 양과 함께 물통을 표시한다:
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*waterDisplay))

    # 물통에 목표한 물의 양이 있는지 확인한다:
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print('Good job! You solved it in', steps, 'steps!')
            sys.exit()

    # 플레이어가 물통으로 수행할 작업을 선택하게 한다:
    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    while True:  # 플레이어가 유효한 동작을 입력할 때까지 계속 요청한다.
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in ('F', 'E', 'P'):
            break  # 플레이어가 유효한 동작을 선택했다.
        print('Enter F, E, P, or Q')

    # 플레이어가 물통을 선택하게 한다:
    while True:  # 유효한 물통을 입력할 때까지 계속 요청한다.
        print('Select a bucket 8, 5, 3, or QUIT:')
        srcBucket = input('> ').upper()

        if srcBucket == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if srcBucket in ('8', '5', '3'):
            break  # 플레이어가 유효한 물통을 선택했다.

    # 선택한 동작을 수행한다:
    if move == 'F':
        # 물의 양을 최대로 설정한다.
        srcBucketSize = int(srcBucket)
        waterInBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'E':
        waterInBucket[srcBucket] = 0  # 물의 양을 없앤다.
        steps += 1

    elif move == 'P':
        # 플레이어가 물을 부을 물통을 선택하게 한다:
        while True:  # 유효한 물통을 입력할 때까지 계속 요청한다.
            print('Select a bucket to pour into: 8, 5, or 3')
            dstBucket = input('> ').upper()
            if dstBucket in ('8', '5', '3'):
                break  # 플레이어가 유효한 물통을 선택했다.

        # 붓는 양을 계산한다:
        dstBucketSize = int(dstBucket)
        emptySpaceInDstBucket = dstBucketSize - waterInBucket[dstBucket]
        waterInSrcBucket = waterInBucket[srcBucket]
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)

        # 이 물통에서 물을 따른다:
        waterInBucket[srcBucket] -= amountToPour

        # 다른 물통에 물을 붓는다:
        waterInBucket[dstBucket] += amountToPour
        steps += 1

    elif move == 'C':
        pass  # 플레이어가 최소를 선택하면 아무런 작업을 하지 않는다.
