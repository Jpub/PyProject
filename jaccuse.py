"""J'ACCUSE!, by Al Sweigart al@inventwithpython.com
A mystery game of intrigue and a missing cat.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: extra-large, game, humor, puzzle"""

# 원래의 플래시 게임을 해 보자.
# https://homestarrunner.com/videlectrix/wheresanegg.html
# 자세한 정보는 http://www.hrwiki.org/wiki/Where's_an_Egg%3F를 참고하자.

import time, random, sys

# 상수 설정하기:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # 300초(5분)이 주어진다.

# 메뉴 표시를 위해 장소의 첫 번째 글자와 가장 긴 길이가 필요하다:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# 상수들의 기본적인 개수 확인:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# 첫 번째 글자는 고유해야 한다:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)


knownSuspectsAndItems = []
# visitedPlaces: 키는 장소, 값은 그곳의 용의자와 아이템의 문자열.
visitedPlaces = {}
currentLocation = 'TAXI'  # 이 게임은 택시에서 시작한다.
accusedSuspects = []  # 고발된 용의자는 단서를 제공하지 않는다.
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3  # 3 명까지 고발할 수 있다.
culprit = random.choice(SUSPECTS)

# 이들을 연결하는 공통 인덱스. 예를 들어, SUSPECTS[0]과 ITEMS[0]은 PLACES[0]에 있다.
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# 진실을 말하는 사람들이 제공하는
# 아이템과 용의자에 대한 단서의 데이터 구조를 생성한다.
# clues: 키는 단서가 제공된 용의자. 값은 '단서 딕셔너리'
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue  # 여기서 거짓말하는 사람은 건너 뛴다.

    # 이 '단서 딕셔너리'의 키는 아이템과 용의자이며,
    # 값은 주어진 단서이다.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False  # 디버깅에 도움이 된다.
    for item in ITEMS:  # 각 아이템에 대한 단서를 선택한다.
        if random.randint(0, 1) == 0:  # 아이템이 어디에 있는지 알려 준다:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:  # 누가 아이템을 가지고 있는지 알려 준다:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:  # 각 용의자에 대한 단서를 선택한다.
        if random.randint(0, 1) == 0:  # 용의자가 어디에 있는지 알려 준다:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:  # 용의자가 가지고 있는 아이템이 무엇인지 알려 준다:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

# 거짓을 말하는 사람들이 제공하는
# 아이템과 용의자에 대한 단서의 데이터 구조를 생성한다:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue  # 우리는 이미 진실을 말하는 사람들에 대한 처리를 했다.

    # 이 '단서 딕셔너리'의 키는 아이템과 용의자이며,
    # 값은 주어진 단서다:
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True  # 디버깅에 도움이 된다.

    # 이 인터뷰 대상자는 거짓을 말하는 사람이며 잘못된 단서를 제공한다:
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:  # 무작위로 (잘못된) 장소에 대한 단서를 선택한다.
                # 아이템이 있는 장소에 대해 거짓말을 한다.
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    # 거짓 단서가 선택되면 루프를 빠져나간다.
                    break
        else:
            while True:  # 무작위로 (잘못된) 용의자에 대한 단서를 선택한다.
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    # 거짓 단서가 선택되면 루프를 빠져나간다.
                    break
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:  # 무작위로 (잘못된) 장소에 대한 단서를 선택한다.
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    # 거짓 단서가 선택되면 루프를 빠져나간다.
                    break
        else:
            while True:  # 무작위로 (잘못된) 아이템에 대한 단서를 선택한다.
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    # 거짓 단서가 선택되면 루프를 빠져나간다.
                    break

# 조피에 대해 물었을 때 제공되는 단서에 대한 데이터 구조를 생성한다:
zophieClues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kindOfClue = random.randint(1, 3)
    if kindOfClue == 1:
        if interviewee not in liars:
            # 누가 조피를 가지고 있는지를 말한다.
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                # (잘못된) 용의자 단서를 선택한다.
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                    # 거짓 단서가 선택되면 루프를 빠져나간다.
                    break

    elif kindOfClue == 2:
        if interviewee not in liars:
            # 조피가 어디에 있는지를 말한다.
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # (잘못된) 장소 단서를 선택한다.
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    # 거짓 단서가 선택되면 루프를 빠져나간다.
                    break
    elif kindOfClue == 3:
        if interviewee not in liars:
            # 조피 근처에 있는 아이템이 무엇인지를 말한다.
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # (잘못된) 아이템 단서를 선택한다.
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    # 거짓 단서가 선택되면 루프를 빠져나간다.
                    break

# 실험: 단서에 대한 데이터 구조를 보기 위해 다음 코드의 주석을 해제하자:
#import pprint
#pprint.pprint(clues)
#pprint.pprint(zophieClues)
#print('culprit =', culprit)

# 게임의 시작
print("""J'ACCUSE! (a mystery game)")
By Al Sweigart al@inventwithpython.com
Inspired by Homestar Runner\'s "Where\'s an Egg?" game

You are the world-famous detective, Mathilde Camus.
ZOPHIE THE CAT has gone missing, and you must sift through the clues.
Suspects either always tell lies, or always tell the truth. Ask them
about other people, places, and items to see if the details they give are
truthful and consistent with your observations. Then you will know if
their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
CAT in time and accuse the guilty party?
""")
input('Press Enter to begin...')


startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

while True:  # 메인 게임 루프
    if time.time() > endTime or accusationsLeft == 0:
        # '게임 오버' 조건 처리하기:
        if time.time() > endTime:
            print('You have run out of time!')
        elif accusationsLeft == 0:
            print('You have accused too many innocent people!')
        culpritIndex = SUSPECTS.index(culprit)
        print('It was {} at the {} with the {} who catnapped her!'.format(culprit, PLACES[culpritIndex], ITEMS[culpritIndex]))
        print('Better luck next time, Detective.')
        sys.exit()

    print()
    minutesLeft = int(endTime - time.time()) // 60
    secondsLeft = int(endTime - time.time()) % 60
    print('Time left: {} min, {} sec'.format(minutesLeft, secondsLeft))

    if currentLocation == 'TAXI':
        print('  You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            placeInfo = ''
            if place in visitedPlaces:
                placeInfo = visitedPlaces[place]
            nameLabel = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print('{} {}{}'.format(nameLabel, spacing, placeInfo))
        print('(Q)UIT GAME')
        while True:  # 유효한 입력이 들어올 때까지 계속 요청한다.
            response = input('> ').upper()
            if response == '':
                continue  # 다시 요청한다.
            if response == 'Q':
                print('Thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTERS[response]
        continue  # 메인 게임 루프의 시작점으로 돌아간다.

    # 장소에서; 플레이어는 단서에 대해 물어볼 수 있다.
    print('  You are at the {}.'.format(currentLocation))
    currentLocationIndex = PLACES.index(currentLocation)
    thePersonHere = SUSPECTS[currentLocationIndex]
    theItemHere = ITEMS[currentLocationIndex]
    print('  {} with the {} is here.'.format(thePersonHere, theItemHere))

    # 이 장소의 용의자와 아이템을
    # 알려진 용의자와 아이템 리스트에 추가한다:
    if thePersonHere not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(thePersonHere)
    if ITEMS[currentLocationIndex] not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(ITEMS[currentLocationIndex])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = '({}, {})'.format(thePersonHere.lower(), theItemHere.lower())

    # 플레이어가 이전에 잘못된 사람을 고발했다면,
    # 단서를 제공하지 않을 것이다:
    if thePersonHere in accusedSuspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')
        currentLocation = 'TAXI'
        continue  # 메인 게임 루프의 시작점으로 돌아간다.

    # 질문할 항목으로 알려진 용의자와 아이템을 메뉴로 표시한다:
    print()
    print('(J) "J\'ACCUSE!" ({} accusations left)'.format(accusationsLeft))
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspectOrItem in enumerate(knownSuspectsAndItems):
        print('({}) Ask about {}'.format(i + 1, suspectOrItem))

    while True:  # 유효한 입력이 들어올 때까지 계속 요청한다.
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response) <= len(knownSuspectsAndItems)):
            break

    if response == 'J':  # 플레이어는 이 용의자를 고발한다.
        accusationsLeft -= 1  # 고발 횟수를 사용한다.
        if thePersonHere == culprit:
            # 올바른 용의자를 고발했다.
            print('You\'ve cracked the case, Detective!')
            print('It was {} who had catnapped ZOPHIE THE CAT.'.format(culprit))
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken = int(time.time() - startTime) % 60
            print('Good job! You solved it in {} min, {} sec.'.format(minutesTaken, secondsTaken))
            sys.exit()
        else:
            # 잘못된 용의자를 고발했다.
            accusedSuspects.append(thePersonHere)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            currentLocation = 'TAXI'

    elif response == 'Z':  # 플레이어는 조피에 대해 묻는다.
        if thePersonHere not in zophieClues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif thePersonHere in zophieClues:
            print('  They give you this clue: "{}"'.format(zophieClues[thePersonHere]))
            # 알려진 것들의 리스트에 장소가 아닌 단서들을 추가한다:
            if zophieClues[thePersonHere] not in knownSuspectsAndItems and zophieClues[thePersonHere] not in PLACES:
                knownSuspectsAndItems.append(zophieClues[thePersonHere])

    elif response == 'T':  # 플레이어는 택시로 돌아간다.
        currentLocation = 'TAXI'
        continue  # 메인 게임 루프의 시작점으로 돌아간다.

    else:  # 플레이어는 용의자 또는 아이템에 대해 묻는다.
        thingBeingAskedAbout = knownSuspectsAndItems[int(response) - 1]
        if thingBeingAskedAbout in (thePersonHere, theItemHere):
            print('  They give you this clue: "No comment."')
        else:
            print('  They give you this clue: "{}"'.format(clues[thePersonHere][thingBeingAskedAbout]))
            # 알려진 것들의 리스트에 장소가 아닌 단서들을 추가한다:
            if clues[thePersonHere][thingBeingAskedAbout] not in knownSuspectsAndItems and clues[thePersonHere][thingBeingAskedAbout] not in PLACES:
                knownSuspectsAndItems.append(clues[thePersonHere][thingBeingAskedAbout])

    input('Press Enter to continue...')
