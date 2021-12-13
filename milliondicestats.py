"""Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
A simulation of one million dice rolls.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, math, simulation"""

import random, time

print('''Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com

Enter how many six-sided dice you want to roll:''')
numberOfDice = int(input('> '))

# 주사위를 굴린 결과를 저장하기 위한 딕셔너리를 설정한다:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# 주사위 굴림을 시뮬레이션하기:
print('Simulating 1,000,000 rolls of {} dice...'.format(numberOfDice))
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print('{}% done...'.format(round(i / 10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# 결과 표시하기:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print('  {} - {} rolls - {}%'.format(i, roll, percentage))
