import pickle, json


class Car:

    def __init__(self, brand, speed, age, mileage):
        self.brand = brand
        self.speed = speed
        self.age = age
        self.mileage = mileage

    def get_price(self):
        '''Условный расчёт цены в зависимости от марки, возраста и
        пробега в у.е. К реальным цифрам не имеет никакого отношения =)'''
        brand_dict = {'Lada': 2, 'Ford': 3, 'Volvo': 4, 'Mercedes': 5, 'Toyota': 6}
        brand_coeff = 1
        if self.brand in brand_dict:
            brand_coeff = brand_dict[self.brand]
        price = (1_000_000 * brand_coeff) - (10_000 * self.age + self.mileage)
        return price

    def calc_to_time(self, distance):
        '''Расчёт времени за сколько пройдёт машина заданную дистанцию
        в идеальных условиях'''
        time_to_distance = round(distance / self.speed, 2)
        return time_to_distance


my_car = Car('Volvo', 180, 10, 300_000)
print(my_car.get_price())
print(my_car.calc_to_time(10_000))
print()

print(my_car.__dict__)

json_data = json.dumps(my_car,
                       default=lambda obj_car: obj_car.__dict__,
                       ensure_ascii=False, indent=2)
print(json_data)

python_data = json.loads(json_data)
print(python_data)
print()

pickled_data = pickle.dumps(my_car, pickle.HIGHEST_PROTOCOL)
print(pickled_data)
depickled_data = pickle.loads(pickled_data)
print(depickled_data.__dict__)
