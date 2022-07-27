class Car:
    wheels = 4
    def __init__(self, model, color, owner, year ):
        self.model = model
        self.miles = 0
        self.fuel_tank = 0
        self.color = color
        self.owner = owner
        self.year = year



    def get_fuel_tank(self, litr):
        self.fuel_tank += litr
        print(f"Вы залили {litr} литров бензина, итого {self.fuel_tank} в баке ")
        return self.fuel_tank

    def drive(self, km):
        litr = km * 0.1
        if self.fuel_tank >= litr:
            print('Go go go')
            self.miles += km
            self.fuel_tank -= litr
        else:
            print("NO GAS")

    def change_color(self, new_color):
        self.color = new_color
        print(f"New color!!! {self.color}")





tesla = Car("Model X", "white", "Nazgul", "2022")
porshe = Car("Cayen", "red", "Mirlan", "2022")
tesla.get_fuel_tank(40)
tesla.get_fuel_tank(50)
porshe.get_fuel_tank(50)

tesla.drive(400)
porshe.drive(500)

tesla.change_color("green")

porshe.exous = "noise"
print(tesla.__dict__)
print(porshe.__dict__)

print(tesla.fuel_tank)
print(tesla.color)
print(porshe.fuel_tank)


