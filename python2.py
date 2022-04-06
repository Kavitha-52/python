Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,3]
id(a)
2118192860416
a[1]=10
print(a)
[1, 10, 3]
id(a)
2118192860416
a=[1,2,3]
a=a+[4,5]
print(a)
[1, 2, 3, 4, 5]
a=[1,"hii",10.5]
print(a)
[1, 'hii', 10.5]
a=[1,2,3]
p[rint(a)
  print(a)
  
SyntaxError: '[' was never closed
a=[1,2,3]
  
a=[1,2,3]
  
print(a)
  
[1, 2, 3]
print(len[1,2,3])
  
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(len[1,2,3])
TypeError: 'builtin_function_or_method' object is not subscriptable
a=[1,2,3,4,5]
  
a(0)
  
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a(0)
TypeError: 'list' object is not callable
a[0]
  
1
a[2]
  
3
a=[10,20,[1,2,3],30]
  
pint(a)
  
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pint(a)
NameError: name 'pint' is not defined. Did you mean: 'print'?
print(a)
  
[10, 20, [1, 2, 3], 30]
a[2]
  
[1, 2, 3]
s=['p','y','t','h','o','n']
  
s[1:4]
  
['y', 't', 'h']
s[-4:2]
  
[]
s[-4:-2]
  
['t', 'h']
a=[1,2,3]
  
a.append(4)
  
print(a)
  
[1, 2, 3, 4]
a=[1,2,3]
  
b=[4,5,6]
  
a.etnd(b)
  
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.etnd(b)
AttributeError: 'list' object has no attribute 'etnd'. Did you mean: 'extend'?
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
a=[50,20,40,10,30,10,20]]
SyntaxError: unmatched ']'
a=[50,20,30,10,60,40]
a.sort()
print(a)
[10, 20, 30, 40, 50, 60]
a=[10,20,30,40,50]
a.reverse()
print(a)
[50, 40, 30, 20, 10]
a=[1,2,3]
b=a
c=a.copy()
print(c)
[1, 2, 3]
print(b)
[1, 2, 3]
s="abcdef"
print(list(s))
['a', 'b', 'c', 'd', 'e', 'f']
a=[1,89,54,679,4,-9]
print(max(a))
679
a=[1,2,3,4,5,6,-987,-7]
print(min(a))
-987
a=[1,2,3,4,5]
print(sum(a))
15
tup=10,12.45,
"pythonn",10
('pythonn', 10)
tup=10,12.45,"python",45
abcd=tup
print(a)
[1, 2, 3, 4, 5]
tup=10,12.34,"pythoun",30
a,b,c,d=tup
print(a)
10
print(b)
12.34
print(c)
pythoun
print(d)
30
a=(1,2,3)
a=a+(4,5)
print(a)
(1, 2, 3, 4, 5)
a=(1,2,3,4)a(0)
SyntaxError: invalid syntax
a=(1,2,3,4)
a(0)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a(0)
TypeError: 'tuple' object is not callable
a[0]
1
a[1]
2
a[3]
4
a=(1,2,[10,20,30],6)
print(a)
(1, 2, [10, 20, 30], 6)
a[2]
[10, 20, 30]
a[2][1]
20
a=(1,2,3)a[1
           
SyntaxError: '[' was never closed

a=(1,2,3)
           
a[1]
           
2
a=(1,2,3,4)
           
print(len(a))
           
4
print(10,20)+(1,2)
           
10 20
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print(10,20)+(1,2)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'tuple'
print((10,20)+(1,2))
           
(10, 20, 1, 2)
print(3 in (1,2,3))
           
True
print(4 in(1,2,3))
           
False
for x in(1,2,3)
           
SyntaxError: expected ':'
for(x in (1,2,3):
    
SyntaxError: invalid syntax
print(x*x)
    
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print(x*x)
NameError: name 'x' is not defined
for( x in (1,2,3)):
    
SyntaxError: invalid syntax
for x in (1,2,3):
    print(x*x)

    
1
4
9
a=(1,2,3,4,1,3,1)
    
print(a.count(1))
    
3
a=(10,20,30,40)
    
print(a.indx(30)
print(a.index(30)
      
SyntaxError: '(' was never closed
print(a.index(30))
      
2
s="abcdf"
      
print(tuple(s))
      
('a', 'b', 'c', 'd', 'f')
a=(1,2,5,67)
      
print(max(a))
      
67
a=(1,3,6,89)
      
print(min(a))
      
1
a=(1,2,3,4,5,6,7,8,9)
      
print(sum(a))
      
45
