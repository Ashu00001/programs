a=eval(input("enter a number : "))
result=0

def fact(a):
    if(a==1):
        return 1
    else:
        result=a*fact(a-1)
        return result

res=fact(a)
print("fact : ",res)
