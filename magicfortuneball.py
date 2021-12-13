"""Magic Fortune Ball, by Al Sweigart al@inventwithpython.com
Ask a yes/no question about your future. Inspired by the Magic 8 Ball.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, humor"""

import random, time


def slowSpacePrint(text, interval=0.1):
    """Slowly display text with spaces in between each letter and
    lowercase letter i's."""
    for character in text:
        if character == 'I':
            # 대문자 I를 소문자로 표시한다:
            print('i ', end='', flush=True)
        else:
            # 다른 문자들은 그대로 표시한다:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()  # 끝에 두 줄 개행한다.
    print()


# 질문에 대한 프롬프트:
slowSpacePrint('MAGIC FORTUNE BALL, BY AL SWEiGART')
time.sleep(0.5)
slowSpacePrint('ASK ME YOUR YES/NO QUESTION.')
input('> ')

# 간단한 응답을 표시한다:
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]
slowSpacePrint(random.choice(replies))

# 극적 효과를 위한 멈춤:
slowSpacePrint('.' * random.randint(4, 12), 0.7)

# 답을 준다:
slowSpacePrint('I HAVE AN ANSWER...', 0.2)
time.sleep(1)
answers = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]
slowSpacePrint(random.choice(answers), 0.05)
