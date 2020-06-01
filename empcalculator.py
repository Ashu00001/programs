emp_name=input("enter name : ")
emp_id=eval(input("enter the id : "))
emp_dept=input("enter the dept : ")
emp_designation=input("enter the designation : ")
print("name : "+emp_name)
print("ID : ",emp_id)
print("Department : "+emp_dept)
print("name : "+emp_designation)
yearpay=0

def pay(payrate,hour,week):
    monthpay=(payrate*hour*week)
    return monthpay

print(pay(12,4,1))

for x in range (1 , 13):
    month=input("enter the month : ")
    a=eval(input("payrate : "))
    b=eval(input("hours : "))
    c=eval(input("weeks : "))
    d=pay(a,b,c)
    
    yearpay=yearpay+d

print("total yearpay : ",yearpay)

if(yearpay<500000):
    print("tax : 0")

elif(yearpay>=500000 and yearpay<1000000):
    tax=(0.1*yearpay)
    print("yearpay : ",yearpay)
    print("tax : ",tax)
    
elif(yearpay>=1000000):
    tax=(0.2*yearpay)
    print("tax : ",tax)

netsalary=yearpay-tax
print(netsalary)
