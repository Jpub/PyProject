"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# 해킹할 메시지를 사용자가 입력하게 하자:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# 암호화/복호화할 수 있는 가능한 모든 기호:
# (이것은 메시지를 암호화할 때 사용했던 SYMBOLS와 일치해야 한다.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):  # 모든 키에 대해 루프를 돈다.
    translated = ''

    # 메시지의 각 기호를 복호화한다:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # 기호의 숫잣값을 구한다.
            num = num - key  # 숫자만큼 복호화한다.

            # 만약에 숫자가 0보다 작으면 랩어라운드(wrap-around) 처리한다:
            if num < 0:
                num = num + len(SYMBOLS)

            # 복호화된 숫자의 기호를 translated에 더한다:
            translated = translated + SYMBOLS[num]
        else:
            # 복호화 없이 그 기호를 그냥 더한다:
            translated = translated + symbol

    # 테스트된 키와 함께 복호화된 텍스트를 표시한다:
    print('Key #{}: {}'.format(key, translated))
