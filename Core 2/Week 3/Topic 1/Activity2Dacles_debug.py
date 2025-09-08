class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.mileage = 0 # mileage defined incorrectly

    def show_details(self):
        print(f"This is a {self.color} {self.brand} from {self.year}.")

    def drive_distance(self, distance):
        self.mileage += distance # self missing

    def display_mileage(self):
        print(f"This car has traveled {self.mileage} kilometers.") # Wrong string interpolation

# Create a car object
car = Car("Ford", "Black", 2022) 

# Drive the car
car.drive_distance(500)
car.drive_distance(300)
car.drive_distance(200)

# Show total mileage
car.display_mileage()