#Exception Handling
'''
try:
    a,b=map(int,input("Enter the value:").split())
    result=a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')
    '''
'''
#Multiple Except Block
try:
    a,b=map(int,input("Enter the value:").split())
    result=a/b
    print(f'Answer is {result}')
except ValueError:
    print('ValuError should be only 2 and only integer')
except ZeroDivisionError:
    print('ValuError should not be zero')
except NameError:
    print('code Sariga Chusi rayu')
    
try:
    subjects=['Python',45,'AI',30]
    subjects.append("sql")
    print(subjects)
except Exception as e:
    print(e)  #this can be written if u want
              #exception to make take care
except IndexError:
    print("Make sure to check the lenght")
except NameError:
    print("Check the spelling")
except AttributeError:
    print("Chack the method properly")
finally:
    print("Aneway this will be printed..")


try:
    value=int(input("enter  value"))
    f=10/value
    print(int(f))
except (ValueError,ZeroDivisionError,NameError) as e:
    print(f'An Error occured:{e}')
'''


#Raising Excepthions
#You can rais an error intentionally using raise keyword
'''

value=int(input("enter a number"))
if value<0:
    raise ValueError("Value Cannot be Negative")
else:
    print("Done")
    
#Custom ErrorMessage-->
try:
    raise Exception("Custom Error")
except Exception as e:
    print(e)

try:
    value=-15
    if value<0 or value in [1,20]:
        raise Exception("Value is in Negative")
except Exception as e:
    print(e)

def fn(a,d):
    """Testing"""
'''
#File Handilng-->
''' File and directory operations are essentila to store the data...
Python Provides built-in function--open()
'''
#mode of operations-->'r','w','r+','w+'
#open(filename,mode) default med is 'r'
'''
try:
    file=open('Nwfile.txt','r')
    print(file)
    #print(file.read())  #read the file total content
    #print(file.readline()) #read only 1 line
    print(file.readlines()) #display the in a list
except FileNotFoundError:
    print(e)
'''

file=open('Newfile.txt','r')
print(file)
#print(file.read())  #read the file total content
#print(file.readline()) #read only 1 line
print((file.readlines()) #display the in a list

    









