"""sPoNgEcAsE, by Al Sweigart al@inventwithpython.com
Translates English messages into sPOnGEcAsE.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, word"""

import random

try:
    import pyperclip  # pyperclip은 텍스트를 클립보드로 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면, 아무런 동작도 하지 않는다. 별일 아니다.


def main():
    """Run the Spongecase program."""
    print('''sPoNgEtExT, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

eNtEr YoUr MeSsAgE:''')
    spongecase = englishToSpongecase(input('> '))
    print()
    print(spongecase)

    try:
        pyperclip.copy(spongecase)
        print('(cOpIed SpOnGeCasE to ClIpbOaRd.)')
    except:
        pass  # pyperclip이 설치되어 있지 않다면, 아무 작업도 하지 않는다.


def englishToSpongecase(message):
    """Return the spongecase form of the given string."""
    spongecase = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongecase += character
            continue

        if useUpper:
            spongecase += character.upper()
        else:
            spongecase += character.lower()

        # 90퍼센트의 확률로 대소문자를 바꾼다.
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # 대소문자를 바꾼다.
    return spongecase


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다
:
if __name__ == '__main__':
    main()
