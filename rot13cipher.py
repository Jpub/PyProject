"""ROT13 Cipher, by Al Sweigart al@inventwithpython.com
The simplest shift cipher for encrypting and decrypting text.
More info at https://en.wikipedia.org/wiki/ROT13
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, cryptography"""

try:
    import pyperclip  # pyperclip은 텍스트를 클립보드로 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면, 아무런 동작도 하지 않는다. 별일 아니다.

# 상수 설정하기:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT13 Cipher, by Al Sweigart al@inventwithpython.com')
print()

while True:  # 메인 프로그램 루프
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break  # 메인 프로그램 루프에서 벗어난다.

    # 메시지의 문자를 13자 이동한다.
    translated = ''
    for character in message:
        if character.isupper():
            # 대문자로 된 문자를 붙인다.
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # 소문자로 된 문자를 붙인다.
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # 번역되지 않은 문자를 붙인다.
            translated += character

    # 암호화된 내용 표시하기:
    print('The translated message is:')
    print(translated)
    print()

    try:
        # 암호화된 내용을 클립보드에 복사하기:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass
