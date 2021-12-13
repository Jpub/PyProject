"""Simple Substitution Cipher, by Al Sweigart al@inventwithpython.com
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.
More info at: https://en.wikipedia.org/wiki/Substitution_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, cryptography, math"""

import random

try:
    import pyperclip  # pyperclip은 텍스트를 클립보드로 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면, 아무런 동작도 하지 않는다. 별일 아니다.

# 암호화/복호화할 수 있는 가능한 모든 기호:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''Simple Substitution Cipher, by Al Sweigart
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.''')

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
        if myMode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
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

    # 결과를 표시한다:
    print('The %sed message is:' % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  # pyperclip이 설치되어 있지 않다면, 아무 작업도 하지 않는다.


def checkKey(key):
    """Return True if key is valid. Otherwise return False."""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encryptMessage(message, key):
    """Encrypt the message using the key."""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """Decrypt the message using the key."""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """Encrypt or decrypt the message using the key."""
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # 복호화의 경우, 암호화와 동일한 코드를 사용할 수 있다.
        # 사용했던 키와 LETTERS 문자열의 위치만 바꾸면 된다.
        charsA, charsB = charsB, charsA

    # 메시지의 각 기호에 대해 루프를 돈다:
    for symbol in message:
        if symbol.upper() in charsA:
            # 그 기호를 암호화/복호화 한다:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # 그 기호가 LETTERS에 있지 않다면, 변경없이 그냥 추가한다.
            translated += symbol

    return translated


def generateRandomKey():
    """Generate and return a random encryption key."""
    key = list(LETTERS)  # LETTERS 문자열에서 리스트를 가져온다.
    random.shuffle(key)  # 리스트를 무작위로 섞는다.
    return ''.join(key)  # 리스트에서 문자열을 가져 온다.


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
