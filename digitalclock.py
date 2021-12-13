"""Digital Clock, by Al Sweigart al@inventwithpython.com
Displays a digital clock of the current time with a seven-segment
display. Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import sys, time
import sevseg  # sevseg.py 프로그램 임포트하기

try:
    while True:  # 메인 프로그램 루프
        # 몇 개의 새로운 줄을 출력하여 화면을 깨끗하게 정리한다:
        print('\n' * 60)

        # 컴퓨터의 시계로부터 현재 시간을 가져온다:
        currentTime = time.localtime()
        # 24시간이 아닌 12시간을 사용하므로 % 12를 한다:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'  # 12-시간 시계는 00:00이 아닌 12:00이라고 표시한다.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # sevseg 모듈로부터 디지털 문자열을 얻는다:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # 숫자 표시하기:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit.')

        # 초 단위가 변경될 때까지 루프를 계속 돈다:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
