"""Digital Stream, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's visuals.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic, beginner, scrolling"""

import random, shutil, sys, time

# 상수 설정하기:
MIN_STREAM_LENGTH = 6  # (!) 이 값을 1 또는 50으로 바꿔 보자.
MAX_STREAM_LENGTH = 14  # (!) 이 값을 100으로 바꿔 보자.
PAUSE = 0.1  # (!) 이 값을 0.0 또는 2.0으로 바꿔 보자.
STREAM_CHARS = ['0', '1']  # (!) 이 문자를 다른 문자로 바꿔 보자.

# 밀더의 범위는 0.0에서 1.0까지다.:
DENSITY = 0.02  # (!) 이 값을 0.10 또는 0.30으로 바꿔 보자.

# 터미널 창의 크기를 구한다:
WIDTH = shutil.get_terminal_size()[0]
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다:
WIDTH -= 1

print('Digital Stream, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # 각 열에 대해 카운터가 0이면 스트림을 더 이상 표시하지 않는다.
    # 0이 아니라면, 그 값은 해당 열에 1 또는 0이 얼마나 표시되어야 하는지를 가리키는
    # 카운터 역할을 하게 된다.
    columns = [0] * WIDTH
    while True:
        # 각 열에 대한 카운터를 설정한다:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # 이 열의 스트림을 다시 시작한다.
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)

            # 빈 공백 또는 1이나 0 문자를 출력한다.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()  # 열의 마지막 행에 줄바꿈을 출력한다.
        sys.stdout.flush()  # 텍스트가 화면에 나타나도록 한다.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
