s=[1,2,35,45,6,7,0]
print(len(s))
temp=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if  s[i]<s[j]:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
print(s)