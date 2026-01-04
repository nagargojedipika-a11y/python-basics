#create dog class and their attributes
class Dog:
  def __init__(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
  def details(self):
    print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.age} ")

dog1 = Dog('Husky', 5, 'Blank')
dog1.details()

print('----------rectangle class---------------')
class Rectangle:
    def __init__(self, length, width ):
        self.length = length
        self.width = width
    def area(self):
        print(f"Length - {self.length}, Width - {self.width}")
        return self.length * self.width

first = Rectangle(5,2)
print(first.area())

print('-----------student class-----------')
class Student:
    def __init__(self, name):
        self.name = name         # the right side name is coming from the argument in the init(). While with the left side name we are defining a new property for the object and assigning value to that property with right side name

    def intro(self):
        print('Hi I am', self.name)

    def change_name(self, name):
        self.name = name
john = Student('john')
# access method
john.intro()
# access attribute
print(john.name)
# change name
john.change_name('JJOOHHNN')
john.intro()

