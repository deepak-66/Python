'''
Python was work with OOP and POP.
POP--> procedure oriented Programming -->Functions


Function--> A Function is a blook of code (statements) which performs a specific task.
It is a reusable code--> readbility,reusability and easy to maintain...

<-->Types of Function<-->
1-->User Define Function-->def
2-->Built In Functions-->Python by default(print,len,min,max,sorted...etc
3-->Anonymous Function--> Nameless Function-->Lambda(map,filter) reduce
4-->Recursive Function-->Recursion-->Factorial,Fibbonic--Decorators

'''
#User Define Function-->

#Syntax:
'''
def fname(parameter): #Function Header
        """Doc String (Description Function)"""
        
        Statements(s).....#Body of function
        ..................
        return value(s)
fname(args) #function call

#Simple Function to Understand the reusability

def add(a,b):
    """ This Function is used for add 2 obj"""
    c=a+b
    print(c)

add(208930,29083)
add('dee','pak')
add([1,2,0,3],[2,5,6,63,])

def add(a,b):
    """ This Function is used for add 2 obj"""
    c=a+b
    #print(c
    return c

print(add(208930,29083))
add('dee','pak')
print(add([1,2,0,3],[2,5,6,63,]))

def add(a,b):
    """ This Function is used for add 2 obj"""
    #c=a+b
    #print(c
    #return c
    return f'Result is {a+b}'
#print(add(24,3))
#print(add(dhdh,sjs))
g,h=38,32
e=add(g,h)
print(e)

def greetings():
    """Greeting to User"""
    return "Hello sir! Wellcome to codegnan"
    #return "How r u guys" A function have multiple values to return but not multiple return statements

print(greetings())
print(type(greetings()))
print(type(greetings))
'''
def greetings():
    """Greeting to User"""
    return "Hey","Guys","Mahi" #it is a tuple not string
    #if u need a list put it in [] sq brackets
print(greetings())
print(type(greetings()))
print(type(greetings))



































