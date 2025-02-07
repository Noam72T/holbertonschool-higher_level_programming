from abc import ABC

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
