def pattern(n):
    for i in range (1,n+1):
        for space in range(n-i):
            print(" " ,end=" ")
        for j in range (1,i+1):
            print(j,end=" ")

        print()

n=int(input("Enter the number :"))

pattern(n)

