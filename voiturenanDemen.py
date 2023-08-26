#super().__init__(make,model,year,daily_rate)

#Klas manman
class Veyikil:
    def __init__(self,make,model,year,daily_rate):
        self.make=make
        self.model=model
        self.year=year
        self.daily_rate=daily_rate
#klas pitit
class Car(Veyikil):
    def __init__(self,make,model,year,daily_rate,num_seats):
        Veyikil.__init__(self,make,model,year,daily_rate)
        self.num_seats=num_seats
    def display_info(self):
        print("Car-------------->Name:",self.make,"            Model:",self.model,"     Year:",self.year,"   Price/day:",f"{self.daily_rate}.00","HTG","   Num_seats:",self.num_seats)
        
#klas  pitit
class Motorcycle(Veyikil):
    def __init__(self,make,model,year,daily_rate,engine_type):
        Veyikil.__init__(self,make,model,year,daily_rate)
        self.engine_type=engine_type
    def display_info(self):
        print("Motorcycle------->Name:",self.make,"   Model:",self.model," Year:",self.year,"   Price/day:",f"{self.daily_rate}.00","HTG","   Engine_type:",self.engine_type)
        
#klas pitit
class Bicycle(Veyikil):
    def __init__(self,make,model,year,daily_rate,frame_type):
        Veyikil.__init__(self,make,model,year,daily_rate)
        self.frame_type=frame_type
    def display_info(self):
        print("Bicycle---------->Name:",self.make,"              Model:",self.model,"        Year:",self.year,"   Price/day:",f"{self.daily_rate}.00","HTG","   Frame_type:",self.frame_type)
        


class Rental:
    def __init__(self,vehicle,rental_days):
        self.vehicle=vehicle
        self.rental_days=rental_days
    def calculate_total_cost(self):
        return self.vehicle.daily_rate*self.rental_days                                      
    def display_receipt(self):
        print("-------display_receipt------\n")
        self.vehicle.display_info()
        print(f"Rental days:{self.rental_days}")
        total_cost=self.calculate_total_cost()
        print(f"Total cost:{total_cost:.2f} HTG") 

#P. prensipal
car=Car("Toyota","Camry",2023,50,5)
motorcycle = Motorcycle("Harley-Davidson","Sportster",2023,80,"V-twin")
bicycle=Bicycle("Trek","FX",2023,15,"Hybrid\n")

car.display_info()
motorcycle.display_info()
bicycle.display_info()


rental_car = Rental(car,3)
rental_car.display_receipt()

rental_motorcycle=Rental(motorcycle,2)
rental_motorcycle.display_receipt()

rental_bicycle=Rental(bicycle,1)
rental_bicycle.display_receipt()

