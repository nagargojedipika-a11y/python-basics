courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses))
print(courses[1]) 
print(courses.count('ba'))
print(courses.count('baa'))  
print(courses.index('bsc'))
#use for loop for tuple
for item in courses:     
  print(item)
#enumerate() fun to get index of element as well
for id, item in enumerate(courses):     
  print(id, item)  
#check length of tuple
print(len(courses))
# If you are storing numbers in tuple, you don't need ''
nums = (2, 3, 4)
print(type(nums))
# Mix of str and int and bool is allowed in tuple
data = ('ba', 2, True, 'bsc')
print(data)
print(type(data))
# TRICKY ONE. For single valued tuple, you have to add a comma, else it'll be treated as a string
new = ('50')              # this will be treated as string
print(type(new))
print('-----------------------------')
new1 = ('50',)            # this will be treated as tuple
print(type(new1))
#concatenate two tuple

new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1 + new2)
#for delete use del
del new2
# check whether an element is in the tuple
fruits = ('apple','mango')
print('mango' in fruits)   # return True if 'mango' is part of fruits else False. Thanks to 'IN', it comes handy many times in the real world programs. 
print('mangoes' in fruits)
# To convert list into a tuple
num = [1, 2, 3, 4]
new = tuple(num)
#for getting elemnt using their index
num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])
print(num[-2])   
courses = ('ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me')
print(courses[3:5])   # print courses from 3rd index to 5th
print(courses[3:])   # print courses from 3rd index onwards
print(courses[:3])   # print courses upto 3d index
print(courses[-3:])   # print last three courses