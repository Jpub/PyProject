"""Leetspeak, by Al Sweigart al@inventwithpython.com
Translates English messages into l33t5p34]<.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, word"""

import random

try:
    import pyperclip  # pyperclip은 텍스트를 클릭보드에 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면 아무 것도 하지 않는다. 큰 일은 아니다.


def main():
    print('''L3375P34]< (leetspeek)
By Al Sweigart al@inventwithpython.com

Enter your leet message:''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        # pyperclip이 임포트되지 않았다면,
        # pyperclip을 사용하려고 할 때 NameError 예외가 발생할 것이다:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass  # 만약에 pyperclip이 설치되어 있지 않다면 아무것도 하지 않는다.


def englishToLeetspeak(message):
    """Convert the English string in message and return leetspeak."""
    # `charMapping`의 모든 키를 소문자로 한다.
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leetspeak = ''
    for char in message:  # 각 문자를 확인한다:
        # 문자를 리트 스피크로 변환할 확률은 70퍼센트다.
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # 이 문자는 변환하지 않는다:
            leetspeak = leetspeak + char
    return leetspeak


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
