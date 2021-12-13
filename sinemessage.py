"""Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import math, shutil, sys, time

# 터미널 윈도우의 크기를 구한다:
WIDTH, HEIGHT = shutil.get_terminal_size()
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다:
WIDTH -= 1

print('Sine Message, by Al Sweigart al@inventwithpython.com')
print('(Press Ctrl-C to quit.)')
print()
print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')
while True:
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')


step = 0.0  # 'step'은 우리가 사인파와 얼마나 멀리 떨어져 있을지를 결정한다.
# 사인(Sine)은 -1.0에서 1.0으로 이동하므로, 승수(multiplier)로 그 값을 바꿔야 한다:
multiplier = (WIDTH - len(message)) / 2
try:
    while True:  # 메인 프로그램 루프
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25  # (!) 이 값을 0.1 또는 0.5로 바꿔 보자.
except KeyboardInterrupt:
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
