#Dictionary
dict={"A":"Apple","A":"Aeroplane"}
print(dict)
{'A': 'Aeroplane'}
dict={"A":"Apple","a":"Aeroplane"}
print(dict)
{'A': 'Apple', 'a': 'Aeroplane'}
dict={"Apple":"A","Aeroplane":"a"}
KeyboardInterrupt
print(dict)
{'Apple': 'A', 'Aeroplane': 'a'}
dict={"Apple":"A","Aeroplane":"a"}
print(dict)
{'Apple': 'A', 'Aeroplane': 'a'}
d={1:"one"}
print(d)
{1: 'one'}
d.clear()
print(d)
{}
d={"one":1}
print(d)
{'one': 1}
d={1:"one"}
x=d.copy()
print(x)
{1: 'one'}
d={1:"one",2:"two",3:"three"}
x=d.fromkeys(d)
print(x)
{1: None, 2: None, 3: None}
d={'A','Ant','B':'Bat','C':'cat'}
SyntaxError: invalid syntax
d={'A':'Ant','B':'Bat','C':'cat'}
x=d.get('B')
print(x)
Bat
d={'A':'Ant','B':'Bat','C':'Cat'}
x=d.items()
x
dict_items([('A', 'Ant'), ('B', 'Bat'), ('C', 'Cat')])
d={'A':'Ant','B':'Bat','C':'Cat'}
x=d.keys()
x
dict_keys(['A', 'B', 'C'])
d={'A':'Ant','B':'Bat','c':'cat'}
x=d.pop('B')
x
'Bat'
d={'A':'Ant','B':'Bat','c':'cat'}
d.popitem()
('c', 'cat')
d={'A':'Ant'}
x=d.setdefault('B',"bat")
d
{'A': 'Ant', 'B': 'bat'}
x
'bat'
d={'A':'Ant','B':'Bat'}
x={'c':'cat'}
x
{'c': 'cat'}
d.update(x)
d
{'A': 'Ant', 'B': 'Bat', 'c': 'cat'}
d={'A':'Ant','B':'Bat'}
d.values()
dict_values(['Ant', 'Bat'])
