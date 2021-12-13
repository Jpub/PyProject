"""Sound Mimic, by Al Sweigart al@inventwithpython.com
A pattern-matching game with sounds. Try to memorize an increasingly
longer and longer pattern of letters. Inspired by the electronic game,
Simon.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, beginner, game"""

import random, sys, time

# 다음 URL에서 사운드 파일을 다운로드 하거나 여러분이 가진 파일을 사용하자:
# https://inventwithpython.com/soundA.wav
# https://inventwithpython.com/soundS.wav
# https://inventwithpython.com/soundD.wav
# https://inventwithpython.com/soundF.wav

try:
    import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install playsound')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install playsound')
    sys.exit()


print('''Sound Mimic, by Al Sweigart al@inventwithpython.com
Try to memorize a pattern of A S D F letters (each with its own sound)
as it gets longer and longer.''')

input('Press Enter to begin...')

pattern = ''
while True:
    print('\n' * 60)  # 여러 줄바꿈을 출력하여 화면을 깨끗하게 한다.

    # 무작위 문자를 패턴에 추가한다:
    pattern = pattern + random.choice('ASDF')

    # 패턴을 표시하고 사운드를 재생한다:
    print('Pattern: ', end='')
    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound.playsound('sound' + letter + '.wav')

    time.sleep(1)  # 마지막에 잠깐 동안 일시 중지가 되도록 한다.
    print('\n' * 60)  # 여러 줄바꿈을 출력하여 화면을 깨끗하게 한다.

    # 플레이어가 패턴을 입력하게 하자:
    print('Enter the pattern:')
    response = input('> ').upper()

    if response != pattern:
        print('Incorrect!')
        print('The pattern was', pattern)
    else:
        print('Correct!')

    for letter in pattern:
        playsound.playsound('sound' + letter + '.wav')

    if response != pattern:
        print('You scored', len(pattern) - 1, 'points.')
        print('Thanks for playing!')
        break

    time.sleep(1)
