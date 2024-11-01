class Animal:
    name: str
    sound: str

    def make_sound(self):
        pass


class Cat(Animal):
    sound = 'Meow!'

    def make_sound(self):
        print(self.sound)


class Dog(Animal):
    sound = 'Woof!'

    def make_sound(self):
        print(self.sound)


if __name__ == '__main__':
    cat = Cat()
    dog = Dog()

    cat.make_sound()
    dog.make_sound()
