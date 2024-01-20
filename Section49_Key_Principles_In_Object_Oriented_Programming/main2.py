class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        # Code to start the vehicle
        pass

    def stop(self):
        # Code to stop vehicle
        pass

class Car(Vehicle):
    def __init__(self, make, model, doors_qty):
        super().__init__(make, model)
        self.doors_qty = doors_qty

    def lock_doors(self):
        # logic to lock doors
        pass

    def unlock_doors(self):
        # logic to unlock the doors
        pass

