"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short"""

import datetime

# 상수 설정:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True:  # 사용자가 년도를 입력하도록 루프를 돈다.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True:  # 사용자가 달을 입력하도록 루프를 돈다.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def getCalendarFor(year, month):
    calText = ''  # calText는 생성할 달력에 대한 문자열을 담게 될 것이다.

    # 달력 상단에 년도와 달을 표시한다:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # 달력에 요일을 추가한다:
    # (!) 요일을 약자(SUN, MON, TUE 등)로 바꿔 보자:
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # 주를 구분하는 수평선 문자열:
    weekSeparator = ('+----------' * 7) + '+\n'

    # 일을 구분하는 | 사이의 공백은 10칸이다:
    blankRow = ('|          ' * 7) + '|\n'

    # 해당 월의 첫 날을 구한다. (The datetime module handles all
    # (datetime 모듈은 여기서 달력에 필요한 모든 복잡한 일을 처리해 준다.)
    currentDate = datetime.date(year, month, 1)

    # 일요일인 날짜가 될 때까지 currentDate를 하루씩 이전 날짜로 옮긴다.
    # (weekday()는 일요일에 대한 값으로 0이 아닌 6을 반환한다.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # 그 달의 각 주를 반복한다.
        calText += weekSeparator

        # dayNumberRow는 날짜 레이블을 가지고 있는 행이다:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # 다음 날로 이동.
        dayNumberRow += '|\n'  # 토요일 다음에 수직선을 추가한다.

        # 날짜 행과 세 줄의 빈 행을 추가한다.
        calText += dayNumberRow
        for i in range(3):  # (!) 5 또는 10으로 변경해 보자.
            calText += blankRow

        # 그 달에 대한 작업이 끝났는지 확인한다:
        if currentDate.month != month:
            break

    # 달력 맨 하단에 수평선을 추가한다.
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # 달력을 표시한다.

# 달력을 텍스트 파일로 저장한다:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)
