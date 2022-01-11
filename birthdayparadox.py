"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """생일에 대한 임의의 날짜 객체들의 리스트를 반환한다."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # 여기서 년도는 중요하지 않기 때문에
        # 모든 생일을 같은 년도로 한다.
        startOfYear = datetime.date(2001, 1, 1)

        # 그 년도에서 임의의 날짜를 얻는다:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """생일 리스트에서 중복되는 생일 날짜인 
    객체를 반환한다."""
    if len(birthdays) == len(set(birthdays)):
        return None  # 모든 생일이 서로 다르다면 None을 반환한다.

    # 모든 생일을 각각 다른 생일과 비교한다:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # 일치하는 생일을 반환한다.


# 인트로 출력:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# 월 이름이 순서대로있는 튜플을 만든다:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # 사용자가 유효한 값을 입력할 때까지 계속 묻는다.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # 사용자가 유효한 값을 입력
print()

# 생일을 생성하고 출력하기:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # 첫 번째 생일 이후부터 각 생일마다 콤마를 표시한다.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# 두 생일이 서로 일치하는지 판단한다.
match = getMatch(birthdays)

# 결과 출력하기:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# 100,000번의 시뮬레이션 실행하기:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0  # 생일이 일치하는 시뮬레이션 수
for i in range(100_000):
    # 10,000번의 시뮬레이션마다 진행 상황 출력하기:
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# 시뮬레이션 결과 출력하기:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
