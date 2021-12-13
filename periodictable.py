"""Periodic Table of Elements, by Al Sweigart al@inventwithpython.com
Displays atomic information for all the elements.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, science"""

# https://en.wikipedia.org/wiki/List_of_chemical_elements의 데이터
# 표를 복사하여 엑셀이나 구글 시트와 같은 스프레드시트 프로그램에 붙인다.
# https://invpy.com/elements
# 그런 다음, periodictable.csv라는 이름으로 저장하거나,
# https://inventwithpython.com/periodictable.csv에서 이 csv 파일을 다운로드받는다.

import csv, sys, re

# periodictable.csv로부터 모든 데이터를 읽는다.
elementsFile = open('periodictable.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']

# 텍스트를 정렬하려면 ALL_COLUMNS에서 가장 긴 문자열을 찾아야 한다.
LONGEST_COLUMN = 0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)

# 모든 원소 데이터를 데이터 구조에 넣는다:
ELEMENTS = {}  # 모든 원소 데이터를 저장하고 있는 데이터 구조
for line in elements:
    element = {'Atomic Number':  line[0],
               'Symbol':         line[1],
               'Element':        line[2],
               'Origin of name': line[3],
               'Group':          line[4],
               'Period':         line[5],
               'Atomic weight':  line[6] + ' u', # 원소 질량 단위
               'Density':        line[7] + ' g/cm^3', # 그램/세제곱 cm
               'Melting point':  line[8] + ' K', # 켈빈
               'Boiling point':  line[9] + ' K', # 켈빈
               'Specific heat capacity':      line[10] + ' J/(g*K)',
               'Electronegativity':           line[11],
               'Abundance in earth\'s crust': line[12] + ' mg/kg'}

    # 예를 들어, 붕소의 원자량처럼
    # 원소 위키백과에는 일부 데이터에 삭제해야 할 괄호로 묶인 텍스트가 있다.
    # '10.81[III][IV][V][VI]'은 '10.81'처럼 되어야 한다:

    for key, value in element.items():
        # [로마 숫자] 텍스트 제거하기:
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

    ELEMENTS[line[0]] = element  # 원소 번호를 원소에 매핑한다.
    ELEMENTS[line[1]] = element  # 원소 기호를 원소에 매핑한다.

print('Periodic Table of Elements')
print('By Al Sweigart al@inventwithpython.com')
print()

while True:  # 메인 프로그램 루프
    # 주기율표를 표시하고 사용자가 원소를 선택할 수 있게 한다:
    print('''            Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('> ').title()

    if response == 'Quit':
        sys.exit()

    # 선택된 원소의 데이터를 표시한다:
    if response in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(keyJustified + ': ' + ELEMENTS[response][key])
        input('Press Enter to continue...')
