class Animal:
    class_attribute = "I am a class attribute"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print("\n")
print(dog.name, "says", dog.speak())  # Buddy says Woof!
print(cat.name, "says", cat.speak())  # Whiskers says Meow!
print(cat.class_attribute)
print("\n")


class A:
    def greet(self): print("Hello from A")

class B(A):
    def greet(self): print("Hello from B")

class C(A):
    def greet(self): print("Hello from C")

class D(B, C):  # Multiple inheritance
    pass


d = D()
d.greet()  # Hello from B
print(D.mro()) # Return a type's method resolution order.
print("\n")