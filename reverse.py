#뮤터블 시퀸스 원소를 역순으로 정렬
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]


if __name__ == '__main__':
    print('배열의 원소를 역순으로 정렬합니다')
    nx = int(input('원소 수 입력: '))
    x = [None] * nx
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요: '))
    
    reverse_array(x)

    print('역순으로 정렬 완료')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')