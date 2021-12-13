"""Fish Tank, by Al Sweigart al@inventwithpython.com
A peaceful animation of a fish tank. Press Ctrl-C to stop.
Similar to ASCIIQuarium or @EmojiAquarium, but mine is based on an
older ASCII fish tank program for DOS.
https://robobunny.com/projects/asciiquarium/html/
https://twitter.com/EmojiAquarium
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: extra-large, artistic, bext"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 상수 설정하기:
WIDTH, HEIGHT = bext.size()
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다.
WIDTH -= 1

NUM_KELP = 2  # (!) 이 값을 10으로 바꿔 보자.
NUM_FISH = 10  # (!) 이 값을 2 또는 100으로 바꿔 보자.
NUM_BUBBLERS = 1  # (!) 이 값을 0 또는 10으로 바꿔 보자.
FRAMES_PER_SECOND = 4  # (!) 이 값을 1 또는 60으로 바꿔 보자.
# (!) 이들 상수를 조절하여 다시마와 공기 방울만 있는
# 수족관을 만들어 보자.

# 참고: 물고기 딕셔너리의 모든 문자열은 길이가 같아야 한다.
FISH_TYPES = [
  {'right': ['><>'],          'left': ['<><']},
  {'right': ['>||>'],         'left': ['<||<']},
  {'right': ['>))>'],         'left': ['<[[<']},
  {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
  {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
  {'right': ['>-==>'],        'left': ['<==-<']},
  {'right': [r'>\\>'],        'left': ['<//<']},
  {'right': ['><)))*>'],      'left': ['<*(((><']},
  {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
  {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
  {'right': ['><XXX*>'],      'left': ['<*XXX><']},
  {'right': ['_.-._.-^=>', '.-._.-.^=>',
             '-._.-._^=>', '._.-._.^=>'],
   'left':  ['<=^-._.-._', '<=^.-._.-.',
             '<=^_.-._.-', '<=^._.-._.']},
  ]  # (!) 여러분만의 물고기를 FISH_TYPES에 추가하자.
LONGEST_FISH_LENGTH = 10  # FISH_TYPES에서 가장 긴 단일 문자열의 길이.

# 물고기가 화면의 가장자리에 닿을 때 x와 y 위치:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # 전역 변수 생성하기:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # 참고: BUBBLERS가 아닌 공기 방울이 그려진다.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # 각 공기 방울은 임의의 위치에서 시작된다.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # 다시마의 각 부분을 생성한다:
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # 시뮬레이션 실행:
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1


def getRandomColor():
    """Return a string of a random color."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))


def generateFish():
    """Return a dictionary that represents a fish."""
    fishType = random.choice(FISH_TYPES)

    # 물고기 텍스트의 각 문자에 대한 색을 설정한다:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random':  # 모든 부분은 색이 무작위로 지정된다.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength  # 모두 같은 색상
    if colorPattern == 'head-tail':  # 머리/꼬리는 몸통과 다르다.
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # 머리 색 설정하기
        colors[-1] = headTailColor  # 꼬리 색 설정하기

    # 나머지 물고기 데이터 구조를 설정한다:
    fish = {'right':            fishType['right'],
            'left':             fishType['left'],
            'colors':           colors,
            'hSpeed':           random.randint(1, 6),
            'vSpeed':           random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight':       random.choice([True, False]),
            'goingDown':        random.choice([True, False])}

    # 'x'는 항상 물고기 몸의 가장 왼쪽이다:
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    """Simulate the movements in the aquarium for one step."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # 한 단계 물고기의 움직임을 시뮬레이션한다:
    for fish in FISHES:
        # 물고기가 수평으로 움직인다:
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1  # 물고기를 오른쪽으로 이동한다.
                else:
                    fish['goingRight'] = False  # 물고기의 방향을 돌린다.
                    fish['colors'].reverse()  # 색상을 돌린다.
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1  # 물고기를 왼쪽으로 이동한다.
                else:
                    fish['goingRight'] = True  # 물고기의 방향을 돌린다.
                    fish['colors'].reverse()  # 색상을 돌린다.

        # 물고기는 수평 방향을 임의로 변경할 수 있다:
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10, 60)
            # 물고기의 방향을 돌린다:
            fish['goingRight'] = not fish['goingRight']

        # 물고기가 수직으로 움직인다:
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1  # 물고기를 아래로 이동한다.
                else:
                    fish['goingDown'] = False  # 물고기의 방향을 돌린다.
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1  # 물고기를 위로 이동한다.
                else:
                    fish['goingDown'] = True  # 물고기의 방향을 돌린다.

        # 물고기는 수직 방향을 임의로 변경할 수 있다:
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] = random.randint(2, 20)
            # 물고기의 방향을 돌린다:
            fish['goingDown'] = not fish['goingDown']

    # BUBBLES로부터 공기 방울을 생성한다:
    for bubbler in BUBBLERS:
        # 공기 방울을 만들 확률은 5분의 1이다:
        if random.randint(1, 5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    # 공기 방울을 움직인다:
    for bubble in BUBBLES:
        diceRoll = random.randint(1, 6)
        if (diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1  # 공기 방울이 왼쪽으로 간다.
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1  # 공기 방울이 오른쪽으로 간다.

        bubble['y'] -= 1  # 공기 방울은 항상 위로 간다.

    # BUBBLES를 반대로 루프를 돈다.
    # 왜냐하면 이 루프를 통해 삭제를 하기 때문이다.
    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:  # 상단에 도착한 공기 방울은 삭제한다.
            del BUBBLES[i]

    # 물결치는 다시마의 움직임을 한 단계 시뮬레이션한다:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # 20분의 1 확률로 움직임을 변경한다:
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    """Draw the aquarium on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # 종료 메시지 그리기
    bext.fg('white')
    bext.goto(0, 0)
    print('Fish Tank, by Al Sweigart    Ctrl-C to quit.', end='')

    # 공기 방울 그리기:
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')

    # 물고기 그리기:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # 오른쪽 또는 왼쪽을 향하믄 물고기 텍스트를 가져온다.
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]

        # 물고기 텍스트의 각 문자를 올바른 색상으로 그린다.
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    # 다시마 그리기:
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end='')

    # 바닥에 모래 그리기:
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')  # '░' 문자를 그린다.

    sys.stdout.flush()  # (bext를 사용하는 프로그램에 필요한 부분)


def clearAquarium():
    """Draw empty spaces over everything on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP

    # 공기 방울을 그린다:
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    # 물고기를 그린다:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # 물고기 텍스트의 각 문자를 올바른 색상으로 그린다.
        print(' ' * len(fish['left'][0]), end='')

    # 다시마 그리기:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print('  ', end='')

    sys.stdout.flush()  # (bext를 사용하는 프로그램에 필요한 부분)


# 이 프로그램이 다른 프로그램에 임포트(import)된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
