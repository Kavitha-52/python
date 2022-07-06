'''a=10
print(a)
print(type(a))

a=1.1324
print(a)
print(type(a))

a='A'
print(a)
print(type(a))

a="Apple"
print(a)
print(type(a))

a=None
print(a)
print(type(a))

a,b,c=10,20,30
print(a)
print(b)
print(c)
print(a,b,c)
print(a+b+c)

a=b=c=10
print(a,b,c)
print(a+b)
print(a-b)

a=10
print(a)
print(type(a))
print(float(a))

b=float(a)
print(b)
print(type(a))
print(int(b))

c=int(b)
print(c)
print(type(c))

name="kavitha"
print("my name is :",name)

name=input("enter a name:")
print("my name is :",name)

a=10
b=20
print(a+b)
a=input("enter a num1:")# it will take string format
b=input("enter a num1:")
print(a+b)


a=int(input("enter a value:"))
b=int(input("enter a value:"))
print(a+b)

a=float(input("enter a value:"))
b=float(input("enter a value:"))
print(a+b)


a=(input("enter a atring 1:"))
b=(input("enter a string 2:"))
print(a+b)

a=10
b=20
print(a>b)
print(a<b)
print(type(a))
print(type(b))
c=a>b
print(type(c))

a=10
b=20
c=complex(a,b)
print(c)
print(type(c))
print(c.real)
print(c.imag)

s="thudersoft"
print(s)
print(type(s))
a=thunder
soft
private limited
company
print(a)

s="thunder"
print(s)
s.replace("thunder","soft")#it can't replace
print(s)

s="thunder"
print(s)
s1=s.replace("thunder","soft")
print(s1)
print(s1+"hyderabad")


s="thunder"
print(s)
print(s.replace("thunder","soft"))
print(s+"hyderabad")

l=[]
print(l)
print(type(l))

l=[1,2,3,1.21113,'a',"hell"]
print(l)
print(type(l))
l.append("welcome")
print(l)
print(l.append('mango'))#it will not appended

l.remove(1)
print(l)
print(l.remove(2))# error

t=()
print(t)
print(type(t))

t=(1,2,3,10.678,'n',"hyderabad")
print(t)
print(dir(tuple))
t.remove(1)#remove append is not in tuple
print(t)
#print(t.append("is beautiful"))
print(dir(tuple))

s={}
print(s)
print(type(s))#dictonary
s={1,2,3,1.231,'s',"apple",'k'}
print(s)
#print(s[0])#in this not possible because values are not ordered

s.add(100)
print(s)
s.discard(100)
print(s)

d={}
print(d)
print(type(d))

d={1,2,3}
print(type(d))

d={1:"apple",2:"mango",3:"banana"}
print(type(d))
print(d)
for k,v in d.items():
    print(k,v)


d={1:"sai",2:"mohan",3:"ram",2:"ram"}
print(d)
    
d={1:"sai",2:"mohan",3:"ram",4:"ram"}
print(d)

d={"sai":1,"mohan":2,"ram":3,"ram":4}
print(d)
    
d={"sai":1,"mohan":2,"ram":3,"ram":2}
print(d)

a=range(0,10)
print(list(a))
print(set(a))

a=range(0,10,2)
print(list(a))

a=1
b=1
print( a is b)
print(id(a))
print(id(b))
print(a is  not b)

a="kavitha"
b="Kavitha"
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

a=10
b=2
print(bin(a&b))
print(a&b)
print(bin(a|b))
print(a|b)
print(bin(a^b))
print(a^b)
print(a<<4)
print(a>>4)

i=10
if i==10:
    print("true")
    
i=int(input("enter a number:"))
j=int(input("enter a number:"))
if i>j:
    print(i,"is greater")
else:
    print(j,"is greater")
    
    
i=int(input("enter a number:"))
if i<10:
    print(i ,"is less than 10")
elif i==10:
    print(i," is equal to 10")
elif i<0:
    print(i," is negative value")
else:
    print(i," is greater than 10")


l=[1,2,3,'k',"hii","hello"]
for i in l:
    print(i)

s="kavitha"
for i in s:
    print(i)


for i in range(0,10,3):
    #print(i)
    print(i,end=" ")

n=int(input("enter a number:"))
s=0   
for i in range(n):
      s=s+i
print(s)

for i in range (1,30):
    if(i%2==0):
        print("even numbers:",i,end=" ")

num=[1,2,3,4]
alpha=['a','b','c','d','e']
for i in num:
    print(i)
for i in alpha:
    print(i)

num=[1,2,3,4]
alpha=['a','b','c','d','e']
for i in num:
    print(i)
    for i in alpha:
        print(i)
i=1
while(i<10):
    print(i)
    i=i+1
    
n=int(input("enter a number:"))
i=1
s=0
while(i<n):
    s=s+i
    print(s)
    i=i+1

n=int(input("enter a number:"))
i=1
s=0
while(i<n):
    s=s+i
    i=i+1
print(s)

i=1
while(i<10):
    print(i)
    i=i+1
    if(i==5):
        break
i=1
while(i<10):
    if(i==5):
        #i=i+1
        continue
    print(i)
    i=i+1
i=1
while(i<10):
    if(i==5):
        i=i+1
        continue
    print(i)
    i=i+1
for i in range(1,11):
    print(i,end=" ")
    if(i==5):
        break
    
for i in range(1,11):
    print(i,end=" ")
    if(i==5):
        continue   

##strings
s="thunder soft"
print(s[0])
print(s[-1])
print(s[7])       
print(s[8])
print(s[0:])
print(s[:7])
print(s[2:8])
print(s[-3:-1])
print(s[0:len(s):2])
print(s[::-1])
print(s[:-1])
print(s[::-2])

s1="hii"
s2="hello"
s3="how are you"
print(s1+s2)
print(s1*5+s2*5)
print(s1+" "+s2+" "+s3)

s="python is easy to learn"
print(s)
s1=s.split(" ",4)
for i in s1:
    print(i)
    
s="python is easy to learn com[aring other languages"
print(s)
s1=s.split(" ",4)
for i in s1:
    print(i)

s="python is very easy"
print(s.capitalize())

s="Python Is Very Easy"
print(s.capitalize())

s="python is very easy"
s1=s.title()
print(s1)
print(s.upper())
print(s.lower())
print(s.replace("python","c"))
print(s.count("p"))

s="KaViThA"
print(s.swapcase())
s="python is very easy"
print(s.replace(" ","*"))

s=["python","ds","c","java"]
s.sort()
print(s)

s="  apple   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s="thundersoft"
print(len(s))
print(s.find('r'))
print(s[0])
print(s.find('z'))
#print(s.index('z'))
print(s.rindex("t"))
print(min(s))
print(max(s))
print(dir(str))
print(s.startswith("t"))
print(s.startswith("x"))
print(s.endswith("t"))
print(s.endswith("a"))

s="1234"
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
s="12 34"
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())

s="asfff1gh"
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())

#list
l=[1,23,[10,20,'l',"hii"],100]
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[2][0])
print(l[2][1])
print(l[2][2])
print(l[2][3]

l=[1,2,3,4]
l.append(5)
print(l)
l.insert(0,6)
print(l)
l.extend([10,20,30,'k',"kavi"])
print(l)

l=[1,2,3]
print(l)
l[1]=12
print(l)
l.insert(0,10)
print(l)
l.remove(3)
print(l)
print(l.pop(0))
l.clear()
print(l)
print(l.clear())

l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
print(l1*2)
l=[1,2,90,34,12,21.324,32.234]
print(l.sort())

l.sort()
print(l)
l.sort(reverse=True)
print(l)

l1=[1,2,3]
l2=l1
print(l1)
print(l2)
print(id(l1))
print(id(l2))
l1.append(9)
print(l1)
print(l1.append(5))
print(l2)
l3=l1.copy()
print(l3)
l3.extend([1,2,3])
print(l3)
print(l1)

l=[1,2,3,4,1,2,1,1,1,2,3,1]
print(l.count(1))
s=l.count(4)
print(s)

print(list(range(10)))
print(list(range(0,20,2)))

t=(1,2,3,"hii",'l')
t1=(10,20)
print(t+t1)
t2=(1,23,12321,1,12)
print(max(t2))
print(min(t2))
print(sum(t2,-8))

s="kavitha"
print(type(s))
t=tuple(s)
print(type(t))

l=[1,2,3,4,5]
t=tuple(l)
print(t)

t=(1,2,3,4)
l=list(t)
print(l)

t=(1,2,3)
a,b,c=t
print(a)
print(b)
print(c)

#set
s={1,2,3,4,5}
s.add("hello")
print(s)
s.update([12,345])
print(s)
s.remove(1)
print(s)
s.clear()
print(s)
del s
print(s)


a={1,2,3,4,5}
b={4,5,3,6,7}
print(a&b)
print(a.intersection(b))
print(a|b)
print(a.union(b))
print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(b))
