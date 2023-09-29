""" Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. """


class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):

    def __init__(self, name: str, age: int, spec):
        super().__init__(name, age)
        self.spec = spec


class Cat(Animal):

    def __init__(self, name: str, age: int, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):

    def __init__(self, name: str, age: int, spec):
        super().__init__(name, age)
        self.spec = spec

if __name__ == '__main__':
    dog_1 = Dog('Рекс', 5, 'кусает')
    cat_1 = Cat('Муся', 3, 'спит')
    bird_1 = Bird('Додо', 1, 'поет')

    for pet in [dog_1, cat_1, bird_1]:
        print(f'{pet.name} {pet.get_spec()}')

class Factory:
    type_list = ['dog', 'cat', 'bird']

    def __init__(self, type_animal, name: str, age: int, spec: str):
        self.type_animal = self.__errors_func(type_animal)
        self.params = (name, age, spec)

    def return_object(self):
        match self.type_animal:
            case 'dog': return Dog(*self.params)
            case 'cat': return Cat(*self.params)
            case 'bird': return Bird(*self.params)
    def __errors_func(self, type_animal):
        if type_animal in self.type_list:
            return type_animal
        else:
            raise ValueError 

if __name__ == '__main__':
    obj_1 = Factory('dog', 'Рекс', 1, 'сторожит').return_object()
    print(type(obj_1))
    print(f'{obj_1.name} {obj_1.get_spec()}')