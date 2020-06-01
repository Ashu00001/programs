str="ashutosh"
b=len(str)
print(b)
m=0
d={}
f={}
for i in range(0,len(str)-1):
    val=str[i:i+1]
    d[i]=val
print("\n")
print(d,"\n")


for i in range(0,len(str)-1):
    m=0
    val=str[i:i+1]
    print(val)
    for j in range(0,len(str)):
        if(val==str[j]):
            m=m+1
    f[val]=m       
    print(m)
        
print(val,m)
print(f)
    
