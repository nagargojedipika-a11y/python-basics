#1.data types-string,float,int
dummy="Hello World"
print(dummy)
print(type(dummy))

num=3
another_num=3.0
print(type(num))
print(type(another_num))

val=True
print(type(val))

#2.Strings
test='Apples\'s products are beautiful'
print(test)
#find len of the string
print(len(test))
#print characters of that index
print(test[0])
print(test[4])
print(test[2:5])
print(test[:2])
print(test[2:])
print(type(test))
print(type(test[2:4]))

#3.String Functions
text="hello world"
#for upper case
print(text.upper())
#for lower case
print(text.lower())
#for first letter of each word is in uppercase
print(text.title())
#for string count
print(text.count('l'))
print(text.count('rl'))
print(text.find('o'))
print(text.count('H'))
print(text.find('H'))

text='This is a beautiful world'
print(text.find('beautiful'))#find beautiful at index 10
print(text.count('beautiful'))#apperance of the word in sentence
print(text.count('is'))
print(text.replace('world','planet'))#replace world with planet
#for storing as a output
new_text=text.replace('world','replace')
print(new_text)
print(text)
fruit='applllllleeeeeee'
print(fruit.replace('e','E'))
print(fruit.replace('z','E'))#no change because z doesen't exist
#strip() for remove 1st and last blank space
msg='     Hello World    '
print(msg)
print(msg.strip())
#for checking blankspace is delete use len()
print(len(msg))#method1
print(len(msg.strip()))
print(msg.count(' '))#method2
print(msg.strip().count(' '))
#split()
address='66,Sneha Didi,Dhule'
print(address.split(','))
#for breaking string where single space is occur
test='how are you doing'
print(test.split(' '))
output=test.split(' ')
print(output)
print(type(output))
#for connect to string use +
first='dipika'
last='nagargoje'
name=first + ' '+last
print(name)
#f string
name=f'{first}{last}'
print(name)
name=f'{first.upper()}{last.lower()}'
print(name)

#accpect input from user
name=input('enter your name')
print(name)
print(type(name))