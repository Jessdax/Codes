class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
    
class Cow(Animal):
    def speak(self):
        return f"{self.name} moos."
    
cat = Cat("Whiskers")
cow= Cow("Bessie")

print(cat.speak())
print(cow.speak())