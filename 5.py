def aa(n):
    num = 1 
    for i in range(n):
        for a in range(i, n):
            print(" ", end="")
        for b in range(1, i + 2):
            print(num, end=" ")  
            num = (num + 1) % 10  
        print("\r")

while True:
    n = int(input())
    if 1 <= n <= 4:
        break
aa(n)
