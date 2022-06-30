'''a=b=c=10
print(a)
print(b)
print(c)
print(a,b,c)
print(a,b,c,sep=",")
print(a,end=",")
print(b,end=",")
print(c,end=","

a,b,c=10,20,30
print(a)
print(b)
print(c)
print(c,b,a)

a=10
print(a)
print(type(a

a=1.132
print(a)
print(type(a))

a="apple"
print(a)
print(type(a))

a='N'
print(a)
print(type(a))

a=20
print(a)
print(type(a))

b=float(a)
print(b)
print(type(b))

c=int(b)
print(c)
print(type(c))

a=10
b=20
print(a+b)
a=int(input("enter  a  number:"))
b=int(input("enter  a  number:"))
print("sum is :",a+b)

a=input("enter  a  number:")
b=input("enter  a  number:")
print("sum is :",a+b)

name="kavitha"
print("my name is:",name)

name=input("enter name:")
print("Name  is:",name)
a=1
b=5
c=a<b
print(c)
print(type(c))

a=1
b=5
print(a>b)

a=1
b=2
c=complex(a,b)
print(c)
print(type(c))
print(c.real)
print(c.imag)

import keyword
print(keyword.kwlist)

a=None
print(a)
print(type(a))

print(dir(str))

print(dir(list))'''

#a='''kavitha
    # honey'''
'''print(a)

a="apple"
print(a)
a.replace("apple","mango")#it gives error we cant replace directly
print(a)

a="apple"
print(a)     
s=a.replace("apple","mango")
print(s)

a="apple"
print(a)     
print(a.replace("apple","mango"))

#-----list-----#
l=[]
print(l)
print(type(l))

l=[1,2,3,4,5,6,7]
print(l)
l.append(100)
print(l)
l.remove(100)
print(l)

l=[1,"kavitha",3.143,'A']
print(l)
l=[1,2,3,4,5,6,7,1,2]
print(l)

//----TUPLE----//

t=(1,2,3,4,5)
print(t)
print(type(t))

t=(1,2,3,4,5,1,2)
print(t)
print(type(t))


t=(1,"kavitha",3.143,'A')
print(t)
print(t[0])
print(t[1])
print(t[2])

t=(1,)
print(t)
print(type(t))

//set//

s={1,2,3,4,5}
print(s)
print(type(s))
s=(1,"kavitha",3.143,'A')
print(s)

s={}
print(s)
print(type(s))#dictionary

s={1,"kavitha",3.143,'A'}
print(s)
print(s[0])#we cant apply index in set
print(s[1])
print(s[2])
s={1,2,3,4,5,1,2}
print(s)

s={1,2,3,4,5,6,7}
print(s)
s.add(100)
print(s)
s.discard(100)
print(s)

s={1,2,3,4,5,6,7,1,2,3}
print(s)
//---dictonary---//
d={}
print(d)
print(type(d))
d={1,2,3,4,5}
print(d)
print(type(d))

d={1:"sai",2:"ram",3:"sree",4:"mohan"}
print(d)
print(type(d))

d={1:"sai",2:"ram",3:"sree",4:"sree"}
print(d)
print(type(d))

d={1:"sai",1:"ram",3:"sree",4:"sree"}
print(d)
print(type(d))

r=range(10)
print(r)
print(type(r))
print(list(r))

r=range(2,30)
print(r)
print(type(r))
print(list(r))

r=range(2,30,3)
print(r)
print(type(r))
print(list(r))
print(set(r))
print(tuple(r))

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3%2)
print(3**2)
print(3//2)

print(3<2)# it wii give boolean output true or false
print(3>2)
print(3<=2)
print(3>=2)
print(3==2)
print(3!=2)

a=5#assignment operator
print(a)
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a**=2
print(a)
a/=2
print(a)
a%=2
print(a)

print(2<3 and 4<6)
print(2>3 and 4<6)
print(2<3 and 4>6)
print(2>3 and 4>6)

print(2<3 or 4<6)
print(2>3 or 4<6)
print(2<3 or 4>6)
print(2>3 or 4>6)

print(not(3<5))
print(not(3>5))

m=[1,2,3,4,5]
print(1 in m)
print(10 in m)
print(1 not in m)
print(10 not in m)
print('a' in "apple")
print('k' in "apple")
print('c'  not  in "apple")


a=2
b=2
print(id(a))
print(id(b))
print(a is  b)
print(a is not  b)

a=2
b=4
print(id(a))
print(id(b))
print(a is  b)
print(a is not  b)

a="kavitha"
b="kavitha"
print(id(a))
print(id(b))
print(a is  b)
print(a is not  b)

a="kavitha"
b="Kavitha"
print(id(a))
print(id(b))
print(a is  b)
print(a is not  b)

a=8
b=2
c=3
print(bin(a))
print(bin(b))
print(bin(c))
print(bin(a&c))
print(a&c)
print(bin(a|c))
print(a|c)
print(bin(a^c))
print(a^c)

a=1
print(~a)

print(a<<2)
print(a>>2)

i=int(input("enter a  number:"))
j=int(input("enter a number:"))
if i>j:
    print(i,"is a big")
else:
    print(j,"is a big")

i=int(input("enter a  number:"))
if i>20:
    print(i,"is greater than 20")
else:
    if(i>15):
        print(i,"is a greater than 15")
    else:
        print(i,"is less than 15")
        

i=int(input("enter a number:"))
if (i==1):
    print("one")#if we give 1,2,3 & it executes else block ,so we prefer elif condition also
if (i==2):
    print("two")
if (i==3):
    print("three")
if (i==4):
    print("four")#if we give 4 it will ,it give perfect op 
else:
    print("invalid input")
    
    
i=int(input("enter a number:"))
if (i==1):
    print("one")   
elif (i==2):
    print("two")
elif (i==3):
    print("three")
elif (i==4):
    print("four")        
else:
    print("invalid input")
      
l=[1,2,"hello",'A']
for i in l:
    print(i)
    print(type(i))



for i in range(2,21):
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")
        
n=int(input("enter a number:"))
sum=0
for i in range(n):
    sum=sum+i
print("sum =",sum)


numlist=[1,2,3]
charlist=['a','b','c']
for n in numlist:
    print(n)
for c in charlist:
    print(c)

numlist=[1,2,3]
charlist=['a','b','c']
for n in numlist:
    print(n)
    for c in charlist:
        print(c)
i=1
while i<=10:
    print(i,end=" ")
    i+=1


n=int(input("enter a number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
i=i+1
print("sum=",sum,end=" ")'''


