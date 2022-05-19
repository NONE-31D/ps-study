import sys
input = sys.stdin.readline

n = int(input())
heights = []
ans = 0
for _ in range(n):
    h = int(input())
    if heights:
        if heights[-1][0] < h:
            while heights and heights[-1][0] < h:
                height = heights.pop()
                if height[1] > 1:
                    ans += height[1] * (height[1] - 1) // 2
                ans += height[1]
                if heights:
                    ans += height[1]
        if heights and heights[-1][0] == h:
            heights[-1][1] += 1
            continue
        
    heights.append([h, 1])

while heights:
    height = heights.pop()
    if height[1] > 1:
        ans += height[1] * (height[1] - 1) // 2
    if heights:
        ans += height[1]


print(ans)
        