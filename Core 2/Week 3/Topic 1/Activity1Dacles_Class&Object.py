class Car():
    def __init__(self, brand, model, color, year, engine_status):
        self.brand = brand
        self.color = color
        self.year = year
        self.model = model
        self.engine_status = engine_status

    def describe(self):
        print(f"{self.brand} {self.model} in {self.color} color.")

    def start_engine(self):
        if self.engine_status:
            print(f'The {self.brand} {self.model} engine is now ON')
        else:
            print(f"Error: The {self.brand} {self.model}'s engine is not working")
    def stop_engine(self):
        print(f'The {self.brand} {self.model} engine is now OFF')


Car1 = Car("Rusi","XR100", "Purple", 2003, True)
Car2 = Car("Ferrari","LF20", "White", 1995, False)

Car1.describe()
Car1.start_engine()
Car1.stop_engine()

Car2.describe()
Car2.start_engine()
Car2.stop_engine()

