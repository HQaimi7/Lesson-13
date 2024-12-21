#no inheritence

class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def feature3(self):
         print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a1 = A()
a1.feature1()
b1 = B()
b1.feature4()

#With inheritence -- single

class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def feature3(self):
         print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a1 = A()
a1.feature1()
b1 = B()
b1.feature1()


#Multi-Level Inheritence


class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def feature3(self):
         print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(B):
    def feature5(self):
        print("Feature 5 is working")


b1= C()
b1.feature3()

# Multiple Inheritance

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 3 working")


class C(A, B):
    def feature5(self):
        print("Feature 5 working")


b1 = C()
b1.feature3()

# Base class/Parent
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make a sound!"

# Derived class/child
class Dog(Animal):
    def talk(self):
        return "Woof!"

# Creating an instance of the Dog class
my_dog = Dog("Buddy")

# Using the inherited method
print(f"{my_dog.name} says: {my_dog.speak()}")  # Output: Buddy says: I make a sound!
print(f"{my_dog.name} says: {my_dog.talk()}")   # Output: Buddy says: Woof!

# Base Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "Vehicle is starting"

# Derived class
class Car(Vehicle):
    def start(self):
        return "Car is starting"

class Bike(Vehicle):
    def start(self):
        return "Bike is starting"

# Creating instances
my_car = Car("Toyota")
my_bike = Bike("Yamaha")

print(f"{my_car.brand}: {my_car.start()}")  # Output: Toyota: Car is starting
print(f"{my_bike.brand}: {my_bike.start()}")  # Output: Yamaha: Bike is starting
