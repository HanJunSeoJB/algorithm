def med3(a, b, c):
    if a >= b: 
        if b >= c: 
            return b
        elif a <= c: 
            return a
        else:
            return c
    elif a > c: 
        return a
    elif b > c: 
        return c
    else:
        return b


print('세 정수의 중앙값을 구합니다')
a = int(input('a값 입력: '))
b = int(input('b값 입력: '))
c = int(input('c값 입력: '))
print(f'중앙값은 {med3(a, b, c)}입니다')