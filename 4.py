def a(n):

    for i in range(n):
        for a in range(n,n+i):
            print(" ", end=" ")
        for a in range(i, n-1):
            print("* ", end="")
        for b in range(n, i):
            print(" ", end="")
        for c in range(i, n):
            print("* ", end="")
        print("\r")
        
n = int(input())
a(n)
