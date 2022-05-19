n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))

# 제일 큰 순서로 내림차순 정렬
ropes.sort(reverse=True)

ans = 0
for i in range(n):
    weight = ropes[i] * (i + 1)
    ans = max(weight, ans)

print(ans)