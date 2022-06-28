#using decorator we can change behaviour of function
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)#it will return new values
    return inner
    
div=smart_div(div)
div(2,4)
        
