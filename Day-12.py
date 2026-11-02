'''
Dictionaries -->A Dictionary is a Mutable collection,data is indexed
using keys,keys must be unique.Dictionaries Methods
'''
details={'ids':['CGVI0242','CGVIO249','CGVI0224','CGVI0240'],
         'names':['Nikitha','Deepthi','Vinay','Tej'],
         'batch':'PFS-VSP-007',
         'place':('Vizag','Vijayawada','HYD','Banglore'),
         'subjects':{'Python','Aptitude','softskills'}}

#print(details.get('ids'))
#print(details.get('id'))
#print(details.keys())

#Inserting multiple keys into dictionary

data = {'email_ids':['nkt@gmail.com','dpt@icloud.com',
                     'vny@yahoo.com','tej@gmail.com'],
        'linkedin_ids':['nkt_123','dpt_234',
                        'vinay345','tej13']}
details.update(data)
'''
print(details.keys())
print(details)

#Delete data from the dictionary

#print(details.pop('linkedin_ids'))
print(details.popitem())#remove and retuurn key value pair from last
print(details.clear())# remove every thing and return error
print(details)

#del details[['ids','names']] return error
del details['ids'],details['names']# we can use to delete multiple pair at a time
print(details.keys())
'''
#setdefault()--> insert keys into the dictionary if its not preser

details.setdefault('status')
#print(details.keys())
details['status']=['placed','active','onhol']
#print(details)

#print(details.setdefault('ids'))#aswe already have ids in dictionary
#its just print the values

#fromkey()--> create a new dis
print(details.keys())












