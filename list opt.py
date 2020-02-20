a=[1,2,12.8,13+12j,"aefredg"]
a.insert(3, 100)
print(a)
a.append(99)
print(a)
a.extend([11, 22])
print(a)
a[2]=20
print(a)
a[3:5]=[12+1.2j,"ramteja"]
print(a)
b=[12,13,12.24,0.088,12+0.04j,"harish"]
del b[4]
print(b)
del b[1:5]
print(b)
del b
c=[12,13,12.24,0.088,12+0.04j,"harish"]
print(c)
c.remove(12)
print(c)
c.pop(3)
print(c)
c.pop()
print(c)
c.clear()
print(c)

l =[];
n = int(input("Enter the number of elements in the list")); #Number of elements will be entered by the user
for i in range(n): # for loop to take the input
    l.append(input("Enter the item?")); # The input is taken from the user and added to the list as the item
for i in l: # traversal loop to print the list items
    print(i, end = "  ");


List = [0,1,2,3,4,13+0.4j,"abcde",13.089]
print("printing original list: ");
for i in List:
    print(i,end=" ")
List.remove(0)
print("\nprinting the list after the removal of first element...")
for i in List:
    print(i,end=" ")
print(len(List))