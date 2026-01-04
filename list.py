#basic program
courses = ['ba', 'bcom', 'bsc', 'ma', 'mcom', 'msc']
print(courses)  

#access list name
print(courses[0])
print(courses[3])
print(courses[0:2])
print(courses[-1])
print(courses[-2]) 
print(courses[-3:-1])
print(courses[-3:])

#functions
#help(list)       # list is a special and reserved keyword in python. It should NOT be used as variablename
help(list.append)
help(courses.append)  
courses.append('BE')
print(courses)
courses.insert(3, 'ME')   #insert requires position and value
print(courses)
new = ['11th', '12th']   
courses.append(new)      # Appending new list to the old list
print(courses)     
help(courses.extend)
courses.extend(new)
print(courses)
#To remove last entry of list, use pop()
courses.pop()
print(courses)
#To remove specific item, use remove()
courses.remove('ba')
print(courses)    # ba is removed

#to sort list
fruits = ['mango', 'apple', 'orange', 'kiwi', 'pineapple', 'papaya']
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(len(fruits))

nums=[8,4,2,1,16]
print(max(nums))
print(min(nums))
print(sum(nums))

#iterate list
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
for x in countries:
  print(x)
print('Now I am outside the for loop')
print('-------------')
for x in countries:
  print(x)
  print('Now I am inside the for loop')
print('---------')
for item in countries:
  print(item, len(item))          # printing each item and its length
print('---------')
for item in countries:
  print(item, item.upper(), len(item)) 
print('---------')
for item in countries:
  print(f'{item}, {item.upper()}, {len(item)}')      
print('----------')
for id, item in enumerate(countries):   # enumerate returns index along with the actual item, hence we need to catch it explicitly. 
  print(id, item)

#create list using loop and append()
cubes = []    # first define a blank list
for i in range(5):       # you can explore what range(5) gives. In short, it returns numbers upto 5. 
  cubes.append(i ** 3)
print(cubes)

#nested list
fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[0], type(fruits[0]))
print(fruits[1], type(fruits[1]))
print(fruits[0][0])
print(fruits[1][0])
print(fruits[0][2])