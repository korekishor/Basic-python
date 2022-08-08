# print( "The list printed sorting by age: ")

# print(sorted(lis, key=itemgetter('age')))


"""
l=[1,2,3]
l2=[5,6,8]
l.append(l2)
print(l)

l2[2]=999
print(l)


l=[1,2,3]
l2=[5,6,8]
l.extend(l2)
print(l)
l2[2]=999
print(l)

""""""
s=set()
print(type(s))

"""


"""
l=[1,2,3,3,4]
s=set(l)
l=list(s)
print(l)

"""
# ----------------------------------->>>>>>>>>>>>>>>>>>>>>>>•	Type Casting  - 
"""
list=[1,2,3,4,5]
s=set(list)
print(s)
t=tuple(list)
print(t)

"""
"""
set={1,2,3,"hi","hellow"}
l=list(set)
print(l)
t=tuple(set)
print(t)

"""
"""
t=(1,2,3,"hi","hellow")
s=set(t)
print(s)
l=list(t)
print(l)

"""



# oprators
"""
+ ==>Addition
- ==>Subtraction
* ==>Multiplication
/ ==>Division operator
% ===>Modulo operator
// ==>Floor Division operator
** ==>Exponent operator or power operator

"""



"""
a,b=12,32
print(a-b)
print(a+b)
print(a*b)
print(a/b)
 
print(a%b)
print(a//b)
print(a**2)

"""

# •	Decorators, generators - 
"""
print(9>9)
def change1(fun):
    def inner(a,b):
        print(a+b)
    return inner

def change2(fun):
    def inner(a,b):
        if a>b:
            print("this is addition :",a-b)
        else:
            fun(b,a)
    return inner

@change2
@change1
def sum(a,b):
    print("this is total sum",a+b)

sum(9,9)
"""
"""
# generators
def sum(a):
    while a!=10:
        a=a+1
        yield a

l=sum(2)
print("list",l)
print("type",type(l))
for i in l:
    print(i,end="-")
"""

"""
str='''a person who ask a question.. is a # % fool for.. 5 min person 1433'''
import re
match=re.findall('[^a-zA-Z0-9]',str)
print(match)

match=re.sub('\.','@',str)
print(match)

match=re.match('a',str)
print("match = ",match)

match=re.split('\s',str)
print(match)

match=re.findall('^a|3$',str)
print("start and end ",match)

match=re.findall('\d{2}',str)
print(match)

"""

# pynotifier,psutile



