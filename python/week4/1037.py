n = int(input())
divs = [int(i) for i in input().split()]

divs.sort()

print(divs[0] * divs[-1])