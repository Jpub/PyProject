"""Duckling Screensaver, by Al Sweigart al@inventwithpython.com
A screensaver of many many ducklings.

>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, object-oriented, scrolling"""

import random, shutil, sys, time

# 상수 설정하기:
PAUSE = 0.2  # (!) 이 값을 1.0 또는 0.0으로 바꿔 보자.
DENSITY = 0.10  # (!) 이 값을 0.0 ~ 1.0 범위의 값으로 바꿔 보자.

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# 터미널 창의 크기를 얻는다:
WIDTH = shutil.get_terminal_size()[0]
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다.
WIDTH -= 1


def main():
    print('Duckling Screensaver, by Al Sweigart')
    print('Press Ctrl-C to quit...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  # 메인 프로그램 루프.
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # 이 줄에 오리를 생성해야 하는지 확인한다:
            if (ducklingObj == None and random.random() <= DENSITY):
                    # 이 줄에 오리를 둔다:
                    ducklingObj = Duckling()
                    ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # 이 줄에 오리가 있으면 그린다:
                print(ducklingObj.getNextBodyPart(), end='')
                # 그리기가 끝났다면 오리를 삭제한다:
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                # 여기에 오리가 없다면 공백 5개를 그린다.
                print(' ' * DUCKLING_WIDTH, end='')

        print()  # 줄바꿈을 한다.
        sys.stdout.flush()  # 화면에 텍스트가 표시되도록 한다.
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """임의의 신체 특징들을 가진 새로운 오리를 생성한다."""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # 통통한 오리는 눈동자만 가질 수 있다.
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        """오리 머리에 대한 문자열을 반환한다."""
        headStr = ''
        if self.direction == LEFT:
            # 입을 추가한다:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            # 눈을 추가한다:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '  # 뒤통수를 추가한다.

        if self.direction == RIGHT:
            headStr += ' ('  # 뒤통수를 추가한다.

            # 눈을 추가한다:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            # 입을 추가한다:
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # 통통한 오리가 매우 통통한 오리의 폭과 동일하도록
            # 여분의 공간을 확보한다.
            headStr += ' '

        return headStr

    def getBodyStr(self):
        """오리 몸통에 대한 문자열을 반환한다."""
        bodyStr = '('  # 몸의 왼쪽을 추가한다.
        if self.direction == LEFT:
            # 몸통 내부 공간을 추가한다:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            # 날개를 추가한다:
            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:
            # 날개를 추가한다:
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            # 몸통 내부 공간을 추가한다:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'  # 몸의 오른쪽을 추가한다.

        if self.body == CHUBBY:
            # 통통한 오리가 매우 통통한 오리의 폭과 동일하도록
            # 여분의 공간을 확보한다.
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        """오리 발에 대한 문자열을 반환한다."""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """표시해야 하는 다음 몸통에 대한 
        메서드를 호출한다. 그런 다음,
        partToDisplayNext에 None을 설정한다."""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()



# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
