class Car:
    def __init__(self, speed):
        self.speed = speed

    def calculate_distance(self, time):
            return self.speed * time

car = Car(70)

print(f"In 6 hours the car will travel {car.calculate_distance(6)}miles.")
print(f"In 10 hours the car will travel {car.calculate_distance(10)}miles.")
print(f"In 15 hours the car will travel {car.calculate_distance(15)}miles.")
