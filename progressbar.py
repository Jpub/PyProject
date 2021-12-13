"""Progress Bar Simulation, by Al Sweigart al@inventwithpython.com
A sample progress bar animation that can be used in other programs.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, module"""

import random, time

BAR = chr(9608) # Character 9608은 '█'

def main():
    # 다운로드 시뮬레이션하기:
    print('Progress Bar Simulation, by Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        # 임의 양의 '바이트'를 '다운로드':
        bytesDownloaded += random.randint(0, 100)

        # 진행률에 대한 프로그레스 바 문자열을 가져온다:
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        # 끝에 줄바꿈을 출력하지 말자.
        # 화면에 출력된 문자열을 즉시 플러시한다:
        print(barStr, end='', flush=True)

        time.sleep(0.2)  # 잠깐 일시 정지한다:

        # 텍스트 커서를 줄의 시작 위치로 이동하기 위해 백스페이스를 출력한다:
        print('\b' * len(barStr), end='', flush=True)


def getProgressBar(progress, total, barWidth=40):
    """Returns a string that represents a progress bar that has barWidth
    bars and has progressed progress amount out of a total amount."""

    progressBar = ''  # 이 변수의 값은 문자열이다.
    progressBar += '['  # 프로그레스 바의 왼쪽 끝을 만든다.

    # 진행률이 0에서 total 사이인지 확인한다:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # 표시할 '바'의 수를 계산한다:
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars  # 프로그레스 바를 추가한다.
    progressBar += ' ' * (barWidth - numberOfBars)  # 빈 공백을 추가한다.
    progressBar += ']'  # 프로그레스 바의 오른쪽 끝을 추가한다.

    # 완료률을 계산한다:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'  # 퍼센트 표시를 추가한다.

    # 숫자를 추가한다:
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar  # 프로그레스 바 문자열을 반환한다.


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
