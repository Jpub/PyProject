"""Numeral System Counters, by Al Sweigart al@inventwithpython.com
Shows equivalent numbers in decimal, hexadecimal, and binary.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, math"""


print('''Numeral System Counters, by Al Sweigart al@inventwithpython.com

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)
''')

while True:
    response = input('Enter the starting number (e.g. 0) > ')
    if response == '':
        response = '0'  # 디폴트로 0부터 시작한다.
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display (e.g. 1000) > ')
    if response == '':
        response = '1000'  # 디폴트로 1000을 표시한다.
        break
    if response.isdecimal():
        break
    print('Please enter a number.')
amount = int(response)

for number in range(start, start + amount):  # 메인 프로그램 루프
    # 16진수/2진수로 변환하고 접두사를 제거한다:
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC:', number, '   HEX:', hexNumber, '   BIN:', binNumber)
