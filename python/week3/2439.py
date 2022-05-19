n = int(input())

# for i in range(1, n+1, 1):
#     a = n - i 
#     print(" "*(a) + "*"*(i))

for i in range(n):
    print(" "*(n - i - 1)+"*"*(i+1))
    