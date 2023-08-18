def a(n):
 for i in range(n):
        for a in range(1+i, n):
            print(" ", end=" ")
        for b in range(0-i, 1):
            print("* ", end="")
        for c in range(n, i):
            print(" ", end="")
        for d in range(1-i, 1):
            print("* ", end="")
        print("\r")
        
n = int(input())
a(n)
