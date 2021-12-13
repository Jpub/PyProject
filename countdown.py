"""Countdown, by Al Sweigart al@inventwithpython.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import sys, time
import sevseg  # 우리의 sevseg.py 프로그램을 임포트한다.

# (!) 초를 다른 숫자로 변경하자:
secondsLeft = 30

try:
    while True:  # 메인 프로그램 루프
        # 여러 개의 개행 문자를 출력하여 화면을 깨끗하게 정리한다:
        print('\n' * 60)

        # secondsLeft의 값으로부터 시/분/초를 얻는다:
        # 예를 들어, 7265는 2시간, 1분, 5초다.
        # 즉, 7265 // 3600는 2시간이다:
        hours = str(secondsLeft // 3600)
        # 그리고 7265 % 3600은 65이며, 65 // 60은 1분이다:
        minutes = str((secondsLeft % 3600) // 60)
        # 그리고 7265 % 60은 5초다:
        seconds = str(secondsLeft % 60)

        # sevseg 모듈로부터 디지털 문자열을 얻는다:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # 디지털 문자열을 표시한다:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # 1초 일시 정지를 추가한다.
        secondsLeft -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
