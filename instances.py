class Vehicle:
    def Vehicle_info(self):
        print('Inside Parent(Vehicle)class')
        class Car(Vehicle):
            def car_info(self):
                print('Inside Child(Car) class')
                car = Car()
                car.Vehicle_info()
                car.car_info()
            
    