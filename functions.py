#define function
def hello():
   print('hello world')
#call function
hello() 
#pass arguments
def hello (name):
  print(f'hello {name}')
hello('John')
hello(12)
#function for addition
def addthis(first, second):
  print(first + second)
addthis(12, 13) 
#return statement
def hi(name):    
    message = "Hi "+name  
    return message  
name = input("Enter the name:")    
print(hi(name))
#function to calculate interest on loan
p = int(input("Enter the principle amount? "))    
r = float(input("Enter the rate of interest? "))     
t = int(input("Enter the time in years? "))
def simple_interest(p,t,r):    
    return (p*t*r)/100     
print("Simple Interest: ",simple_interest(p,r,t))