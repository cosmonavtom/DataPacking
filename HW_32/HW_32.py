import pickle


class CountryState:

    def __init__(self, country_dict=None):
        if country_dict is None:
            country_dict = {}
        self.country_dict = country_dict

    def add_cd(self, country, capital):
        '''Добавляем в словарь Страну:Столицу. Сокращение cd от country_dict'''
        self.country_dict.update({country: capital})

    def rem_cd(self, country):
        '''Удаляем пару ключ:значение по ключу'''
        if self.country_dict.get(country):
            self.country_dict.pop(country)
        return f'Ключ {country} не найден'

    def check_cd(self, country):
        '''Проверяем наличия ключа в словаре'''
        if self.country_dict.get(country):
            return True
        return False

    def search_by_key(self, country):
        '''Поиск значение по ключу'''
        if self.country_dict.get(country):
            return self.country_dict[country]
        return f'Ключ {country} не найден'

    def search_by_value(self, capital):
        '''Поиск ключа по значению'''
        for key, value in self.country_dict.items():
            if capital == value:
                return key
        return f'Значение {capital} не найдено'


    def show_cd(self):
        '''Вывод словаря на экран'''
        print(self.country_dict)

    def change_cd(self, country, capital):
        if self.country_dict.get(country):
            self.country_dict[country] = capital
            return f'Ключ {country} получил значение {capital}'
        return f'Ключ {country} не найден'

    def save_cd(self, file):
        '''Сохраняем словарь в файл используя pickle'''
        with open(file, 'wb') as f:
            pickle.dump(self.country_dict, f, protocol=5)

    def load_cd(self, file):
        '''Распаковываем в наш словарь данные из файла'''
        with open(file, 'rb') as f:
            self.country_dict = pickle.load(f)


# test_cc = CountryState()
# test_cc.add_cd('Russia', 'Moscow')
# test_cc.add_cd('Belarus', 'Minsk')
# test_cc.add_cd('China', 'Beijing')
# test_cc.show_cd()
# test_cc.rem_cd('China')
# test_cc.show_cd()
# print(test_cc.check_cd('Russia'))
# print(test_cc.check_cd('Germany'))
# test_cc.save_cd('country_dict.pickle')
# test_cc.add_cd('China', 'Beijing')
# test_cc.show_cd()
# test_cc.load_cd('country_dict.pickle')
# test_cc.show_cd()
# test_cc.change_cd('Russia', 'Saint-Petersburg')
# test_cc.show_cd()
# print(test_cc.search_by_key('Belarus'))
# print(test_cc.search_by_value('Minsk'))
