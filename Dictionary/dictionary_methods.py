
car = {"CarName": "BMW", "model": "i8", "make": 2018}
print(car)
print(car.keys())
print(car.values())
print(car.items())
car_duplicate = car.copy()
print(car_duplicate)
car.popitem()  # will remove the last item in the dictionary by default
car.pop("model")  # to remove a specific item
print(car)


print("*"*10)
cars = {"BMW": {"model": "i8", "year": 2016},
        "FERRARI": {"model": "FF", "year": 2018},
        "BUGATTI": {"model": "BGM", "year": 2019}}

print(cars.keys())
print(cars.values())
print(cars.items())