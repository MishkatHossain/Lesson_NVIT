from car import Car


car1 = Car("Bugatti", "Cheron", 2021, "red")
car2 = Car("Lamborgini", "Gallardo", 2021, "yellow")
car3 = Car("Ferrari", "Enzo", 2020, "red")

print(car1.name, car1.model, car1.year, car1.color)
print(car2.name, car2.model, car2.year, car2.color)
print(car3.name, car3.model, car3.year, car3.color)


car1.drive()
car1.stop()



