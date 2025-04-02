
#Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например,
# `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says 'Woof!'")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says 'Meow!'")


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says 'Moo!'")


# Пример использования:
if __name__ == "__main__":
    dog = Dog(name="Buddy", age=2)
    cat = Cat(name="Whiskers", age=1)
    cow = Cow(name="Daisy", age=4)

    animals = [dog, cat, cow]

    for animal in animals:
        animal.make_sound()
        animal.eat()
#Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые
# наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите
# методы, если требуется (например, различный звук для `make_sound()`).

class Bird(Animal):
    def __init__(self, name: str, age: int, can_fly: bool):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} says 'Chirp!'")

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying!")
        else:
            print(f"{self.name} cannot fly.")


class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} makes a mammal sound.")


class Reptile(Animal):
    def __init__(self, name: str, age: int, has_shell: bool):
        super().__init__(name, age)
        self.has_shell = has_shell

    def make_sound(self):
        print(f"{self.name} hisses.")

    def shed_skin(self):
        print(f"{self.name} is shedding its skin.")


# Пример использования:
if __name__ == "__main__":
    bird = Bird(name="Tweety", age=1, can_fly=True)
    mammal = Mammal(name="Simba", age=3, fur_color="brown")
    reptile = Reptile(name="Lizzy", age=5, has_shell=False)

    animals = [bird, mammal, reptile]

    for animal in animals:
        animal.make_sound()
        animal.eat()

        if isinstance(animal, Bird):
            animal.fly()
        elif isinstance(animal, Reptile):
            animal.shed_skin()


