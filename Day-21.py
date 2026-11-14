'''
Functions--> A reusable block of code which performs a task...

def fname(parameters): #fun defn-> formal arguments
    """Doc dtring"""
    statement(s)...
    return value(s)...
fname(arg) #actual arguments

Position Arguments--> count of argumnets to be matched
Default Arguments--> we can  make arguments as default
Keyword Arguments-->order/keyword ane to matched
Varible Lenght arguments (*arg)--> we can pass any number of postnl arguments
Keyword Varible lenght arguments (**kargs)-->we can pass any number of keyword arguments


#Positional arguments---> count of arguments to be matched

def data(a,b,c):
    """ function to perform arthmetic operation"""
    d=a+b+c
    e=a-b-c
    f=a*b*c
    g=a/b/c
    return d,e,f,g
#print(data(9,9,9))
# print(data(7,9)) Typeerror no_of arguments should be match
# print(data(8,2,3,5,56))  TypeError: data() takes 3 positional arguments but 5 were given
d,e,f=map(int,input("enter 3 values : ").split())
result=data(d,e,f)
print(f'result is {result}')

#Default arguments --> we can arguments as default

def data(a,b=5,c=2):  #non default arguments always first,next default arguments
    """ function to perform arthmetic operation"""
    d=a+b+c
    e=a-b-c
    f=a*b*c
    g=a/b/c
    return d,e,f,g
print(data(22,3,45))  #if a arguments has default give more priority then default values
print(data(28)) #here we no need to mentions other arguments
print(data(2,3))#here one default argument taken
print(data()) #here we should pass the atleast 1 argument

#keyword arguments --> Keyword name to be matched
#Grocary Purchase
#def grocary(item='bread',price): #non default arguments always first,next default arguments 
#def grocary(item,price=78): it is the correct way
def grocary(item,price):
    """ Use of Keyword arguments"""
    print(f'Item is {item}')
    print(f'Value of item is {price}')
grocary('milk',32)
# grocery(89,'Bread') in this case the order differs result changes
grocary(price=29,item='Bread')
#grocary(price=[28,82,38] item=['bread','jam','cream']) it dos't take multiple values
'''
#varible lenght arguments--> we can capture any number of positional arguments,we use (*args), captures
# excess potional arguments and pack them into tuple.

'''
def sample(*a):
    """ Use of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(28,33,2)
'''














