n=int(input("enter the value of n : "))
if(n<=0 ):
    print("Plese enter a positive integer ")
else:
    a=0
    b=1

    print(a)
    for i in range(n-1):
        c=a+b
        a=b
        b=c
        print(a)
