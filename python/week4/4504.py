n = input()
n = int(n)
# n = int(input())

while True:
    a = input()
    a = int(a)
    if a == 0:
        break

    if a % n == 0: 
        print(f"{a} is a multiple of {n}.")
    else:
        print(f"{a} is NOT a multiple of {n}.")

