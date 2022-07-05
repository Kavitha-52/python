'''="abcdefgh"
for i in range(0,len(input),1):
    input=input[:i]+input[i].upper()+input[i+1:]
print(input)
for i in range(0,5):
    for j in range(0,5):
        print("*",end=" ")
    print()#it will goes to next line
    
n=int(input("enter a number:"))
for i in range(0,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=int(input("enter a number:"))
for i in range(0,n+1):
    for j in range(j):
        print("*",end=" ")
    print()

#another method

n=int(input("enter a number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("enter a number:"))
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

def fun(n):
    
    #n=int(input("enter a number:"))
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print()
fun(5)
i=0
while(i <= 10):
    print (i, end = '  ')
    i = i+1
    
n=int(input("enter number"))
if(n%2==0):
    print(n," is even")
else:
    print(n," is odd")
    
count=10
while(count>0):
    print(count)
    count=count-1
    
import keyword
print(keyword.kwlist)

l=['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
for i in range(0,len(l)):
    print(i)

l=['a','e','i','o','u']
if(l==a):
    print("vowel")
else:
    print("not vowel")

print("Enter the Character: ")
c = input()

if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
    print("\nIt is a Vowel")
elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    print("\nIt is a Vowel")
else:
    print("\nIt is a Consonant")

#print(dir(str))
print(dir(list))
print(dir(tuple))  
print(dir(set))
print(dir(dict))

#functions
def square(n):
    print("sqaure is :",n*n)
square(5)
    
def square(n):
    print("sqaure is :",n*n)
square(n=int(input("enter a number:")))

n=int(input("enter a numberr:"))
def square(n):
    print("sqaure is :",n*n)
square(n)

def even(n):
    if(n%2==0):
        print(n, "is even")
    else:
        print(n,"is odd"
 
even(n=int(input("enter e number"))

#functions with 2 paramenters
def fun(a,b):
    if(a>b):
        print(a,"is big")
    else:
        print(b, "is big")
fun(10,20)

def add(a,b):
    print("sum is:",a+b)
add(10,20)
add(1.5,1.5)
add("sai","ram")

#function with return
def add(a,b):
    return a+b
x=add(10,20)
print("sum is :",x)

def add(a,b):
    return a+b
print("sum is :",add(10,20))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
print("sum is :",add(10,20))
print("sub is :",sub(10,20))
print("mul is :",mul(10,20))
print("div is :",div(10,20))
print("mod is :",mod(10,20))

def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(10,20)
print("sum is :",x)
print("sub is :",y)

#local variable

def f1():
    a=10
    print(a)
def f2():
    a=10
    print(a)
f1()
f2()
# global varaible
a=10
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()

a=10
def f1():
    a=20
    print(a)
def f2():
    print(a)
f1()
f2()

a=10
def f1():
    global a # we modify the global variable 
    a=20
    print(a)
def f2():
    print(a)
f1()
f2()

a=10
def f1():
    global a
    a=20
    print(a)
def f2():
    print(a)
f2()
f1()

#positional argument
def f1(a,b):
    print("sub is :",a-b)
f1(20,10)
f1(10,20)

#keyword argument
def fun(name,msg):
    print("hello:",name,msg)
fun(name="ramu",msg="good evening")
fun(msg="good evening",name="ramu",)

#default argument

def f1(course):
    print("course is :",course)
f1("c")

def f1(course="python"):
    print("course is :",course)
f1()

#variable length arguments

def f1(a):
    print(a)
f1(10)

def f1(*a):
    print(a)
f1(10)
f1(10,20)
f1(10,20,30)
f1(10,20,30,40)

def add(*arg):
    s=0
    for i in arg:
        s=s+i
    print("sum is :",s)
add(10,1)
add(10,20)
add(10,20,30)
add(10,20,30,40)


def f1(**n):
    for k,v in n.items():
        print(k,"=",v)
f1(a=10,b=20,c=30)
f1(eid=123,ename="sai",eaddress="hyd",salary=45000)
f1(name="durga")

#positional only arguments
def add(a,b,/):
    print("result is :",a+b)
add(10,20)
#add(a=10,b=20)---> it gives error

#keyword only arguments:-
def add(*,a,b):
    print("result is :",a+b)
#add(10,20)
add(a=10,b=20)

def f1():
    print("hello")
del f1
f1()#it will give error

def f1():
    print("hello")
def f2():
    print("hii")
f1()
f2()

def f1():
    print("hello")
    def f2():
        print("hai")
    f2()
f1()

def f1():
    print("hello")
    def f2():
        print("hai")
        def f3():
            print("welcome")
        f3()
    f2()
f1()'''






 
