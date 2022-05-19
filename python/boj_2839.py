n = int(input())

box_5 = n // 5
n %= 5
if n % 3 == 0:
    print(box_5 + n // 3)
else:
    print(-1)