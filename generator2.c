def mygen():
     yield 1# it makes function as generator
     yield 2
     yield 3
     yield 4
     yield 5
g=mygen()
print(type(g))# it give type
print(g)#it print in format
print(g.__next__())
for i in g:
    print(i)
