"""Prime Numbers, by Al Sweigart al@inventwithpython.com
Calculates prime numbers, which are numbers that are only evenly
divisible by one and themselves. They are used in a variety of practical
applications.
More info at: https://en.wikipedia.org/wiki/Prime_number
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, math, scrolling"""

import math, sys

def main():
    print('Prime Numbers, by Al Sweigart al@inventwithpython.com')
    print('Prime numbers are numbers that are only evenly divisible by')
    print('one and themselves. They are used in a variety of practical')
    print('applications, but cannot be predicted. They must be')
    print('calculated one at a time.')
    print()
    while True:
        print('Enter a number to start searching for primes from:')
        print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
        response = input('> ')
        if response.isdecimal():
            num = int(response)
            break

    input('Press Ctrl-C at any time to quit. Press Enter to begin...')

    while True:
        # 모든 소수를 출력한다:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
        num = num + 1  # 다음 숫자로 넘어간다.


def isPrime(number):
    """Returns True if number is prime, otherwise returns False."""
    # 특별한 경우에 대한 처리:
    if number < 2:
        return False
    elif number == 2:
        return True

    # 숫자를 2부터 그 수의 제곱근까지의 모든 숫자로
    # 나머지 없이 나눠지는지 확인한다.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
