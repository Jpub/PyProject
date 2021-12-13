r"""Diamonds, by Al Sweigart al@inventwithpython.com
Draws diamonds of various sizes.
View this code at https://nostarch.com/big-book-small-python-projects
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
Tags: tiny, beginner, artistic"""

def main():
    print('Diamonds, by Al Sweigart al@inventwithpython.com')

    # 크기가 0에서 6까지인 다이아몬드를 표시한다:
    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()  # 새로운 줄을 출력한다.
        displayFilledDiamond(diamondSize)
        print()  # 새로운 줄을 출력한다.


def displayOutlineDiamond(size):
    # 다이아몬드의 위쪽 절반을 표시한다:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # 왼쪽 공백
        print('/', end='')  # 다이아몬드의 왼쪽 면
        print(' ' * (i * 2), end='')  # 다이아몬드의 내부
        print('\\')  # 다이아몬드의 오른쪽 면

    # 다이아몬드의 아래쪽 절반을 표시한다:
    for i in range(size):
        print(' ' * i, end='')  # 왼쪽 공백
        print('\\', end='')  # 다이아몬드의 왼쪽 면
        print(' ' * ((size - i - 1) * 2), end='')  # 다이아몬드의 내부
        print('/')  # 다이아몬드의 오른쪽 면


def displayFilledDiamond(size):
    # 다이아몬드의 위쪽 절반을 표시한다:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # 왼쪽 공백
        print('/' * (i + 1), end='')  # 다이아몬드의 왼쪽 절반
        print('\\' * (i + 1))  # 다이아몬드의 오른쪽 절반

    # 다이아몬드의 아래쪽 절반을 표시한다:
    for i in range(size):
        print(' ' * i, end='')  # 왼쪽 공백
        print('\\' * (size - i), end='')  # 다이아몬드의 왼쪽 절반
        print('/' * (size - i))  # 다이아몬드의 오른쪽 절반


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
