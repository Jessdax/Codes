class Car():
    def __init__(self, brand, color, engine_status):
        self.brand = brand
        self.color = color
        self.engine_status = engine_status

    def describe(self):
        print(f"{self.brand} in {self.color} color.")

    def start_engine(self):
        if self.engine_status == True:
            print(f"The {self.color} {self.brand} is now ON.")
        else:
            print(f"Error: The {self.color} {self.brand}'s is not working.")
        
    def stop_engine(self):
        if self.engine_status == True:
            print(f"The {self.color} {self.brand} is now OFF. ")
        else:
            print(f"The {self.color} {self.brand} engine is now OFF.")

car1 = Car("Toyota Vios", "Red", True)
car2 = Car("Honda Civic", "Blue", False)

car1.describe()
car1.start_engine()
car1.stop_engine()


print("")


car2.describe()
car2.start_engine()
car2.stop_engine()