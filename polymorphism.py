class Bird:
    def fly(self):
        print("Some generic bird can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

def let_bird_fly(bird):
    bird.fly()

bird1 = Bird()
bird2 = Sparrow()
bird3 = Penguin()

let_bird_fly(bird1)
let_bird_fly(bird2)
let_bird_fly(bird3)
