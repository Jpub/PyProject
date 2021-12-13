"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, artistic"""

import sys

# (!) 여러분이 좋아하는 이미지 모양으로 여러 줄의 문자열을 변경해 보자:

# 문자열의 상단과 하단에 마침표 68개가 있다:
# https://inventwithpython.com/bitmapworld.txt의 문자열을
# 복사하여 붙여넣기해도 된다.
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# 루프를 돌며 bitmap의 각 행을 반복한다:
for line in bitmap.splitlines():
    # 루프를 돌며 행의 각 문자를 반복한다:
    for i, bit in enumerate(line):
        if bit == ' ':
            # bitmap의 해당 위치가 공백이므로 빈 공백을 출력한다:
            print(' ', end='')
        else:
            # message의 문자를 출력한다:
            print(message[i % len(message)], end='')
    print()  # 줄을 바꾼다.
