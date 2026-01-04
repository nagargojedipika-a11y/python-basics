#import math module for math 
import math
math.sqrt(4) #for sqrt

from math import sqrt
sqrt(4)

#counting ahead
math.log10(100)
math.pi  #pi value

#data module
from datetime import date
print(date.today())
today = date.today()
print(today)
print(today.day, today.month, today.year) 

#for datetime
from datetime import datetime
print(datetime.now())
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 