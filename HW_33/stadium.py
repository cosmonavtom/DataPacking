import pickle, json
from datetime import date


class Stadium:

    def __init__(self, name, capacity: int, since: int):
        '''Инитим название стадиона, вместимость и год основания'''
        self.name = name
        self.capacity = capacity
        self.since = since

    def get_age(self):
        '''Возвращает возраст стадиона'''
        age_stadion = date.today().year - self.since
        return age_stadion

    def capacity_check(self, capacity=None):
        '''Проверка на вместимость стадиона. True - все влезут. False - не все'''
        if capacity is None:
            return None
        if capacity <= self.capacity:
            return True
        return False


class JSONDataAdapter:
    @staticmethod
    def to_json(o):
        if isinstance(o, Stadium):
            return json.dumps({
                'Name': o.name,
                'Capacity': o.capacity,
                'Since': o.since,
                'Methods': {
                    'get_age': o.get_age(),
                    'capacity_check': o.capacity_check()
                }
            })

    @staticmethod
    def from_json(o):
        o = json.loads(o)
        return o


my_stadium = Stadium('Luzhniki Stadium', 73_189, 1956)
print(my_stadium.__dict__)
print(my_stadium.get_age())
print(my_stadium.capacity_check(70_000))
print()

with open('stadium.pickle', 'wb') as f:
    pickle.dump(my_stadium, f)
with open('stadium.pickle', 'rb') as f:
    python_data_from_file = pickle.load(f)
print(python_data_from_file.__dict__)
print()

json_data = JSONDataAdapter.to_json(my_stadium)
print(json_data)
python_data_from_json = JSONDataAdapter.from_json(json_data)
print(python_data_from_json)
