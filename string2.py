str = "Kevin"

# displaying whole string
print(str)

# displaying first character of string
print(str[0])

# displaying third character of string
print(str[2])

# displaying the last character of the string
print(str[-1])

# displaying the second last char of string
print(str[-2])

str = "Beginnersbook"

# displaying whole string
print("The original string is: ", str)

# slicing 10th to the last character
print("str[9:]: ", str[9::3])

# slicing 3rd to 6th character
print("str[2:6]: ", str[2:6])

# slicing from start to the 9th character
print("str[:9]: ", str[:9])

# slicing from 10th to second last character
print("str[9:-1]: ", str[9:-1])
print(str[-1:-1])
print(str[-3:-1])
print(str[::-1])
print(str[:-1])

str = "Welcome to beginnersbook.com"
str2 = "Welcome XYZ"
str3 = "come XYZ"
str4 = "XYZ"

# str2 is in str? True
print(str2 in str)

# str3 is in str? False
print(str3 in str2)


# str4 not in str? True
print(str4 not in str)
print(str4 not in str3)
str = "AbC"
str2 = "aBC"
str3 = "aYZ"
str4 = "byz"
print(str>str2)
print(str4<str3)

b = "Hello, World!"
print(b[-5:-2])

a = " Hello World! "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(" "))

txt = "The rain in Spain stays mainly in the plain {}"
x = "ain" in txt
print(x)
x = "ain" not in txt
print(x)
age=36
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

r="resdddeff"
print(type(r))
print(r[0:4:1])