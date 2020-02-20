a=[10,12.3,"abcdef",True,12+0.8j]
b=[12,12.34,'adecgf',False,144.03+18j]
e=[]
print(type(a))
print(a[0])
print(a)
print(a[0]+a[1])
print(a[-1])
print(b)
print(a[0]+b[1])
print(type(a[4]))
print(a[-1:2])
print(a[2:-1])
print(b[ :3])
print(b[3: ])
print(b[ : ])
for i in range(len(a)):
    a.remove(a[0])
    print(a)
c=[12.456,13.65,15.089,True,False,1,2,3,12+4j,13+2.3j]
n=len(c)
print(n)
for i in range(n):
    print(c[i])
c.remove(c[0])
print(c)

d=[12.456,13.65,15.089,True,False,1,2,3,12+4j,13+2.3j]
print(d)
d.append(13+1.90j)
print(d)
print(d.copy())
print(d.count(2))
d.extend("abcde")
print(d)
print(d.index(True))
print(d.pop())
d.remove(True)
print(d)
d.reverse()
print(d)
d.clear()
print(d)


