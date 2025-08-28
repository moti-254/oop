class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand       # encapsulated attribute
        self._model = model

    def get_info(self):
        return f"{self._brand} {self._model}"

    def move(self):
        print("The vehicle is moving.")  # Placeholder method (to be overridden)


#Inherit from Vehicle class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def move(self):
        print(f"{self.get_info()} is driving on the road. 🚗")


class Plane(Vehicle):
    def __init__(self, brand, model, airline):
        super().__init__(brand, model)
        self.airline = airline

    def move(self):
        print(f"{self.get_info()} is flying through the sky. ✈️")


class Boat(Vehicle):
    def __init__(self, brand, model, boat_type):
        super().__init__(brand, model)
        self.boat_type = boat_type

    def move(self):
        print(f"{self.get_info()} is sailing on water. 🚢")


# Function to demonstrate polymorphism
def perform_travel(vehicle):
    vehicle.move()  # Polymorphic behavior

#Example usage
car = Car("Toyota", "Corolla", 4)
plane = Plane("Boeing", "747", "Delta Airlines")
boat = Boat("Yamaha", "SX210", "Speedboat")

vehicles = [car, plane, boat]

for v in vehicles:
    perform_travel(v)

