n = int(input())

ans = 0

for _ in range(n):
    ans += int(input())

ans /= n

if ans >= 0.5 :
    print("Junhee is cute!")
else: 
    print("Junhee is not cute!")
