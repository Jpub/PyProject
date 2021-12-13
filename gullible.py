"""Gullible, by Al Sweigart al@inventwithpython.com
How to keep a gullible person busy for hours. (This is a joke program.)
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, humor"""

print('Gullible, by Al Sweigart al@inventwithpython.com')

while True:  # 메인 프로그램 루프
    print('Do you want to know how to keep a gullible person busy for hours? Y/N')
    response = input('> ')  # 사용자의 응답을 받는다.
    if response.lower() == 'no' or response.lower() == 'n':
        break  # 만약에 "no"라면, 루프에서 빠져나간다.
    if response.lower() == 'yes' or response.lower() == 'y':
        continue  # 만약에 "yes"라면, 루프의 시작점으로 돌아간다.
    print('"{}" is not a valid yes/no response.'.format(response))

print('Thank you. Have a nice day!')
