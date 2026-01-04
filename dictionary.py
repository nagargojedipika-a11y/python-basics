#dictionary use key-value pair
company = {
  "name": "Tesla",         # this is called dictionary iteam. This dictionary has 3 items. 
  "founder": 'Elon Musk',
  "established": 2003
}
print(company)
#for their type
print(type(company))
#to access specific item(key)
print(company['name'])
#to get length
print(len(company))  
#for changing value of item,just override that value
company['name'] = 'TESLAA'
print(company)
#add new item
company['location'] = 'US'
print(company)
#to get item using get() func
print(company.get('name'))  # get() is predefined function for dict 
print(company.get('namee'))
#key() and value() func for getting all keys and values
print(company.keys())
print(company.values())
#add new key and value pair and check to get updated list
company['newkey'] = 'newval'
print(company.keys())
print(company.values())
#to delete item use pop and del also
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}
print(student)
student.pop('class') # use pop function and pass key
print(student)
#use del
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}
print(student)
del student['class']  # syntax -> del dict_name['key']
print(student)
#clear() clears the dictionary without deleteing the defined object
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}
print(student)
student.clear()
print(student)
#use loop for dictionary
new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})# dict is special keyword, wrap your dictionary within dict() 
print(new)
print(type(new))
for item in new:  # this loops over only keys
  print(item)
for item, val in new.items():
  print(item, val)
#loop through only 
for xyz in new.values():
  print(xyz)
#nested dictionary
company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company)
print(company['founders'])
print(company['founders']['first'])
for item, val in company.items():
  print(item, val)
  print(type(company['founders']))