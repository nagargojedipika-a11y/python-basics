# Use for loop to iterate through a list
courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
    print(course)
print('-------for loop using range()-----------')
# range() comes handy when using for loop
for i in range(5):   # prints from 0 to 4
  print(i)
print('------------')
for i in range(3,8):   # prints from 3 to 7
  print(i)
print('----------enumerator----------')
# Use enumerator for getting index
courses = ['ba', 'bcom', 'bsc', 'be']
for id, item in enumerate(courses):
  print(id, item)
print('---------condition under loop----------')
# we can use condition inside for loop
courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
    if course == 'bcom':
        print(course)
    else:
        print('Course is NOT bcom')
print('---------break statement----------')
# exit a loop at a certain condition, say 
courses = ['ba', 'bcom', 'bsc', 'be']
for item in courses:
  print(item)
  if item == 'bsc':                
    break  
print('----------continue statement---------')          
courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
  if course == 'bsc':
    continue
  print(course)
print('---------nested loop-------------')
for i in range(4): # outer loop
    for j in range(20, 24): # inner loop
        print(i, j)
print('----------print astrick symbol pattern--------')
rows = int(input("Enter the rows  :"))    
for i in range(0, rows+1):               
    for j in range(i):                   
        print("*", end='')               
    print()        
