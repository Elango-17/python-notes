#global variable
x="super"
def myfunc():
    x="fantastic"
    print("Python is "+x)
myfunc()
print("python is "+x)


'''DATA TYPES:

text-string
numeric-int ,float,complex
sequence-list,tuple
mapping-dict
boolean-true,false
set'''

#data types

a="Hello world"
b=20
c=20.5
d=range(6)
e= None
f=["apple","mango","banana"]
g= 1+4j
h=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

#NUMERIC
#float

x=35e6
y=12E4
z=-87.7e100
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))

#complex

z=-7j
print(z)
print(type(z))


#TYPE CONVERSION:
    
#type conversion
#int to float

a=7
print(float(a))

#float to  int

b=2.33
print(int(b))

#int to complex

c=2
print(complex(c))


'''CASTING :
secifies  a variable type or converts from one data type to another
same as type conversion'''

#casting
#int

x=int(3.14)
print(x)

#float

y=float(5)
print(y)

#boolean

c=bool(0)
d=bool(1)
print(c,d)

#string

e=str(42)
print(e)

#excerise int

x=int(1)
y=int(2.8)
z=int("3")
print(x,y,z)

#ex float

x=float(1)
y=float(2.8)
z=float("3")
w=float("4.2")
print(x,y,z,w)

