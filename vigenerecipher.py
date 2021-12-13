"""Vigenère Cipher, by Al Sweigart al@inventwithpython.com
The Vigenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.
More info at: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, cryptography, math"""

try:
    import pyperclip  # pyperclip은 텍스트를 클립보드로 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면, 아무런 동작도 하지 않는다. 별일 아니다.

# 암호화/복호화가 가능한 모든 기호:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''Vigenère Cipher, by Al Sweigart al@inventwithpython.com
The Viegenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.''')

    # 사용자가 암호화 또는 복호화 여부를 지정하도록 한다:
    while True:  # 사용자가 e 또는 d를 입력할 때까지 계속 요구한다.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # 사용자가 사용할 키를 지정하도록 한다:
    while True:  # 사용자가 유효한 키를 입력할 때까지 계속 요구한다.
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break

    # 사용자가 암호화/복호화할 메시지를 지정하도록 한다:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # 암호화/복호화를 수행한다:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)

    print('%sed message:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  # pyperclip이 설치되어 있지 않다면, 아무 작업도 하지 않는다.


def encryptMessage(message, key):
    """Encrypt the message using the key."""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """Decrypt the message using the key."""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """Encrypt or decrypt the message using the key."""
    translated = []  # 암호화/복호화된 메시지 문자열을 저장한다.

    keyIndex = 0
    key = key.upper()

    for symbol in message:  # 메시지의 각 문자에 대해 루프를 돈다.
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1은 symbol.upper()가 LETTERS에 없다는 의미다.
            if mode == 'encrypt':
                # 암호화하는 경우라면 더한다:
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                # 복호화하는 경우라면 뺀다:
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)  # 잠재적인 랩-어라운드(wrap-around)를 처리한다.

            # 암호화된/복호화된 기호를 translated에 추가한다.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1  # 키의 다음 문자로 이동한다.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # 암호화/복호화 없이 그 기호를 그냥 추가한다:
            translated.append(symbol)

    return ''.join(translated)


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
