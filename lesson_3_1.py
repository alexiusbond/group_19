class MusicPlayable:  # Mixins
    def play_music(self, song):
        print(f'Now is playing {song}')


class Car(MusicPlayable):
    '''Car class is used for creation of car objects'''

    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    # def drive(self):
    #     print("I can drive")

    def __str__(self):
        return f'Model: {self.__model} Year: {self.__year}'

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __eq__(self, other):
        return self.__year == other.__year and self.__model == other.__model


class FuelCar(Car):
    __total_fuel = 800

    @staticmethod
    def fuel_type():
        print('AI - 95')

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    def put_fuel(self, amount):
        print(f'{self.model} is filled with fuel {amount} liters')
        FuelCar.__total_fuel -= amount

    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print("I can drive using fuel")

    def __str__(self):
        return super().__str__() + f' Fuel Bank: {self.__fuel_bank}'


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print("I can drive using electricity")

    def __str__(self):
        return super().__str__() + f' Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, fuel_bank, battery):
        FuelCar.__init__(self, model, year, fuel_bank)
        ElectricCar.__init__(self, model, year, battery)

    def drive(self):
        ElectricCar.drive(self)
        FuelCar.drive(self)


class Phone(MusicPlayable):
    pass


class SmartPhone(Phone):
    pass


prius = HybridCar("Toyota Prius", 2022, 35, 25000)
print(prius)
prius.drive()
prius.play_music("Song 1")

samsung = SmartPhone()
samsung.play_music("Son....")

bmw = FuelCar("BMW X7", 2021, 65)
bmw2 = FuelCar("BMW X7", 2021, 63)

print(4 > 9)
print(prius > bmw)
print(prius == bmw)
print(bmw2 == bmw)

bmw.put_fuel(60)
print(f'Tatol amount at depo: {FuelCar.get_total_fuel()}')
FuelCar.fuel_type()

print(HybridCar.mro())
print(Car.__doc__)
