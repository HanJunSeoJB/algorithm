def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]을 {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1:
        move(no - 1, 6 - x - y, y)


print('하노이 탑을 구성합니다')
n = int(input())
move(n, 1, 3)