class Car():
    def __check_seatbelt(self):
        print("Seatbelt checked")
    
    def __check_fuel(self):
        print("Fuel level is okay")

    def __start_engine(self):
        print("Engine started")

    def drive(self):
        self.__check_seatbelt()
        self.__check_fuel()
        self.__start_engine()
        print("Car is now moving")

    def stop(self):
        print("Car has stopped")

car = Car()

car.drive()
car.stop()