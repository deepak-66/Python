'''
String Methods --> Case Conversions,Replacing,Finding,White Trailing spacea,
Testing methods,alignment methods

#case conversions-->upper(),lower(),title(),capitalize(),swapcase()
data='codegnan'

print(type(data))
print(dir(data))  #dir() returns the avalible methods/function

#upper()-->convert objects ti uppercase
print(data)
print(data.upper())
e=data.upper()
print(e)
#lower()-->convert objects to lowercase
f=data.lower()
print(f)


#capitalize()--> it will capitalize thefirst letter in the word
print(data.capitalize())
d='codegnan vizag'
print(d.capitalize())# caplitalize only works on first word only

#title()
print(d.title())# here it will caplitalize all words in the string

#swapcase() converts upper to lower and lower to upper
name='deePAK'
print(name.swapcase())

#Testing methods (which will give the result as Boolean (True/Flase)
#isupper(),islower(),isalnum(),isdigit()....

print("codegnan".isupper())
print("codegnan".islower())
print("Deepak123".isalnum())
print("Deepak".isdigit())
print("Codegnan".isupper())

print("183".isupper())
print("091723Deepak".isdigit())
print("0938762".isdigit())
print("Python".istitle())
print("Python aptitude".iscaptlize())

data='Python Aptitude'
print(data.startswith('P'))
print(data[7:].startswith('A'))
print(data.startswith('A',7))
print(data.find('A'))
print(data.endswith("e"))
print(data.endswith("n",0,6))
print(data.endswith("n",0,7))

d=2929.22
print(d.isnumeric())

data='codegnan is in vizag'
print(data.find('a'))#returns only first occurance 
print(data.find('a',7))#here it will checks next occurance
print(data.find('u',7))
#find will returns -1 if the given objects is not present
print(data.rfind('a'))#here rfind() returns last occurance

data='codegnan is in vizag'
print(data.index('s'))
print(data.index('is'))
print(data.rindex('n'))

print('codegnan'.count('g'))
'''
#slpit(),join(),strip(),lstrip(),rstrip(),zfill()
#split() return the list of substrings from the string using separator
a="pyhton aptitude softskills mysql"
print(a.split())
d="pythoe,djde,dje.dd"
print(d.split(','))
print(d.join(" | "))
 #a=['Deepak','Balu','Nikhil'] list' object has no attribute 'join'
print(a.join(' | '))

#white space & trimming method-->strip(),lstrip(),rstrip()
a=' Deepak '
print(len(a))
print(len(a.strip()))

#Alignment method-->zfill() (make sure to pass the width > len(obj)

a='python'
'''
print(a.zfill(20))
print(a.center(20,'#'))
print(a.ljust(20,'#'))
print(a.rjust(20,'#'))
print('Deepak'.center(200,'$'))
'''
print(a.zfill(1))










