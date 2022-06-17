class Transport:
    def __init__(self, year_value, model, color):
        self.year = year_value  # self.year - attribute, year_value - parameter
        self.model = model
        self.color = color

    def change_color(self, new_color):
        self.color = new_color


class Car(Transport):
    number_of_wheels = 4
    counter = 0

    def __init__(self, year_value, model, color, penalties=0.0):  # constructor
        super().__init__(year_value, model, color)
        print(self)
        Car.counter += 1
        self.penalties = penalties

    def drive(self, city):  # method
        print(f'Car {self.model} is driving to ' + city)


class Plane(Transport):
    def __init__(self, year_value, model, color):
        super().__init__(year_value, model, color)


class Truck(Car):
    number_of_wheels = 10
    counter = 0

    def __init__(self, year_value, model, color, load_capacity):
        super().__init__(year_value, model, color)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weigth, cargo_info):
        print(f'Cargo of weigth {weigth} kg of {cargo_info} was loaded on {self.model}')


def test():  # function
    print("Test")


mazda_car = Car(2020, "Mazda RX-8", "Red")  # mazda_car - reference variable
print(f'Model: {mazda_car.model} Year: {mazda_car.year} Color: {mazda_car.color} '
      f'Penalties of car: {mazda_car.penalties} Number of wheels: {mazda_car.number_of_wheels}')
mazda_car.color = "Yellow"
print(f'Model: {mazda_car.model} Year: {mazda_car.year} Color: {mazda_car.color} '
      f'Penalties of car: {mazda_car.penalties} Number of wheels: {mazda_car.number_of_wheels}')
print(mazda_car)
bmw_car = Car(year_value=2011, color="Black", model="BMW X5", penalties=800.5)
print(f'Model: {bmw_car.model} Year: {bmw_car.year} Color: {bmw_car.color} '
      f'Penalties of car: {bmw_car.penalties} Number of wheels: {bmw_car.number_of_wheels}')
bmw_car.drive("Osh")
mazda_car.drive("Bishkek")

print(f'Model: {bmw_car.model} Year: {bmw_car.year} Color: {bmw_car.color} '
      f'Penalties of car: {bmw_car.penalties} Number of wheels: {bmw_car.number_of_wheels}')

print(f'We need {Car.number_of_wheels * Car.counter} winter lastics')

Car.number_of_wheels = 5
audi_car = Car(2009, "Audi Q7", "White")
print(f'Model: {audi_car.model} Year: {audi_car.year} Color: {audi_car.color} '
      f'Penalties of car: {audi_car.penalties} Number of wheels: {audi_car.number_of_wheels}')

print(f'We need {Car.number_of_wheels * Car.counter} winter lastics')

airbus_plane = Plane(2022, "A-360", "White")
print(f'PLANE Model: {airbus_plane.model} Year: {airbus_plane.year} Color: {airbus_plane.color}')
airbus_plane.change_color("Blue")
print(f'PLANE Model: {airbus_plane.model} Year: {airbus_plane.year} Color: {airbus_plane.color}')

volvo_truck = Truck(2000, "Volvo - 8788", "Blue", 20000)
print(f'TRUCK Model: {volvo_truck.model} Year: {volvo_truck.year} Color: {volvo_truck.color} '
      f'Penalties of car: {volvo_truck.penalties} Number of wheels: {volvo_truck.number_of_wheels} '
      f'Load Capacity: {volvo_truck.load_capacity}')
volvo_truck.load_cargo(10000, "apples")

print(f'We need {Car.number_of_wheels * Car.counter} winter lastics for cars')
print(f'We need {Truck.number_of_wheels * Truck.counter} winter lastics for trucks')
print(Car.counter)