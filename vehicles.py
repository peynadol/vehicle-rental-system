class Vehicle:
    def __init__(self, id, model, year, rate, availability):
        self.id = id
        self.model = model
        self.year = year
        self.rate = rate
        self.availablity = availability

    def check_out(self):
        if self.availablity:
            self.availablity = False
            print(f"This {self.model} is now checked out and unavailable.")
        else:
            print(f"This {self.model} is already unavailable.")

    def return_vehicle(self):
        pass

    def maintenance_check(self):
        pass


class Car(Vehicle):
    def __init__(self, id, model, year, rate, availability,
                 seats, fuel_type, transmission):

        super().__init__(id, model, year, rate, availability)

        self.seats = seats
        self.fuel_type = fuel_type
        self.transmission = transmission


class Motorcycle(Vehicle):
    def __init__(self, id, model, year, rate, availability, engine_size,
                 requires_license):

        super().__init__(id, model, year, rate, availability)

        self.engine_size = engine_size
        self.requires_license = requires_license


class Bicycle(Vehicle):
    def __init__(self, id, model, year, rate, availability, type,
                 helmet_included):

        super().__init__(id, model, year, rate, availability)

        self.type = type
        self.helmet_included = helmet_included
