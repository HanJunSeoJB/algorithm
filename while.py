print('a부터 b까지 정수의 합 구합니다')
a = int(input('a값 : '))
b = int(input('b값 : '))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b+1):
    sum += i

print(f'합계: {sum}')

