"""Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, scrolling, artistic"""


import random, sys, time

# 상수 설정하기:
WIDTH = 70  # (!) 이 값을 10 또는 30으로 변경해 보자.
PAUSE_AMOUNT = 0.05  # (!) 이 값을 0 또는 1.0으로 변경해보자.

print('Deep Cave, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # 터널 세그먼트 출력하기:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    # 잠깐 멈췄을 때 Ctrl-C를 눌렀는지 확인한다:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C가 눌렸다면 프로그램을 종료한다.

    # 왼쪽 폭을 조절한다:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1  # 왼쪽 폭이 줄어들었다.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1  # 왼쪽 폭이 늘어났다.
    else:
        pass  # 아무것도 하지 않는다. 왼쪽 폭의 변화가 없다.

    # 공백의 폭을 조절한다:
    # (!) 다음 코드 전부를 주석 해제해 보자:
    #diceRoll = random.randint(1, 6)
    #if diceRoll == 1 and gapWidth > 1:
    #    gapWidth = gapWidth - 1  # 공백의 폭이 줄어들었다.
    #elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
    #    gapWidth = gapWidth + 1  # 공백의 폭이 늘어났다.
    #else:
    #    pass  # 아무것도 하지 않는다. 공백의 폭은 변하지 않았다.
