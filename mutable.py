a=[]
n=int(input("enter the list range"))
for i in range(n):
    item=input("enter the list")
    if item.isnumeric() is True:
        if item.isdigit()is True:
            item=int(item)
            a.insert(item,float(item))
    else:
        a.append(item)
print(a)


n=int(input("Enter length of the list"))
l1=[]
for i in range(n):
    a=input()
    if a.isdigit():
        l1.insert(i,float(a)) #statement1
    else:
        l1.insert(i,a)
print(li)