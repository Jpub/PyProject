"""Hacking Minigame, by Al Sweigart al@inventwithpython.com
The hacking mini-game from "Fallout 3". Find out which seven-letter
word is the password by using clues each guess gives you.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, game, puzzle"""

# 참고: 이 프로그램은 sevenletterwords.txt 파일이 필요하다.
# 이 파일은 https://inventwithpython.com/sevenletterwords.txt에서 다운로드할 수 있다.

import random, sys

# 상수 설정하기:
# '컴퓨터 메모리' 표현을 위한 가비지 필터 문자
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# 7글자 단어로 구성된 텍스트 파일을 WORDS 리스트로 로드한다.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # 모든 단어를 대문자로 변환하고 끝에 있는 줄바꿈을 제거한다:
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """Run a single game of Hacking."""
    print('''Hacking Minigame, by Al Sweigart al@inventwithpython.com
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.\n''')
    input('Press Enter to begin...')

    gameWords = getWords()
    # '컴퓨터 메모리'는 그냥 꾸미는 것이지만 멋져 보인다:
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # 4번의 기회를 가지고 시작하며, 점점 감소한다:
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S   G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries. Secret password was {}.'.format(secretPassword))


def getWords():
    """Return a list of 12 words that could possibly be the password.

    The secret password will be the first word in the list.
    To make the game fair, we try to ensure that there are words with
    a range of matching numbers of letters as the secret word."""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # 두 단어를 더 찾는다. 아직 일치하는 문자가 들어 있지 않다.
    # 비밀 암호는 이미 words에 들어있기 때문에 '< 3'을 사용한다.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # 세 글자가 일치하는 단어 2개를 찾는다.
    # (500번을 돌면서 찾았는데도 없다면 찾는 걸 포기한다)
    for i in range(500):
        if len(words) == 5:
            break  # 5개의 단어를 찾았다면 루프를 빠져나간다.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # 적어도 한 글자 이상 일치하는 단어를 7개는 찾는다.
    # (500번을 돌면서 찾았는데도 없다면 찾는 걸 포기한다)
    for i in range(500):
        if len(words) == 12:
            break  # 7개 이상의 단어를 찾았다면 루프를 빠져나간다.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # 찾은 단어가 전부 12개가 될 때까지 무작위로 단어를 추가한다.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    """Returns a random word from WORDS that isn't in blocklist."""
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def numMatchingLetters(word1, word2):
    """Returns the number of matching letters in these two words."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def getComputerMemoryString(words):
    """Return a string representing the "computer memory"."""

    # 단어를 포함하기 위해 단어마다 한 줄을 사용한다.
    # 16개의 줄이 있지만 두 부분으로 나눈다.
    linesWithWords = random.sample(range(16 * 2), len(words))
    # 시작 부분의 메모리 주소(이것 역시 꾸미는 역할을 한다).
    memoryAddress = 16 * random.randint(0, 4000)

    # '컴퓨터 메모리' 문자열을 생성한다.
    computerMemory = []  # 각 줄에 하나씩 16개의 문자열을 포함한다.
    nextWord = 0  # 각 줄에 넣을 배열 words의 인덱스
    for lineNum in range(16):  # '컴퓨터 메모리'는 16줄을 갖는다.
        # 가비지 문자를 반 줄 만든다:
        leftHalf = ''
        rightHalf = ''
        for j in range(16):  # 각 반 줄은 16 개의 문자를 갖는다.
            leftHalf += random.choice(GARBAGE_CHARS)
            rightHalf += random.choice(GARBAGE_CHARS)

        # words에 있는 단어들로 채운다:
        if lineNum in linesWithWords:
            # 단어를 삽입할 반 줄의 임의 위치를 구한다:
            insertionIndex = random.randint(0, 9)
            # 단어를 삽입한다:
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord]
                + leftHalf[insertionIndex + 7:])
            nextWord += 1  # 반 줄에 넣을 단어를 업데이트한다.
        if lineNum + 16 in linesWithWords:
            # 단어를 삽입할 반 줄의 임의 위치를 구한다:
            insertionIndex = random.randint(0, 9)
            # 단어를 삽입한다:
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord]
                + rightHalf[insertionIndex + 7:])
            nextWord += 1  # 반 줄에 넣을 단어를 업데이트한다.

        computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                     + '  ' + leftHalf + '    '
                     + '0x' + hex(memoryAddress + (16*16))[2:].zfill(4)
                     + '  ' + rightHalf)

        memoryAddress += 16  # 다음으로 이동. 예를 들어 0xe680에서 0xe690으로 이동.

    # computerMemory 리스트의 각 문자열은
    # 반환될 하나의 큰 문자로 결합된다:
    return '\n'.join(computerMemory)


def askForPlayerGuess(words, tries):
    """Let the player enter a password guess."""
    while True:
        print('Enter password: ({} tries remaining)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print('Try entering "{}" or "{}".'.format(words[0], words[1]))


# 이 프로그램이 다른 프로그램에 임포트(import)된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
