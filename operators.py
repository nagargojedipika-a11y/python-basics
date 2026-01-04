num1=3
num2=5
print(num1,num2)
print(type(num1),type(num2))
#arithmetic operator
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num2/num1)
print(num2//num1)
print(num2%num1)
print(3**2)
#BODMAS rule
print(5*4+1)   #first multiplication execute
print(5*(4+1))
#comparison operator
print(2==2)
print(2==1)
print(3!=2)
print(3>2)
print(3<2)
print(3>=3)
print(3>=2)
print(3<=2)
#assignment operator
num=4
print(num)
num +=1
print(num)
#logical operator
x=5
print(x>4 and x<6) #and(&) operator,it's true when both cond are true 
print(x>3 or x<4)  #OR(|)operator,it's true when one of the cond is true
print(not(x>3 and x<10))   #not(!)operator,it's check for opposite result

#function realated to int and float
print(abs(-2))  #abs() func gives positive number
print(abs(-2.1))
print(round(3.45))  #round()func round off the digits after decimal point
print(round(-3.95))
print(round(3.469,1))  #round the number till 1 decimal place
print(round(3.469,2))

#type casting
#1.converting string to int
a = '2'
b = '3'
print(a, type(a))
print(b, type(b))
print('Addition = ', a+b)   
print()                     # Leaves a blank space in output

a = int(a)
b = int(b)
print(a, type(a))       # here you'll get output as int
print(b, type(b))       # here you'll get output as int
print('Addition = ', a+b)

#2.float to str
num = 2.0
print(type(num))
num = str(num)
print(type(num))

#3.str to bool
num = 'True'
print(type(num))
num = bool(num)
print(type(num))

#4.convert string to integer
num = input('Enter some number --- ')       
print(num, type(num))
new = int(num)            # typecasting
print(new, type(new))
#carry addition of two user-inputted numbers
num1 = input('Enter first number:  ')
num2 = input('Enter second number:  ')
print(num1 + num2)    
print(int(num1) + int(num2))   
