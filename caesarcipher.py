"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

try:
    import pyperclip  # pyperclip은 텍스트를 클립보드로 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면, 아무런 동작도 하지 않는다. 별일 아니다.

# 암호화/복호화할 수 있는 모든 기호:
# (!) 숫자와 문장 부호도 암호화할 수 있도록
# 여기에 추가해 보자.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# 암호화 또는 복호화할 문자를 사용자가 입력하게 하자:
while True:  # e 또는 d를 입력할 때까지 계속 반복한다.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# 사용할 키를 사용자가 입력하게 하자:
while True:  # 유효한 키를 입력할 때까지 계속 반복한다.
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# 암호화/복호화하려는 메시지를 사용자가 입력하게 하자:
print('Enter the message to {}.'.format(mode))
message = input('> ')

# 카이사르 암호는 대문자에서만 동작한다:
message = message.upper()

# 암호화/복호화된 형태의 메시지를 저장한다:
translated = ''

# 메시지의 각 기호를 암호화/복호화한다:
for symbol in message:
    if symbol in SYMBOLS:
        # 이 기호에 대한 암호화된(또는 복호화된) 숫자를 얻는다.
        num = SYMBOLS.find(symbol)  # 기호의 숫자를 얻는다.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # num이 SYMBOLS의 길이보다 큰지 아니면 0보다 작은지에 따라
        # 랩어라운드(wrap-around) 처리한다:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # 암호화/복호화된 숫자의 기호를 translated에 추가한다:
        translated = translated + SYMBOLS[num]
    else:
        # 암호화/복호화없이 그 기호를 그냥 추가한다:
        translated = translated + symbol

# 암호화/복호화된 문자열을 화면에 표시한다:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass  # pyperclip이 설치되어 있지 않다면 아무 작업도 하지 않는다.
