n = int(input("0,1,2,3,4,5"))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
