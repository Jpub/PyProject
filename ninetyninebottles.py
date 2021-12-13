"""Ninety-Nine Bottles of Milk on the Wall
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! Press
Ctrl-C to stop.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, scrolling"""

import sys, time

print('Ninety-Nine Bottles, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  # 이것은 시작하는 병의 수다.
PAUSE = 2  # (!) 전체 가사를 한 번에 보려면 이 값을 0으로 변경하자.

try:
    while bottles > 1:  # 계속 반복하여 가사를 표시한다.
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)  # PAUSE 수(초)만큼 일시 정지한다.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1  # 병의 수를 하나씩 줄인다.
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()  # 줄바꿈을 출력한다.

    # 마지막 절 가사를 표시한다:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
