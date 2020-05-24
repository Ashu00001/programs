n=eval(input("enter a no of testcase : "))


fact=1
while(n>0):
    a=eval(input("enter a no : "))
    for i in range(1,a+1):
        fact=fact*i
       
    n=n-1

print("fact : ",fact)
