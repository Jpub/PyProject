"""niNety-nniinE BoOttels of Mlik On teh waLl
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! The song
gets sillier and sillier with each verse. Press Ctrl-C to stop.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, scrolling, word"""

import random, sys, time

# 상수 설정하기:
# (!) 한 번에 모든 가사를 출력하려면 이들 값 모두를 0으로 변경하자.
SPEED = 0.01  # 글자를 출력하는 사이에 일시 중지한다.
LINE_PAUSE = 1.5  # 각 줄의 끝에 일시 중지한다.


def slowPrint(text, pauseAmount=0.1):
    """텍스트의 문자를 한 번에 하나씩 천천히 출력한다."""
    for character in text:
        # 텍스트가 즉시 출력되도록 여기서 flush=True로 설정한다:
        print(character, flush=True, end='')  # end=''는 개행이 없다는 의미다.
        time.sleep(pauseAmount)  # 각 문자 사이에 일시 중지한다.
    print()  # 줄바꿈을 출력한다.


print('niNety-nniinE BoOttels, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  # 이것은 시작하는 병의 숫자다.

# 이 리스트는 가사에 사용되는 문자열이 있다:
lines = [' bottles of milk on the wall,',
         ' bottles of milk,',
         'Take one down, pass it around,',
         ' bottles of milk on the wall!']

try:
    while bottles > 0:  # 계속 반복하면서 가사를 표시한다.
        slowPrint(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles - 1  # 병의 숫자를 하나 줄인다.

        if bottles > 0:  # 현재 가사의 마지막 줄을 출력한다.
            slowPrint(str(bottles) + lines[3], SPEED)
        else:  # 전체 노래의 마지막 줄을 출력한다.
            slowPrint('No more bottles of milk on the wall!', SPEED)

        time.sleep(LINE_PAUSE)
        print()  # 줄바꿈을 출력한다.

        # 가사를 '더 이상하게' 만들기 위해 무작위 라인을 선택한다:
        lineNum = random.randint(0, 3)

        # 편집할 수 있도록 리스트로 만든다.
        # (파이썬의 문자열은 불변적이다.)
        line = list(lines[lineNum])

        effect = random.randint(0, 3)
        if effect == 0:  # 문자를 공백으로 바꾼다.
            charIndex = random.randint(0, len(line) - 1)
            line[charIndex] = ' '
        elif effect == 1:  # 문자의 대소문자를 변경한다.
            charIndex = random.randint(0, len(line) - 1)
            if line[charIndex].isupper():
                line[charIndex] = line[charIndex].lower()
            elif line[charIndex].islower():
                line[charIndex] = line[charIndex].upper()
        elif effect == 2:  # 두 문자를 서로 바꾼다.
            charIndex = random.randint(0, len(line) - 2)
            firstChar = line[charIndex]
            secondChar = line[charIndex + 1]
            line[charIndex] = secondChar
            line[charIndex + 1] = firstChar
        elif effect == 3:  # 문자를 두 번 쓴다.
            charIndex = random.randint(0, len(line) - 2)
            line.insert(charIndex, line[charIndex])

        # 리스트를 다시 문자열로 변환하고 줄에 넣는다:
        lines[lineNum] = ''.join(line)
except KeyboardInterrupt:
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
