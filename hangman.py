"""Hangman, by Al Sweigart al@inventwithpython.com
Guess the letters to a secret word before the hangman is drawn.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, word, puzzle"""

# 이 게임은 "Invent Your Own Computer Games with Python" 책에도 나와 있다.
# https://nostarch.com/inventwithpython

import random, sys

# 상수 설정하기:
# (!) HANGMAN_PICS의 문자열을 추가하거나 변경하여
# 교수대를 기요틴으로 바꿔 보자.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# (!) 새로운 문자열을 가진 CATEGORY와 WORDS로 교체해 보자.
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


def main():
    print('Hangman, by Al Sweigart al@inventwithpython.com')

    # 새로운 게임을 위해 변수를 셋업한다:
    missedLetters = []  # 틀린 글자 리스트
    correctLetters = []  # 맞춘 글자 리스트
    secretWord = random.choice(WORDS)  # 플레이어가 맞춰야 하는 단어

    while True:  # 메인 게임 루프
        drawHangman(missedLetters, correctLetters, secretWord)

        # 사용자가 예상한 글자 입력하기:
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # 맞춘 글자를 correctLetters에 추가하기:
            correctLetters.append(guess)

            # 플레이어가 이겼는지 검사하기:
            foundAllLetters = True  # 플레이어가 이겼다는 가정으로 시작.
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # correctLetters에 정답인 단어의 글자가 아직 없기 때문에,
                    # 플레이어가 이긴 것이 아니다:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break  # 메인 게임 루프에서 빠져나온다.
        else:
            # 플레이어의 추측이 틀렸다:
            missedLetters.append(guess)

            # 플레이어가 기회를 다 써서 졌는지 확인한다.
            # ('- 1'을 하는 이유는
            # HANGMAN_PICS에서 교수대가 비어 있는 단계를 카운트하지 않기 때문이다.)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break


def drawHangman(missedLetters, correctLetters, secretWord):
    """비밀 단어에 대해 맞힌 글자와 틀린 글자와 함께
    교수형 집행인의 현재 상태를 그린다."""
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    # 틀린 글자들을 보여 준다:
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # 정답 단어에 대해 한 글자당 한 칸씩 빈칸을 표시한다:
    blanks = ['_'] * len(secretWord)

    # 맞춘 글자는 빈칸 대신 표시한다:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # 글자 사이에 공백을 표시한다:
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    """플레이어가 입력한 문자를 반환한다. 
    이 함수는 플레이어가 이전에 추측하지 않은 문자를 입력했는지 확인한다."""
    while True:  # 플레이어가 유효한 글자를 입력할 때까지 계속 요청한다.
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
