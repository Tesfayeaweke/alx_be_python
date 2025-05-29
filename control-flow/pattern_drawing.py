size = int(input("Enter the size of the pattern: "))

m=0
while m < size:
    n=0
    while n < size: 
        print("*",end="")
        n+=1
    print()
    m+=1