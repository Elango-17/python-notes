a=10
b="hello"
print(str(a)+b)

str1="hello elango"
str2="how are you"
print(str1[0:2])
print(str1[4])
print(str1*2)
print(str1+str2)

'''1.Application of python

speech and image  recognition
food recommendation
health care

2.List (store a different data types in single variable)
Ordered
Changeble
Allow Duplicates'''
 
#access items

l1 = ["apple", "banana", "cherry"]
print(l1[-1])
print(l1[0])

#Range

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

l1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
l1[1:3]="red","lemon"
print(l1)
l1.insert(4,"elango")
print(l1)

l2=[1,2,3,4,5,6,7]
l2.append(8)
print(l2)
l2.reverse()
print(l2)
l2.insert(3,2)
print(l2)

l1=["elango","lango"]
l2=("madhan","sudhan")
l1.extend(l2)
print(l1)