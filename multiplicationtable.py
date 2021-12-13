"""Multiplication Table, by Al Sweigart al@inventwithpython.com
Print a multiplication table.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, math"""

print('Multiplication Table, by Al Sweigart al@inventwithpython.com')

# 숫자 레이블 가로로 출력하기:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

# 각 행 표시하기:
for number1 in range(0, 13):

    # 숫자 레이블 세로로 출력하기:
    print(str(number1).rjust(2), end='')

    # 구분자 출력하기:
    print('|', end='')

    for number2 in range(0, 13):
        # 결과 다음에 공백을 넣어 출력한다:
        print(str(number1 * number2).rjust(3), end=' ')

    print()  # 줄바꿈을 출력하여 행을 마무리한다.
