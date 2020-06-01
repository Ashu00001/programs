d={}
e={}
l={}
k={}
temp=0
val=0
a=input()
b=input()
for i in range(len(a)):
    d[i]=a[i]
print(d)
for i in range(len(b)):
    e[i]=b[i]
print(e)
for i in range(len(a)):
    if(d[i]!=e[i]):
        l[i]=d[i]
        for j in range(len(b)):
            if(d[i]==e[j]):
                temp=e[i]
                e[i]=d[i]
                e[j]=temp
print(k)
print(l)
print("\n\n")
print(d)
print(e)


for i in range(len(a)):
    if(d[i]==e[i]):
        print("equal")
        break
