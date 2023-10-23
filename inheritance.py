class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog speaks")

class dogChild(Dog):
    def eats(self):
        print("Drinking milk")

dog=Dog()
dog.bark()
dog.speak()
dogMdogo=dogChild()
dogMdogo.bark()
dogMdogo.speak()
dogMdogo.eats()
