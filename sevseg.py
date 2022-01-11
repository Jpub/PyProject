"""Sevseg, by Al Sweigart al@inventwithpython.com
A seven-segment number display module, used by the Countdown and Digital
Clock programs.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, module"""

"""A부터 G까지 레이블이 지정되어 있는 7 세그먼트 디스플레이:
 __A__
|     |    Each digit in a seven-segment display:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""


def getSevSegStr(number, minWidth=0):
    """숫자에 대한 7 세그먼트 디스플레이 문자열을 반환한다.
    반환된 문자열이 minWidth보다 작으면 0으로 채워진다."""

    # int 또는 float인 경우, 숫자를 문자열로 변환한다:
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':  # 소수점을 렌더링한다.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # 숫자 사이를 공백으로 간격을 준다.
        elif numeral == '-':  # 음수 기호를 렌더링한다:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # 0을 렌더링한다.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # 1을 렌더링한다.
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # 2를 렌더링한다.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # 3을 렌더링한다.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # 4를 렌더링한다.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # 5를 렌더링한다.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # 6을 렌더링한다.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # 7을 렌더링한다.
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # 8을 렌더링한다.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # 9를 렌더링한다.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # 이것이 마지막 숫자가 아니고 다음에 소수점도 없다면,
        # 숫자 사이의 간격을 위해 공백을 추가한다:
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)


# 이 프로그램이 임포트된 게 아니라면, 0에서 99 사이의 숫자를 표시한다.
if __name__ == '__main__':
    print('This module is meant to be imported rather than run.')
    print('For example, this code:')
    print('    import sevseg')
    print('    myNumber = sevseg.getSevSegStr(42, 3)')
    print('    print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
