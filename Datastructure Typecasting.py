#giving list and performing typecasting
print("giving list and performing typecasting")
f=[10,20,"abcds",40.08,10+12j]
print(id(f))
print(type(f))
print(str(f))
print(bool(f))
print(tuple(f))
print(set(f))
print(id(frozenset(f)))
#giving tuple and performing typecasting
print("giving tuple and performing typecasting")
g=(10,20,30,"abcds",40.08,10+12j)
print(id(g))
print(type(g))
print(str(g))
print(bool(g))
print(list(g))
print(set(g))
#giving set and performing typecasting
print("giving set and performing typecasting")
h={1,2,"fell",12.34,12+1.2j}
print(id(h))
print(type(h))
print(str(h))
print(bool(h))
print(list(h))
print(tuple(h))
#giving dict and performing typecasting
print("giving dict and performing typecasting")
i={1:"ram",2:"teja","a":12,1.2:"ust",13+1.2j:1.2}
print(id(i))
print(type(i))
print(str(i))
print(bool(i))

