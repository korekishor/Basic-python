

"""

def outer_div(func):  
    def inner(x,y):  
        if(x<y):  
           x,y = y,x  
           return func(x,y)  
    return inner  
# syntax of generator  
@outer_div  
def divide(x,y): 
    print("---") 
    print(x/y)  


divide(12,22)

"""
 

"""
def decor1(func):
    def inner():
        print("++++++++++++")
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        print("-------------")
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print(num())

"""

"""
def decor(func): 
    def inner(name): 
        if name=="Sunny": 
            print("Hello Sunny Bad Morning") 
        else: 
            func(name) 
    return inner 

@decor 
def wish(name): 
    print("Hello",name,"Good Morning") 
 
wish("Durga") 
wish("Ravi") 
wish("Sunny") 

"""

"""
def decor(func): 
    def inner(name): 
        print("First Decor(decor) Function Execution") 
        func(name) 
    return inner 
 
def decor1(func): 
    def inner(name): 
        print("Second Decor(decor1) Execution") 
        func(name) 
    return inner 

@decor1 
@decor 
def wish(name): 
    print("Hello",name,"Good Morning") 
 
wish("Vikas") 
"""


