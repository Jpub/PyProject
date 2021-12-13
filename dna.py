"""DNA, by Al Sweigart al@inventwithpython.com
A simple animation of a DNA double-helix. Press Ctrl-C to stop.
Inspired by matoken https://asciinema.org/a/155441
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, scrolling, science"""

import random, sys, time

PAUSE = 0.15  # (!) 이 값을 0.5 또는 0.0으로 바꿔 보자.

# 다음은 DNA 애니메이션의 개별 행이다:
ROWS = [
    #123456789 <- 공백의 수를 알기 위해 사용한다:
    '         ##',  # 인덱스 0은 {}가 없다.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # 인덱스 9는 {}가 없다.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    #123456789 <- 공백의 수를 알기 위해 사용한다:

try:
    print('DNA Animation, by Al Sweigart al@inventwithpython.com')
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    rowIndex = 0

    while True:  # 메인 프로그램 루프
        # 다음 행을 그리기 위해 rowIndex를 증가한다:
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # 행 인덱스 0과 9는 뉴클레오타이드를 갖지 않는다:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # 뉴클레오타이드 쌍(구아닌-시토신 그리고 아데닌-티민)을
        # 무작위로 선택한다:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        # 행을 출력한다.
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)  # 잠시 멈춤을 추가한다.
except KeyboardInterrupt:
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
