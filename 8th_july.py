'''t=(1,2,3,4,'a',12.123,"apple")
print(t)
print(type(t))
#count

a=(1,2,3,4,5,67,1,2,1)
l=a.count(2)
print(l)
print(a.count(1))

a=(1,2,3,4,5,67,1,2,1)
#print(a.count(1,2))--->error


data = (2,4,6,8,10) 
print(data)   
count = data.count(2)  
print("Occurences:",count)

data = (2,4,6,8,10,2)  
print(data)  
count = data.count(2)  
print("Occurences:",count)

#index

t=(1,2,3,4,5,6,7,2,1,2)
s=t.index(6)
print(s)
print(t.index(1))
#print(t.index(10))-->error

t=(1,2,3,4,5,6,7,2,1,'a','a',"hii")
s=t.index("hii")
print(s)
s=t.index('a')
print(s)

# functions in tuple
a=(1,2,3,2,"hello")
print(all(a))

a=(1,2,3,2,0)
print(all(a))

a=(1,2,3,2,'a',"qwe")
print(any(a))

a=(1,2,3,2,0,1)
print(any(a))

a=(0,0,0)
print(all(a))

a=(10,20,30)
print(list(enumerate(a)))


a=(10,20,30,'a')
print(list(enumerate(a)))

a=(10,20,30)
print(list(enumerate(a,100)))

a=(10,20,30)
print(len(a))

s="hello"
print(tuple(s))

a=(10,20,30,40)
print(max(a))

a=(10,20,30,121)
print(min(a))

a=(10,20,30,121,'a',"hello")
#print(min(a))--> error

a=(101,20,30,1,121)
print(sum(a))

print(sorted(a))

a=(101,20,30,1,121,'a',"hello")
print(sorted(a))-->error

t=(2)
print(t)
print(type(t))

t=(2,)
print(t)
print(type(t))

a=1
b=2
c=3
d="hii"
s=a,b,c,d
print(s)

t=(1,2,3,4,5)
a,b,c,d,e=t
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
print("e=",e)

t=(1,2,3,("hii",'A'),0,1.21,('s',"mango"))
print(t.index(1))
print(t.index(2))
print(t.index(3))
print(len(t))
print(t.index("hii"))-->error
print(t.index('A'))
print(t.index(0))
print(t.index(1.21))
print(t.index("mango"))

a=(1,2,3)
a=a+(4,6)
print(a)
b=a+('a','b','c')
print(b)

a=(1,2,3,4,5)
print(a[0])
print(a[4])
print(a[2])

s=('p','y','t','h','o','n')
print(s[1:4])
print(s[0:7:2])
print(s[::-1])

#list
l=[]
print(l)
print(type(l))

l=[1,2,3,4,5,'a',"hii","hello"]
print(l[0])
print(l[5])
print(l[7])
print(l[10])-->index error

l=[1,2,3,4,5,['a',"hii"],"hello"]
print(l[0])
print(l[5])
print(l[6])
print(l[5][0])
print(l[5][1])

l=[1,2,3,4,5]
print(l)

l.insert(5,100)
print(l)
x=l.insert(1,50)
print(x)
print(l.insert(1,500))
print(l)

l=[1,2,3,4,5]
l.append(10)
print(l)
l.extend(['a','b','c'])
print(l)

l=[1,2,3,4,5]
print(l.append(10))
a=l.append(10)
print(a)
b=l.extend(['a','b','c'])
print(b)


l=[1,2,3,4]
l.remove(1)
print(l)
print(l.remove(2))

l=[1,2,3,4]
l.pop(3)
print(l)
a=l.pop(0)
print(a)
print(l)
print(l.pop(1))
print(l)

l=[1,2,3,4,5]
l.clear()
print(l)

l=[1,2,3,4,5]
del l-->delete list
print(l)

l=[1,2,3,4]
l[0]=10
print(l)

l1=[1,2,3]
l2=['a','b']
print(l1+l2)
print(l1*3,l2*3)

l=[1,2,3,12,78.89]
l.sort()
print(l)

l=[1,2,3,4,5,6,3,21]
print(l)
l1=1
print(l1)
print(l)
l[0]=50
print(l)
print(l1)
print(id(l))
print(id(l1))

l=[1,2,3,4]
l2=l.copy()
print(l)
print(l2)
l.remove(3)
print(l)
print(l2)

l=[1,2,3,1,2,1,21]
#l.count(2)-->error
#print(l)
print(l.count(21))'''

#functions in list
l=[1,2,3,1,2,1,21]
print(len(l))
print(max(l))
print(min(l))
s=[1,2,3,0]
print(all(l))
print(all(s))
print(any(l))
print(any(s))
print(sum(s))





