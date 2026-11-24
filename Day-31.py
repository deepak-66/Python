'''
hii....
Modules--> User Define Modules--> Create, Accessing..
A Module is a python file(.py) Consists of objects,Varibles,function
we use import keyword...

import My_module

print(dir(My_module)) #use dir to get list all avalible methods and attributs
print(type(My_module.greet))
print(My_module.greet("Saketh"))
print(type(My_module.name))
print(My_module.name.items())

print(My_module.__doc__) #It returns docstring (description of module)
print(__doc__)  #it returns current file docstring

My_module.name.update({"Place":"Vizag","subject":['Python','Aptitude','SQL']})
print(My_module.name)
print(len(My_module.name))

#Accessing methods/attributes using from keyword
from My_module import greet
print(greet("Codegnan"))

#print(name)  #this is not possible as we didn't import it
from My_module import greet,name #wee can impotr multiple attributes
print(name)

#Aliasing module names

import My_module as me
print(me.greet("Vijay"))
print(me.name.keys())

#To access all method/attributes we '*'

from My_module import *  #this is only recommend for user/saimple modules
print(name)
print(greet("Saketh"))
'''









