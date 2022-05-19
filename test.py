a = int(input())
b = int(input())

n6 = a*b
n3 = a * (b % 10)
b /= 10 
n4 = a * (b % 10)
b /= 10 
n5 = a*b 
