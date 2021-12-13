"""Pig Latin, by Al Sweigart al@inventwithpython.com
Translates English messages into Igpay Atinlay.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, word"""

try:
    import pyperclip  # pyperclip은 텍스트를 클립보드에 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면 아무 작업도 하지 않는다.

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    print('''Igpay Atinlay (Pig Latin)
By Al Sweigart al@inventwithpython.com

Enter your message:''')
    pigLatin = englishToPigLatin(input('> '))

    # 모든 단어를 하나의 문자열로 결합한다:
    print(pigLatin)

    try:
        pyperclip.copy(pigLatin)
        print('(Copied pig latin to clipboard.)')
    except NameError:
        pass  # 만약에 pyperclip이 설치되어 있지 않다면 아무 작업도 하지 않는다.


def englishToPigLatin(message):
    pigLatin = ''  # 피그 라틴으로 변환된 문자열
    for word in message.split():
        # 이 단어의 시작 부분에 문자가 아닌 것을 분리한다:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue

        # 이 단어의 끝 부분에 문자가 아닌 것을 분리한다:
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]

        # 단어가 모두 대문자인지, 첫 문자만 대문자인지 기억한다.
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()  # 단어가 소문자로 변환되도록 한다.

        # 이 단어의 시작 부분에 있는 자음을 분리한다:
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        # 단어의 끝에 피그 라틴을 추가한다:
        if prefixConsonants != '':
            word += prefixConsonants + 'ay'
        else:
            word += 'yay'

        # 모두 대문자로 할 건지, 첫 문자만 대문자로 할 건지를 설정한다:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        # 단어의 앞/뒤에 있던 문자가 아닌 것을 추가한다.
        pigLatin += prefixNonLetters + word + suffixNonLetters + ' '
    return pigLatin


if __name__ == '__main__':
    main()
