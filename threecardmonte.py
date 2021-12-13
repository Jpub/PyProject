"""Three-Card Monte, by Al Sweigart al@inventwithpython.com
Find the Queen of Hearts after cards have been swapped around.
(In the real-life version, the scammer palms the Queen of Hearts so you
always lose.)
More info at https://en.wikipedia.org/wiki/Three-card_Monte
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, card game, game"""

import random, time

# 상수 설정하기:
NUM_SWAPS = 16   # (!) 이 값을 30 또는 100으로 바꿔 보자.
DELAY     = 0.8  # (!) 이 값을 2.0 또는 0.0으로 바꿔 보자.

# 카드 모양 문자:
HEARTS   = chr(9829)  # 문자 9829는 '♥'
DIAMONDS = chr(9830)  # 문자 9830은 '♦'
SPADES   = chr(9824)  # 문자 9824는 '♠'
CLUBS    = chr(9827)  # 문자 9827은 '♣'
# chr() 코드 목록은 https://inventwithpython.com/chr을 참고하자.

# 세 장의 카드 목록 인덱스:
LEFT   = 0
MIDDLE = 1
RIGHT  = 2


def displayCards(cards):
    """Display the cards in "cards", which is a list of (rank, suit)
    tuples."""
    rows = ['', '', '', '', '']  # 표시할 텍스트를 저장한다.

    for i, card in enumerate(cards):
        rank, suit = card  # 카드는 튜플 데이터 구조다.
        rows[0] += ' ___  '  # 카드의 윗줄을 출력한다.
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))


    # 화면에 각 행을 출력한다:
    for i in range(5):
        print(rows[i])


def getRandomCard():
    """Returns a random card that is NOT the Queen of Hearts."""
    while True:  # 하트 퀸이 아닌 카드를 갖을 때까지 카드를 만든다.
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])

        # 하트 퀸이 아니라면 하드를 반환한다:
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)


print('Three-Card Monte, by Al Sweigart al@inventwithpython.com')
print()
print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
print('the cards move.')
print()

# 원래의 배치를 표시한다:
cards = [('Q', HEARTS), getRandomCard(), getRandomCard()]
random.shuffle(cards)  # 하트 퀸을 임의의 위치에 둔다.
print('Here are the cards:')
displayCards(cards)
input('Press Enter when you are ready to begin...')

# 교체에 대해 출력한다:
for i in range(NUM_SWAPS):
    swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])

    if swap == 'l-m':
        print('swapping left and middle...')
        cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
    elif swap == 'm-r':
        print('swapping middle and right...')
        cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
    elif swap == 'l-r':
        print('swapping left and right...')
        cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
    elif swap == 'm-l':
        print('swapping middle and left...')
        cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
    elif swap == 'r-m':
        print('swapping right and middle...')
        cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
    elif swap == 'r-l':
        print('swapping right and left...')
        cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]

    time.sleep(DELAY)

# 교체에 대한 내용을 숨기기 위해 여러 줄을 출력한다.
print('\n' * 60)

# 레드 레이디를 찾도록 사용자에게 요청한다:
while True:  # LEFT, MIDDLE, 또는 RIGHT가 입력될 때까지 계속 요청한다:
    print('Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)')
    guess = input('> ').upper()

    # 플레이어가 입력한 위치에 대한 카드 인덱스를 가져온다:
    if guess in ['LEFT', 'MIDDLE', 'RIGHT']:
        if guess == 'LEFT':
            guessIndex = 0
        elif guess == 'MIDDLE':
            guessIndex = 1
        elif guess == 'RIGHT':
            guessIndex = 2
        break

# (!) 플레이어가 항상 지도록 하려면 다음 코드의 주석을 해제한다:
#if cards[guessIndex] == ('Q', HEARTS):
#    # 플레이어가 이겼으니 퀸을 이동시키자.
#    possibleNewIndexes = [0, 1, 2]
#    possibleNewIndexes.remove(guessIndex)  # 퀸의 인덱스를 제거한다.
#    newInd = random.choice(possibleNewIndexes)  # 새로운 인덱스를 고른다.
#    # 퀸을 새로운 인덱스에 둔다:
#    cards[guessIndex], cards[newInd] = cards[newInd], cards[guessIndex]

displayCards(cards)  # 모든 카드를 표시한다.

# 플레이어가 이겼는지 확인한다:
if cards[guessIndex] == ('Q', HEARTS):
    print('You won!')
    print('Thanks for playing!')
else:
    print('You lost!')
    print('Thanks for playing, sucker!')
