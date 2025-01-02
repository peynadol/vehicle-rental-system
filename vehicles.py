class Vehicle:
    def __init__(self, id, model, year, rate, availability):
        self.id = id
        self.model = model
        self.year = year
        self.rate = rate
        self.availablity = availability

    def check_out(self):
        pass

    def return_vehicle(self):
        pass

    def maintenance_check(self):
        pass


class Car(Vehicle):
    def __init__(self, id, model, year, rate, availability, seats, fuel_type, transmission):

        super().__init__(id, model, year, rate, availability)

        self.seats = seats
        self.fuel_type = fuel_type
        self.transmission = transmission
