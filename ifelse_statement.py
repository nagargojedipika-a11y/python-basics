#if statement
x = 14
y = 13
if x > y:            
  print('yes, x is indeed greater than y') 
  print('I want to be part of if clause as well, so i have given 4 indents before print()') 
print('this statement is not part of if clause, hence there is no indent here')
print('-----------------')
# We can find the number is even or odd.
n = int(input(" Enter a number to check:"))
if n % 2 == 0:
  print("It's an even number.")
if n % 2 != 0:
  print("It's an odd number.")
if n == 0:
  print("The number is neither even nor odd. Rather you entered Zero.")
print('------------------')
# Using If statement, we can find largest number among the
a = int(input("Enter the Value of a: "));  
b = int(input("Enter the Value of b: "));  
c = int(input("Enter the Value of c: "));  
if a>b and a>c:  
    print("a is largest input.");  
if b>a and b>c:  
    print("b is largest input.");  
if c>a and c>b:  
    print("c is largest input.");  
print('---------------------')
#if-else statement
if 4 > 5:
    print('four is greater than five')
else:
    print('four is smaller than five')
print('-----------------')
age = int (input("Enter your age? "))  
if age>=18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!");
print('--------------------')
#if-elif-else statement
marks = int(input("Enter the marks? "))  
if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
   print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail !!")  
print('----------------')
#logical operator
x = 3
y = 4
if x < y and x + y > 5:
    print('both statements are true')
if x < y or x > y:
    print('one of the statement is true')
if x < y and not x + y < 5:
    print('both the statements must be true')
print('--------------------')
#nested if    
x = 7
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else:
        print('x is smaller than 20')
else:
    print('x is smaller than 10')