a, b, c = map(int, input().split())
time = int(input())

h = time // (60*60)
time -= h*60*60

m = time // 60
time -= m * 60

s = time

c_ = c + s
if c_ >= 60:
    m += 1
    c_ -= 60

b_ =  b + m
if b_ >= 60:
    h += 1
    b_ -= 60

a_ = a + h
if a_ >= 24:
    a_ %= 24

print(f"{a_} {b_} {c_}\n")
