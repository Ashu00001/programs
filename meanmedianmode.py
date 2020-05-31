def maxi(dataset):
    a=0
    for i in dataset:
        if a<i:
            a=i
    print("max="+str(a))

def mini(dataset):
    a=dataset[0]
    for i in dataset:
        if a>i:
            a=i
    print("min="+str(a))
def mean(dataset):
    length=len(dataset)
    sumoflist=sum(dataset)
    mean=sumoflist/length
    print("mean="+str(mean))

def median(dataset):
    length=len(dataset)
    sumoflist=sum(dataset)
    sort=sorted(dataset)
    if length%2==0:
        median1=sort[length//2]
        median2=sort[length//2-1]
        median=(median1+median2)/2
    else:
        median=dataset[length//2]
    print("median="+str(median))
def mode(dataset):
    mode=max(dataset,key=dataset.count)
    print("mode is"+str(mode))

dataset=[1,2,3,4,5,6,7]
maxi(dataset)
mini(dataset)
mean(dataset)
median(dataset)
mode(dataset)
