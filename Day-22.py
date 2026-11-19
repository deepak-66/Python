'''
def sample(*a):
    """ Use of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(28,33,2)
#in above case we used '*' to pack the value into a tuple

a,b,c=2,4,-6
print(a,b,c)
print(c)
print(b)
#a,*b,

a,*b,c=(2,4,5),6,65,12,-12
print(a,b,c)


#Find The sum of values

def deepak(*a):
    """Use of varible lenght arguments"""
    print(a)
    print(type(a))
    result=0
    for i in a:
        result+=i
    print(result)
#deepak(1,2,3,4,5)
#add(12,3,4,2,2,-12,284,282,29)
#print(add(1,2,3,4,'codgnan',282,8,'Deepak')) It will rise the type error it dosn't add int and string

def deepak(*a):
    """Use of varible lenght arguments"""
    result=[]
    for i in a:
        if type(i) in (int,float):
            result+=i
    print(result)

#print(deepak(1,2,3,4,'codgnan',2,8,'Deepak'))
d=list(map(input("Enter value : ").split()))
print(d)
print(deepak(*d))
'''
#we will use above use of variable lenght arguments for ordering pizza
'''
def order_pizza(size,*toppings):
    """use of *args"""
    print(f'Size of Pizza is {size}')
    print(f'Toppings : {toppings}')
order_pizza('Large','Onion','Paneer','Capsium','Olives','Mushrooms')

def order_pizza(size,*toppings):
    """use of *args"""
    print(f'Size of Pizza is {size}')
    for i in toppings:
        print(f'Topping added : {i}')
order_pizza('Large','Onion','Paneer','Capsium','Olives','Mushrooms')

def order_pizza(size,*toppings):
    """use of *args"""
    print(f'Size of Pizza is {size}')
    for i in toppings:
        if i== 'Onion':
            continue
        print(f'Topping added : {i}')
size=input('enter the size of Pizza :')
toppings=list(input('Enter the toppings : ').split())
print(order_pizza(size,*toppings))
'''
#keyword varible lenght arguments:
#Any number of keyword arguments,data is stored in dictionary, we use **args...

def sample(**a):
    """use of *arg"""
    















