Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Helloworld")
Helloworld

3+4
7

3-4
-1
_
-1
_*2
-2
for i in range(1,2):
    print("2","*",i"=",2*i)
2 * 1 = 2
for i in range(1,2 print("2","*",i,"=",2*i)
               
SyntaxError: expected ':'
for i in range(1,10):
    print("2","*",i,"=",2*i)

               
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
for i in range(1,11):
    print("2","*",i,"=",2*i)

               
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
s="hii"
               
s*3
               
'hiihiihii'
s.upper()
               
'HII'
s*3
               
'hiihiihii'
a=10
               
b=20
              
x=a+b
               
print(x)
               
30
a=b=c=5
               
print(a,b,c)
               
5 5 5
a,b,c,d=10,20.44,"thundersoft",'k'
               
print(a,b)
               
10 20.44
print(a,b,c,d)
               
10 20.44 thundersoft k
txt="my name is{fname},iam {age}yearsold.".format (fname="honey
                                                   
SyntaxError: unterminated string literal (detected at line 1)
txt="my name is{fname},iam {age}yearsold.".format(fname="honey",age=4)
                                                   
txt
                                                   
'my name ishoney,iam 4yearsold.'
txt="my name is {0},iam {1}yearsold.".format("honey",4)
                                                   
txt
                                                   
'my name is honey,iam 4yearsold.'
txt="my name is {},iam {}years old.".format("honey",4)
                                                   
txt
                                                   
'my name is honey,iam 4years old.'
a=12
                                                   
type(a)
                                                   
<class 'int'>
str="hello"
                                                   
type(str)
                                                   
<class 'str'>
a=1.34
                                                   
type(a)
                                                   
<class 'float'>
a='k'
                                                   
type(a)
                                                   
<class 'str'>
a=10
                                                   
float(a)
                                                   
10.0
a=1.2334
                                                   
int(a)
                                                   
1
comp=complex(2,4)
                                                   
print(comp)
                                                   
(2+4j)
int(comp)
                                                   
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(comp)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
s="123"
                                                   
int(s)
                                                   
123
f="1.234"
                                                   
int(f)
                                                   
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(f)
ValueError: invalid literal for int() with base 10: '1.234'
id(1)
                                                   
1861792497904
y=1
                                                   
id(y)
                                                   
1861792497904
y="hii"
                                                   
id(y)
                                                   
1861829899056
id(hii)
                                                   
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    id(hii)
NameError: name 'hii' is not defined
id("hii"

   )
                                                   
1861829899056
id('hii')
                                                   
1861829899056
id(3)
                                                   
1861792497968
id(1+2)
                                                   
1861792497968
id(1*3)
                                                   
1861792497968
id(4-1)
                                                   
1861792497968
id(6/2)
                                                   
1861828469392
id(1)
                                                   
1861792497904
id(2)
                                                   
1861792497936
id(3)
                                                   
1861792497968
id(1)+id(2)
                                                   
3723584995840
x=10
                                                   
y=x
                                                   
print(x is y)
                                                   
True
x=10
                                                   
def m1()
SyntaxError: expected ':'
def m1():
    a=10
    print(a)
    return
def m2():
    
SyntaxError: invalid syntax
def m1():
    a=10
    print(a)
    return

def m2():
    print(a)
    return

m1()
10
m2()
1.2334
def m1():
    a=10
    print(a)
    return

def m2()
    a=20
    print(a)
    return
SyntaxError: expected ':'
def m2()
    a=20
    print(a)
    returndef m1():
        a=10
        print(a)
        return
    
SyntaxError: expected ':'
def m1():
    a=10
    print(a)
    return

def m2():
    a=20
    print(a)
    return

m1()
10
m2()
20
def m1():
    a=10
    print(a)
    return

def m2(a):
    print(a)
    return

m1()
10
m2(20)
20
a=20
def test():
    global a
    a=a+10
    print(a)
    return

test()
30
print(a)
30
a=20
def test():
    #global a
    a=a+10
    return
SyntaxError: multiple statements found while compiling a single statement
5+3-2
6
3>3
False
3=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
3<5
True
1==true
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    1==true
NameError: name 'true' is not defined. Did you mean: 'True'?
0==false
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    0==false
NameError: name 'false' is not defined. Did you mean: 'False'?
1==True
True
0==False
True
25.00<=25.55
True
25.00>=25.55
False
25.00>=25.00
True
25.00<=25.00
True
x&y=0
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
x&y==0
False
x=1
y=5
x&y=0
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
x&y==0
False
x>0:
    
SyntaxError: invalid syntax
if x>0:
    print("x is +ve")

    
x is +ve
if x>0:
    print("x is +ve")
else:
    print("x is not +ve")

    
x is +ve
for letter in 'python':
    if letter=='h':

        pass
    print("pass:",letter)

    
pass: p
pass: y
pass: t
pass: h
pass: o
pass: n
for letter in 'python':
    if letter=='h':

        pass
    print("pass:",letter)

pass: p
pass: y
pass: t
pass: h
pass: o
pass: n
for letter in 'python':
    if letter=='h':

        pass
    print("pass:",letter)
print(letter)
SyntaxError: invalid syntax
defvariableArgs(*):
    
SyntaxError: invalid syntax
defvariableArgs(*a):
    
SyntaxError: invalid syntax
seq=[1,2,3,4,5,6]
new_seq=map(lambda x:x*2,seq)
print(list(new_seq))
[2, 4, 6, 8, 10, 12]
seq=[1,2,3,4,5,6]
new_seq=map(lambda x:x%2==0,seq)
print(list(new_seq))
SyntaxError: multiple statements found while compiling a single statement
seq=[1,2,3,4,5,6]
new_seq=map(lambda x:x%2==0,seq)
print(list(new_seq))
SyntaxError: multiple statements found while compiling a single statement
lang="python"
print("%s is easy to learn"%lang)
python is easy to learn
str1="hii"
print("str1:",id(str1))
str1: 1861829951024
name="hii"
age=6
\
age=6
print("%s age is %d"%(name,age))
hii age is 6
s="string"
print(s[1:4])
tri
dell(s)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    dell(s)
NameError: name 'dell' is not defined
a=[1,2,3]
id(a)
1861829988672
a[1]=10
print(a)
[1, 10, 3]
id(a)
1861829988672
a=[1,2,3]
a=a+[4,5]
print(a)
[1, 2, 3, 4, 5]
a=[1,"hii",10.5]
print(a)
[1, 'hii', 10.5]
a=[1,2,3]
print(len(a))
3
print(len(1,2,3))
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    print(len(1,2,3))
TypeError: len() takes exactly one argument (3 given)
a=[10,20,30,40]
a[0]
10
a[3]
40
a[2]
30
a=[10,20,[1,2,3],30]
print(a)
[10, 20, [1, 2, 3], 30]
a[1]
20
a[0]
10
a[2]
[1, 2, 3]
a[3]]
SyntaxError: unmatched ']'
a[3]
30
a[2[1]]
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    a[2[1]]
TypeError: 'int' object is not subscriptable
a[2][0]
1
a[2][1]
2
a[2][2]
3
print(len[10,20,30,40])
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    print(len[10,20,30,40])
TypeError: 'builtin_function_or_method' object is not subscriptable
print(len([10,20,30,40]))
4
print([10,20]+[15,25])
[10, 20, 15, 25]
print(['hii']*3)
['hii', 'hii', 'hii']
print(3 in [1,2,3])
True
print(3 in [1,2,4])
False
for x in[1,2,3]:
    print(x*x)

    
1
4
9
s=[1,2,3,4]
for i in s:
    print(i)

    
1
2
3
4
s=['p','y','t','h','o','n']
print("s[0] :",s[0])
s[0] : p
print("s[0] :",s[0])
print("s[1] :",s[1])
print("s[2] :",s[2])
print("s[3] :",s[3])
print("s[4] :",s[4])
print("s[5] :",s[5])
print("s[6] :",s[6])
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
print("s[1] :",s[1])
s[1] : y
print("s[0] :",s[0])

s[0] : p
print("s[-1] :",s[-1])
s[-1] : n
s=['p','y','t','h','o','n']
s[1:4]
['y', 't', 'h']
s[1:3]
['y', 't']
s=[10,20,30,[40,50],60,70,70]
s[1::2]
[20, [40, 50], 70]
s[1::3]
[20, 60]
a=[1,2,3]
a.append(4)
print(a)
[1, 2, 3, 4]
a.append(4,5)
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    a.append(4,5)
TypeError: list.append() takes exactly one argument (2 given)
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
[1, 2, 3, 4, 5, 6]
a=[10,20,30]
a.insert(1,40)
print(a)
[10, 40, 20, 30]
a=[10,20,30]
a.remove(30)
print(a)
[10, 20]
a.remove(30)
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    a.remove(30)
ValueError: list.remove(x): x not in list
a=[10,20,30]
a.pop()
30
a=[10,20,30]
a.clear()
print(a)
[]
a=[10,20,30,40]
a.index(20)
1
a=[10,20,30,40]
a.count(10)
1
a=[10,30,10,40,10]
a.count()
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a.count(10)
3
a=[7,8,3,5,2,1]
a.sort()
print(a)
[1, 2, 3, 5, 7, 8]
a=[1,2,3]
b=a
c=a.copy()
print(a)
[1, 2, 3]
print(c)
[1, 2, 3]
a=[1,0,1]
print(all(a))
False
a=[1,2,3]
print(all(a))
True
a=[1,0,1,0]
print(any(a))
True
a=[11,22,33]
print(list(enumerate(a)))
[(0, 11), (1, 22), (2, 33)]
print(list(enumerate(a,100)))
[(100, 11), (101, 22), (102, 33)]
a=[1,2,3,4]
print(len(a))
4
s="abcdef"
print(list(s))
['a', 'b', 'c', 'd', 'e', 'f']
a=[1,4,7,876,-9]
print(max(a))
876
a=[1,4,7,876,-9]
print(min(a))
SyntaxError: multiple statements found while compiling a single statement
a=[1,4,7,876,-9]
print(min(a))
SyntaxError: multiple statements found while compiling a single statement

a=[1,2,3,4,-38]
print(min(a))
-38
a=[1,2,3,4,5,6]
print(sum())
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    print(sum())
TypeError: sum() takes at least 1 positional argument (0 given)
a=[1,2,3,4,5,6]
print(sum(a))
SyntaxError: multiple statements found while compiling a single statement
a=[1,2,3,4,5]
print(sum(a))
15
tup=10,12.22,"python",'k'
a,b,c,d=tup
print(a)
10
print(tup)
(10, 12.22, 'python', 'k')
print(d)
k
print(c)
python
=(1,2,3)
SyntaxError: invalid syntax
a=(1,2,3)
a=a+(4,5)
print(a)
(1, 2, 3, 4, 5)
a=(1,2,3)
\
a=(1,2,3)
print(a)
(1, 2, 3)
a=(1,2,3,4,5,6)
print(a)
(1, 2, 3, 4, 5, 6)
print(len(a))
6
a=(1,2,3,4,5,6)
q[0]
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    q[0]
NameError: name 'q' is not defined
a[0]
1
a{5]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[5]
6
a[7]
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    a[7]
IndexError: tuple index out of range
a=(1,2,[3,4,5],9)
print(a)
(1, 2, [3, 4, 5], 9)
a[2]
[3, 4, 5]
a[1]
2
a[4]
Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    a[4]
IndexError: tuple index out of range
a[3]
9

s=(1,2,3,4)
for i in s:
    print(i)

    
1
2
3
4
s=('p','y','t','h','o','n')
print("s[0]:",s[0])
s[0]: p
print("s[-5]:",s[-5])
s[-5]: y

s=('p','y','t','h','o','n')
s[1:4]
('y', 't', 'h')

s[2:1]
()
s[2:3]
('t',)

print(10,20)+(1,2))
SyntaxError: unmatched ')'
print((10,20)+(1,2))
(10, 20, 1, 2)
print(("python")*2)
pythonpython
print(1 in(1,2,3,4))
True
print(5 in(1,2,3,4))
False
for x in(1,2,3)
SyntaxError: expected ':'
for x in(1,2,3)
SyntaxError: expected ':'
for x in(1,2,3):
    print(x*x)

    
1
4
9
a=(10,10,20,20,10,30)
print(a.index(10)

      )
0
print(a.count(10))
3
print(a.count(10,20))
Traceback (most recent call last):
  File "<pyshell#346>", line 1, in <module>
    print(a.count(10,20))
TypeError: tuple.count() takes exactly one argument (2 given)
print(a.count(20))
2

a=(1,2,3)
print(all(a))
True
a=(1,2,3,0)
print(all(a))
False
a=(1,2,3)
print(any(a))
SyntaxError: multiple statements found while compiling a single statement
a=(1,2,3,4,5)
print(any(a))
True
a=(1,2,3,4,5,0)
print(any(a))
True
a=(10,20,30)
print(list(enumarated(a)))
Traceback (most recent call last):
  File "<pyshell#359>", line 1, in <module>
    print(list(enumarated(a)))
NameError: name 'enumarated' is not defined. Did you mean: 'enumerate'?
a=(10,20,30)
print(list(enumarate(a)))
SyntaxError: multiple statements found while compiling a single statement
a=(11,22,33)
print(list(enumarate(a)))
Traceback (most recent call last):
  File "<pyshell#362>", line 1, in <module>
    print(list(enumarate(a)))
NameError: name 'enumarate' is not defined. Did you mean: 'enumerate'?
a=(11,22,33)
print(list(enumerate(a)))
SyntaxError: multiple statements found while compiling a single statement
s={"c","c++","jvaa"}
s.add("python")
print(s)
{'jvaa', 'python', 'c++', 'c'}
s={"c","c++","jvaa"}
s.add("python")
print(s)
SyntaxError: multiple statements found while compiling a single statement
a=(11,12,13,14)
print(list(enumerate(a))

 print(list(enumerate(a)))
      
SyntaxError: '(' was never closed
a=(11,12,13,14)
      
print(list(enumerate(a)))
      
[(0, 11), (1, 12), (2, 13), (3, 14)]
s="abcdef"
      
print(tuple(s))
      
('a', 'b', 'c', 'd', 'e', 'f')
s={"c","c++","python"}
      
t=s.discard("c")
      
print(t)
      
None
print(s)
      
{'python', 'c++'}
x={"c","c++","java"}
      
y={"python","c","c++",}
      
=x.intersection(y)
      
SyntaxError: invalid syntax
z=x.intersection(y)
      
print(z)
      
{'c++', 'c'}
z=x.isdisjoint(y)
      
print(z)
      
False
z=x.issubset(y)
      
print(z)
      
False
z=x.issubset(y)
      
print(z)
      
False
z=y.pop()
      
print(z)
      
python
z=y.remove("c")
      
print(z)
      
None
print(y)
      
{'c++'}
x={"c","c++","java"}
      
y={"python","c","c++"}
      
z=x.symmetric_difference(y)
      
print(z)
      
{'python', 'java'}
z=x.symmetric_difference_update(y)
      
print(x)
      
{'python', 'java'}
z=x.union(y)
      
print(z)
      
{'c++', 'c', 'python', 'java'}
z=x.union(y)
      
print(z)
      
{'c++', 'c', 'python', 'java'}
z=y.update(x)
      
print(z)
      
None
print(y)
      
{'c++', 'c', 'python', 'java'}
s={10,20,30,40}
      
all(s)
      
True
s={10,20,30,40}
      
any(s)
      
True
s={0,0,0}
      
any(s)
      
False
all(s)
      
False
s={1,2,3,4,5}
      
list(s)
      
[1, 2, 3, 4, 5]
s={1,2,3,4,5}
      
max(s)
      
SyntaxError: multiple statements found while compiling a single statement
s={1,2,345,78}
      
max(s)
      
345
s={1,2,5,-9}
      
min(s)
      
-9
sum={-1,-2,3}
      
sum(sum)
      
Traceback (most recent call last):
  File "<pyshell#424>", line 1, in <module>
    sum(sum)
TypeError: 'set' object is not callable
s={-1,-2,3}
      
sum(s)
      
Traceback (most recent call last):
  File "<pyshell#426>", line 1, in <module>
    sum(s)
TypeError: 'set' object is not callable
s={1,2,3,-4}
      
sum(s)
      
Traceback (most recent call last):
  File "<pyshell#428>", line 1, in <module>
    sum(s)
TypeError: 'set' object is not callable
