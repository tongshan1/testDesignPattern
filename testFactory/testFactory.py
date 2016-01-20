__author__ = 'tongshan'

class Animal:

    def __init__(self, name):

        self.life = True
        self.name = name
        self.high = 0

    def eat(self, food):
        a = ("%s eat %s" % (self.name, food))
        return a

    def speak(self):
        return

class Cat(Animal):

    def speak(self):
        b = ("%s speak cat" % (self.name))
        return b


class Dog(Animal):

    def speak(self):
        b = ("%s speak Dog" % (self.name))
        return b

def get_factory(name):
    if name == "cat":
        return Cat(name)
    if name == "dog":
        return Dog(name)


if __name__ == "__main__":

    i = get_factory("dog").speak()
    print(i)
