"""Shining Carpet, by Al Sweigart al@inventwithpython.com
Displays a tessellation of the carpet pattern from The Shining.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, artistic"""

# 상수 설정하기:
X_REPEAT = 6  # 수평으로 반복할 횟수
Y_REPEAT = 4  # 수직으로 반복할 횟수

for i in range(Y_REPEAT):
    print(r'_ \ \ \_/ __' * X_REPEAT)
    print(r' \ \ \___/ _' * X_REPEAT)
    print(r'\ \ \_____/ ' * X_REPEAT)
    print(r'/ / / ___ \_' * X_REPEAT)
    print(r'_/ / / _ \__' * X_REPEAT)
    print(r'__/ / / \___' * X_REPEAT)
