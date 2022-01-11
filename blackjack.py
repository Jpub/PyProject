"""Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, card game"""

import random, sys

# 상수 설정:
HEARTS   = chr(9829) # 문자 9829는 '♥'.
DIAMONDS = chr(9830) # 문자 9830은 '♦'.
SPADES   = chr(9824) # 문자 9824는 '♠'.
CLUBS    = chr(9827) # 문자 9827은 '♣'.
# (chr 코드에 대한 목록은 https://inventwithpython.com/charactermap을 참조하자)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.''')

    money = 5000
    while True:  # 메인 게임 루프
        # 플레이어가 돈을 다 썼는지 검사:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # 이번 판에 얼마를 베팅할 것인지 입력하게 한다:
        print('Money:', money)
        bet = getBet(money)

        # 딜러와 플레이어에게 두 장의 카드를 준다:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # 플레이어의 동작을 처리한다:
        print('Bet:', bet)
        while True:  # 플레이어가 stand 또는 bust될 때까지 계속 루프를 돈다.
            displayHands(playerHand, dealerHand, False)
            print()

            # 플레이어가 bust되었는지 검사:
            if getHandValue(playerHand) > 21:
                break

            # 플레이어의 동작(H, S, 또는 D)을 받는다:
            move = getMove(playerHand, money - bet)

            # 플레이어의 동작을 처리한다:
            if move == 'D':
                # 플레이어가 double down을 함. 베팅을 올릴 수 있다:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit 또는 double down이면 다른 카드를 하나 받는다.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # 플레이어가 bust됨:
                    continue

            if move in ('S', 'D'):
                # Stand 또는 double down이면 플레이어 턴이 끝난다.
                break

        # 딜러의 동작을 처리한다:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # 딜러가 hit함:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # 딜러가 bust됨
                input('Press Enter to continue...')
                print('\n\n')

        # 들고 있던 패를 공개함:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # 플레이어가 이겼는지, 졌는지, 아니면 비겼는지 처리함:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')


def getBet(maxBet):
    """플레이어에게 이번 판에 얼마를 걸지 묻는다."""
    while True:  # 유효한 값을 입력할 때까지 계속 질문한다.
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # 플레이어가 숫자를 입력하지 않았다면 다시 물어본다.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # 플레이어가 유효한 베팅을 입력


def getDeck():
    """52개의 모든 카드에 대한 (rank, suit) 튜플 리스트를 반환한다."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # 숫자로 된 카드를 추가한다.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # 문자로 된 카드를 추가한다.
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """플레이어와 딜러의 카드를 보여준다.
    만약에 showDealerHand가 False이면, 딜러의 첫 번째 카드를 가린다."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # 딜러의 첫 번째 카드를 가린다:
        displayCards([BACKSIDE] + dealerHand[1:])

    # 플레이어의 모든 카드를 표시한다:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """카드의 값을 반환한다. 얼굴이 있는 카드들은 모두 10이며,
    에이스는 11 또는 1이다(이 함수는 최적의 에이스 값을 선택한다)."""
    value = 0
    numberOfAces = 0

    # 에이스가 아닌 나머지 카드들에 값을 추가한다:
    for card in cards:
        rank = card[0]  # card는 (rank, suit)의 튜플이다.
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # 문자 카드는 10을 더한다.
            value += 10
        else:
            value += int(rank)  # 숫자 카드는 자신의 숫자만큼의 값을 더한다.

    # 에이스에 대한 값을 더한다:
    value += numberOfAces  # 에이스 하나당 1을 더한다.
    for i in range(numberOfAces):
        # 만약에 추가로 10을 더해도 bust가 되지 않는다면, 그렇게 한다:
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """카드 리스트에 있는 모든 카드를 표시한다."""
    rows = ['', '', '', '', '']  # 각 행에 표시될 텍스트 변수

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # 카드의 상단 라인 출력
        if card == BACKSIDE:
            # 카드의 뒷면 출력:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # 카드의 앞면 출력:
            rank, suit = card  # card는 튜플 데이터 구조다.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # 화면에 각 행을 출력:
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """플레이어 차례에서 플레이어 선택을 묻는다.
    히트인 'H', 스탠드인 'S', 더블 다운인 'D'를 반환한다."""
    while True:  # 플레이어가 올바른 입력을 할 때까지 계속 반복한다.
        # 플레이어가 선택할 수 있는 게 무엇인지 결정한다:
        moves = ['(H)it', '(S)tand']

        # 플레이어가 최초에 받은 카드 두 장이 서로 같다면,
        # double down할 수 있음을 알려준다.
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # 플레이어의 선택을 받는다:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  # 플레이어는 유효한 선택을 입력했다.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # 플레이어는 유효한 선택을 입력했다.


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
