"""Hex Grid, by Al Sweigart al@inventwithpython.com
Displays a simple tessellation of a hexagon grid.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, artistic"""

# 상수 설정하기:
# (!) 이들 값을 다른 값으로 변경해 보자:
X_REPEAT = 19  # 수평 격자 수
Y_REPEAT = 12  # 수직 격자 수

for y in range(Y_REPEAT):
    # 육각형의 위쪽 절반을 표시한다:
    for x in range(X_REPEAT):
        print(r'/ \_', end='')
    print()

    # 육각형의 아래쪽 절만을 표시한다:
    for x in range(X_REPEAT):
        print(r'\_/ ', end='')
    print()
