"""Lucky Stars, by Al Sweigart al@inventwithpython.com
A "press your luck" game where you roll dice to gather as many stars
as possible. You can roll as many times as you want, but if you roll
three skulls you lose all your stars.

Inspired by the Zombie Dice game from Steve Jackson Games.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, multiplayer"""

import random

# 상수 설정하기:
GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = ["+-----------+",
             "|     .     |",
             "|    ,O,    |",
             "| 'ooOOOoo' |",
             "|   `OOO`   |",
             "|   O' 'O   |",
             "+-----------+"]
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""Lucky Stars, by Al Sweigart al@inventwithpython.com

A "press your luck" game where you roll dice with Stars, Skulls, and
Question Marks.

On your turn, you pull three random dice from the dice cup and roll
them. You can roll Stars, Skulls, and Question Marks. You can end your
turn and get one point per Star. If you choose to roll again, you keep
the Question Marks and pull new dice to replace the Stars and Skulls.
If you collect three Skulls, you lose all your Stars and end your turn.

When a player gets 13 points, everyone else gets one more turn before
the game ends. Whoever has the most points wins.

There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
even.
""")

print('How many players are there?')
while True:  # 사용자가 숫자를 입력할 때까지 루프를 돈다.
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        numPlayers = int(response)
        break
    print('Please enter a number larger than 1.')

playerNames = []  # 플레이어의 이름(문자열) 리스트.
playerScores = {}  # 키는 플레이어 이름이고, 값은 점수다.
for i in range(numPlayers):
    while True:  # 이름을 입력할 때까지 루프를 돈다.
        print('What is player #' + str(i + 1) + '\'s name?')
        response = input('> ')
        if response != '' and response not in playerNames:
            playerNames.append(response)
            playerScores[response] = 0
            break
        print('Please enter a name.')
print()

turn = 0  # playerNames[0]의 플레이어가 먼저 한다.
# (!) 'Al'이라는 이름의 플레이어가 3점을 가지고 시작하도록 주석을 해제하자:
#playerScores['Al'] = 3
endGameWith = None
while True:  # 메인 게임 루프
    # 모든 플레이어의 점수를 표시한다:
    print()
    print('SCORES: ', end='')
    for i, name in enumerate(playerNames):
        print(name + ' = ' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            # 모든 플레이어의 이름이 구분되도록 마지막 플레이어 이름을 제외하고 콤마를 붙인다.
            print(', ', end='')
    print('\n')

    # 수집한 별과 해골 수를 0으로 시작한다.
    stars = 0
    skulls = 0
    # 컵에는 골드 주사위 6개, 실버 주사위 4개, 브론즈 주사위 3개가 있다:
    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = []  # 여러분의 손은 주사위 없이 시작한다.
    print('It is ' + playerNames[turn] + '\'s turn.')
    while True:  # 이 루프가 돌 때마다 주사위를 굴린다.
        print()

        # 컵에 주사위가 충분히 남아 있는지 확인한다:
        if (3 - len(hand)) > len(cup):
            # 주사위가 충분히 남아 있지 않기 때문에 이번 턴을 끝낸다:
            print('There aren\'t enough dice left in the cup to '
                + 'continue ' + playerNames[turn] + '\'s turn.')
            break

        # 여러분의 손에 3개의 주사위를 가질 때까지 컵에서 주사위를 가져온다:
        random.shuffle(cup)  # 컵에 있는 주사위를 섞는다.
        while len(hand) < 3:
            hand.append(cup.pop())

        # 주사위를 굴린다:
        rollResults = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
                # 골드 주사위(별 3개, 물음표 2개, 해골 1개) 굴리기:
                if 1 <= roll <= 3:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == SILVER:
                # 실버 주사위(별 2개, 물음표 2개, 해골 2개) 굴리기:
                if 1 <= roll <= 2:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == BRONZE:
                # 브론즈 주사위(별 1개, 물음표 2개, 해골 3개) 굴리기:
                if roll == 1:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 2 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1

        # 주사위 결과 표시하기:
        for lineNum in range(FACE_HEIGHT):
            for diceNum in range(3):
                print(rollResults[diceNum][lineNum] + ' ', end='')
            print()  # Print a newline.

        # 주사위의 타입(골드, 실버, 브론즈)을 표시한다:
        for diceType in hand:
            print(diceType.center(FACE_WIDTH) + ' ', end='')
        print()  # 개행 출력하기

        print('Stars collected:', stars, '  Skulls collected:', skulls)

        # 해골이 3개 이상 나왔는지 확인하기:
        if skulls >= 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(playerNames[turn] + ', do you want to roll again? Y/N')
        while True:  # 플레이어가 Y 또는 N을 입력할 때까지 계속 요청한다:
            response = input('> ').upper()
            if response != '' and response[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if response.startswith('N'):
            print(playerNames[turn], 'got', stars, 'stars!')
            # 별의 개수를 플레이어의 전체 스코어에 추가한다:
            playerScores[playerNames[turn]] += stars

            # 플레이어가 13점 이상을 획득했는지 확인한다:
            # (!) 이 값을 5 또는 50으로 바꿔 보자.
            if (endGameWith == None
                and playerScores[playerNames[turn]] >= 13):
                # 플레이어가 13점 이상을 획득했다면,
                # 나머지 다른 모든 플레이어를 위해 한 번의 라운드를 플레이한다:
                print('\n\n' + ('!' * 60))
                print(playerNames[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                endGameWith = playerNames[turn]
            input('Press Enter to continue...')
            break

        # 별과 해골을 버리고 물음표만 유지한다:
        nextHand = []
        for i in range(3):
            if rollResults[i] == QUESTION_FACE:
                nextHand.append(hand[i])  # 물음표를 유지한다.
        hand = nextHand

    # 다음 플레이어 턴으로 이동한다:
    turn = (turn + 1) % numPlayers

    # 게임이 끝났다면, 이 루프에서 빠져 나간다:
    if endGameWith == playerNames[turn]:
        break  # 게임을 종료한다.

print('The game has ended...')

# 모든 플레이어의 스코어를 표시한다:
print()
print('SCORES: ', end='')
for i, name in enumerate(playerNames):
    print(name + ' = ' + str(playerScores[name]), end='')
    if i != len(playerNames) - 1:
        # 모든 플레이어의 이름이 구분되도록 마지막 플레이어 이름을 제외하고 콤마를 붙인다.
        print(', ', end='')
print('\n')

# 승자가 누구인지 알아낸다:
highestScore = 0
winners = []
for name, score in playerScores.items():
    if score > highestScore:
        # 이 플레이어의 스코어가 가장 높다:
        highestScore = score
        winners = [name]  # 이전 승자에 덮어 쓴다.
    elif score == highestScore:
        # 이 플레이어는 가장 높은 스코어와 동점이다.
        winners.append(name)

if len(winners) == 1:
    # 단 한 명의 승자만 있다:
    print('The winner is ' + winners[0] + '!!!')
else:
    # 여러 명의 승자가 있다:
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')
