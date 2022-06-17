class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        if isinstance(address, Address):
            self.__address = address
        else:
            raise TypeError("Value for address attribute must be Address type")
        self.__created()

    def set_name(self, value):
        self.name = value

    def set_address(self, value):
        if isinstance(value, Address):
            self.__address = value
        else:
            raise TypeError("Value for address attribute must be Address type")

    def set_age(self, value):
        if value <= 0:
            raise ValueError("Wrong value for age it must be positive integer")
        else:
            self.__age = value

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def info(self):
        return f'Name: {self.__name} Age: {self.__age} \n' \
               f'Address: {self.__address.city}, {self.__address.street} {self.__address.number}'

    def __created(self):
        print(f'{self.__name} was born')

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, address, commands):
        super().__init__(name, age, address)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f" Commands: {self.__commands}"

    def speak(self):
        print(f"{self.get_name()} says gav gav")


class Cat(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)

    def speak(self):
        print(f"{self.get_name()} says myau myau")

class Fish(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)


animal = Animal("Animal 1", 8, Address("Bishek", "Toktogula", 89))
print(animal.info())
# animal.__age = "dsfdas"
animal.set_age(9)
print(animal.info())
print(animal.get_age())
# animal.__created()

dog = Dog("Snoofy", 1, Address("Osh", "Lenina", 21), "Sit")
print(dog.info())
dog.commands = "Sit, Run"
print(dog.info())
dog.speak()

address_of_tom = Address("NY", "Wall Street", 2123)
cat = Cat("Tom", 2, address_of_tom)
print(cat.info())
cat.speak()

fish = Fish ("Ariel", 3, Address("LA", "New Street", 89))

print("___________")
animals_list = [dog, cat, fish]
for a in animals_list:
    print(a.info())
    a.speak()