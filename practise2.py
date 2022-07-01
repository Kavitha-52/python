###----STRING-----###
'''s="thundersoft"
print(s)
print(type(s))

#----string indexing----#
print(s[0])
print(s[1])
print(s[-1])
print(s[-2])
print(len(s))

#---slicing----#
print(s[0:11])
print(s[:7])
print(s[1:])
print(s[:])
print(s[-4:-2])
print(s[-2:-4])#we cant give like this we give higher value in right
print(s[0:11:2])
print(s[::1])
print(s[::-1])

#----string concatination----#
s1="thunder"
s2="soft"
s3=s1+s2
print(s3)
print(s3*3)#string multipliaction

#----string split---#
s="python is very easy"
print(s)#python is very easy
s.split(" ")
print(s)#python is very easy
print(type(s))#<class 'str'>
s1=s.split(" ")
print(s1)#['python', 'is', 'very', 'easy']
print(type(s1))#<class 'list'>

for i in s1: # it print word by word
    print(i)

s1=s.split(" ",1)
for i in s1:
    print(i)


s1=s.split(" ",2)
for i in s1:
    print(i)
    
s="comparing other language python is very easy"
s1=s.split(" ",3)
for i in s1:
    print(i)

s="comparing other language python is very easy"
s1=s.split(" ")#it splits all words in string
for i in s1:
    print(i)

s="comparing other language python is very easy"
s1=s.split("is")#it splits all words in string
for i in s1:
    print(i)

s="comparing is other language python is very easy"
s1=s.split("is")#it splits when is comes  in string
for i in s1:
    print(i)


s="comparing other language python is very easy"
s1=s.split("a")#it splits when a comes in string
for i in s1:
    print(i)

s="m,o,h,a,n"
print(s)
s1=s.split(",",2)
for i in s1:
    print(i)
    
#----string capitalize ----#

s="python is easy"
print(s)
print(s.capitalize())#python Is Easy
s="python Is Easy"
print(s)
print(s.capitalize())#Python is easy

#---string title----#
s="python is easy"
print(s.capitalize())#Python is easy
print(s.title())#Python Is Easy

#----upper & lower----
s="python"
print(s.upper())#PYTHON
print(s.lower())#python

#----swap function---
s="PYthon PRograMMing"
print(s)#PYthon PRograMMing
print(s.swapcase())#pyTHON prOGRAmmING


#---string count----
s="python is very easy"
print(s.count(" "))# 3--spaces

print(s.count("a"))# a
print(s.count("x"))#0
print(s.count("y"))#3
substring="is"
print(s.count(substring))#1
#---- string  replace---
s="python is easy"
print(s.replace("python","java"))
   
s='''python is easy
    python is easy
    python is easy'''
print(s.replace("python","java"))

#---join string---
print(" ".join("sai"))
print(":".join("sai"))

#---strip----
s="  durga  "
print(s.strip())#space removed in both sides
print(s.lstrip())#left side space removd
print(s.rstrip())#right side space removd

s="adurga"
print(s)
print(s.lstrip("a"))#it removes left side a
print(s.rstrip("a"))#it removes right side a

#---length---
s="thundersoft"
print(len(s))#11

#--- find----
s="python is easy is"
print(s.find("is")) # 7 it takes 1st occurance is

print(s.find("p"))#0
print(s.find("x"))#-1

#----index----
print(s.index("is"))#7
print(s.find("is"))#7
print(s.index("x"))#it gives error
print(s.find("x"))# it wont give any error


#---rindex---
s="python language is  very easy is "
print(s.rindex(" "))

print(s.rindex("is"))#return highest index


#--- min & max---
s="pineapple"
print(max(s))
print(min(s))

s="Pineapple"
print(max(s))
print(min(s))

#--startswith() & endswith()---
s="pine apple"
print(s.startswith('p'))
print(s.startswith('a'))
print(s.endswith('e'))
print(s.endswith('p'))
print(s.endswith(''))

#---isdigit---
s="12345"
print(s.isdigit())

s="123 45"
print(s.isdigit())

s="123abc45"
print(s.isdigit())

#---isaplha---
5
s="abcds"
print(s.isalpha())

s="ab cds"
print(s.isalpha())

s="123abcds"
print(s.isalpha())

#---isalnum--#

s="acvbcb"
print(s.isalnum())

s="acvbcb123"
print(s.isalnum())

s="12343"
print(s.isalnum())

s="acvb cb"
print(s.isalnum())

s="a123 4"
print(s.isalnum())

###---LIST----###

l=[]
print(l)
print(type(l))

l=[10,20,"sai",1.123]
print(l[0])
print(l[1])
print(l[3])
print(l[4])
print(l[5])#it gives error

#---slicing---#
l=[10,20,"sai",1.123,'a',12]
print(l[1:4])
print(l[:])
print(l[0:1])

#---nestedlist---#
l=[10,20,"sai",[1.123,'n',45],'a',12]

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[3][0])
print(l[3][1])
print(l[3][2])
print(l[4])
print(l[5])
print(l[-1])
print(l[-2])
print(l[-3])
print(l[-4])
print(l[3][-3])
print(l[3][-2])
print(l[3][-1])

#---append & extend---#
l=[1,2,3,4,5]
print(l)
l.append("hello")
print(l)
l.extend([10,20,30,"mango"])
print(l)

#---insert & remove--#
l=[1,2,3,4,5]
print(l)
l.insert(1,100)
print(l)
l.append(50)
print(l)
#l.append(0,50)-->it gives error
l.remove(100)
print(l)
#l.remove(20)--->gives error
print(l)

#----pop() clear &del---#
l=[1,2,3,4,5]
print(l)
l.pop(3)#poped based on index
print(l)

l.clear()
print(l)

l=[10,20,3.798,"hii"]
print(l)
del l#--->list deleted

#---concatination & multiplication--#
l1=[1,2,3]
l2=["apple","mango","banana"]
print(l1+l2)
print(l1*2)
print(l2*3)

#---list sort---#
l=[9,1,7,20,67,3,23]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

#---copy---#
l=[1,2,3,4,5,6]
l1=l
print(l)
print(l1)

#---list count---#
l=[1,2,3,4,5,1,6,1,7,8]
print(l.count(1))
print(l.count(4))
print(l.index(2))
print(l.index(1))
#print(l.index(10))--->error'''




