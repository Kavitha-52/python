Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10
20 20 20

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10
20 20 20
30 20 20

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10
20 20 20
30 20 20
20 20 30

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10
20 20 20
30 20 20
20 20 30
70

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
hiihello

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
hiihello
10

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
hiihello
welcome

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
hiihello
welcome
10 20.222 thundersoft TS

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10 20.222 thundersoft TS
TS thundersoft 20.222 10
TS thundersoft 20.222 10
txt="my name is{},i am{}years old.".format{"sree",5}
SyntaxError: invalid syntax

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
a=20
type(a)
<class 'int'>
a=1.2334
type(a)
<class 'float'>
str="thundersoft"
type(str)
<class 'str'>

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
a=10
float(a)
10.0
a=20.333
int(a)
20
comcomplex(1,2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    comcomplex(1,2)
NameError: name 'comcomplex' is not defined. Did you mean: 'complex'?
comp=complex(1,2)
print(comp)
(1+2j)
a=2
id(a)
2061699252496
id(1+1)
2061699252496
id(1*1)
2061699252464
id(1*2)
2061699252496
id(3-1)
2061699252496
id(1)-id(2)
-32
id(1)-id(3)
-64
id(-1)-id(-2)
32
id(2)=id(3)
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
id(2)-id(3)
-32
id(a)
2061699252496
id(hii)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    id(hii)
NameError: name 'hii' is not defined
id(h)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    id(h)
NameError: name 'h' is not defined
id(1.2)
2061735025552
id("hii"
id("hii")
   
SyntaxError: '(' was never closed
id('q')
   
2061700589936
id("hii")
   
2061736233328
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

def m1():
    a=1
    print(a)
    return
def m2():
    
SyntaxError: invalid syntax

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10
20

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10
Traceback (most recent call last):
  File "C:/Users/Dell/Desktop/.py", line 39, in <module>
    m2()
  File "C:/Users/Dell/Desktop/.py", line 36, in m2
    print(a)
NameError: name 'a' is not defined

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
10
20

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
Traceback (most recent call last):
  File "C:/Users/Dell/Desktop/.py", line 46, in <module>
    test()
NameError: name 'test' is not defined

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
30
30

====================== RESTART: C:/Users/Dell/Desktop/.py ======================
Traceback (most recent call last):
  File "C:/Users/Dell/Desktop/.py", line 53, in <module>
    test()
  File "C:/Users/Dell/Desktop/.py", line 50, in test
    a=a+10  #it gives error
UnboundLocalError: local variable 'a' referenced before assignment
2+3
5
2-3
-1
2*2
4
2/2
1.0
4%@
SyntaxError: invalid syntax
4%2
0
(2+2)*4
16
'a'*3
'aaa'
5<1
False
5>5
False
5>1
True
2=int(2.33)
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
2==int(2.33)
True
2==float(1.33)
False
2.0==float(2)
True
5>3 and 5!=5
False
5>3==5==5
False
5>3 and 5==5
True
5>1 or 51=5
SyntaxError: cannot assign to expression
5>1 or 5!=5
True
not true
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not 3!=3
True
not 2==2
False
a=1
b=2
list=[1,2,3,4,5]
if(a in list):
    print("a is available in given list")
else
SyntaxError: expected ':'
else:
    
SyntaxError: invalid syntax
a=1
b=10
list=[1,2,3,4]
if( a in list):
    print("a is available in list")
else:
    print("a is not available in list")

    
a is available in list



'1'+'2'
'12'
'hii'+'hello'
'hiihello'
day=input()

day=input()
sunday
print(day)
sunday
if x>0:
    print("x is +ve")
    x

    
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    if x>0:
NameError: name 'x' is not defined
