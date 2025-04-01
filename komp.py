
#Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например,
# `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal ():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print (f'{self.name}, "говорит гав"')

class Cat (Animal):
    def make_sound(self):
        print("мяу")
dog1 = Dog ("Бобик", 5)
cat1 = Cat ("Тома", 1)

animals = [dog1, cat1 ]

for animal in animals:
    animal.make_sound()

print(animal)






