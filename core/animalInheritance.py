
class Animal:
    def speak(self):
        raise NotImplementedError
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
for animal in [Dog(), Cat()]:
    print(animal.speak())