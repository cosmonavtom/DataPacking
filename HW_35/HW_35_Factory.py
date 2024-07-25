from abc import ABC, abstractmethod

'''Будем делать через паттерн Фабрики, для наибольшей гибкости и разнообразия'''


class Pasta(ABC):
    '''Тут на данный момент достаточно класса Pasta(ABC), но скорее всего в дальнейшем мы будем
       расширяться и торговать ещё пиццей(есть такое подозрение). А так бы я разбил на несколько
       классов от (ABC) (Type_product(ABC), Sauce(ABC), etc) от которых потом и наследовался
       необходимый продукт. Но не буду бежать впереди паровоза =)'''

    
    @abstractmethod
    '''Добавил метод pasta_name для возврата названия пасты. Надеюсь я правильно понял, что
    название пасты и тип пасты из которой она приготовлена это не одно и тоже(по крайней мере
    не всегда'''
    def pasta_name(self):
        pass

    @abstractmethod
    def pasta_type(self):
        pass

    @abstractmethod
    def sauce(self):
        pass

    @abstractmethod
    def filling(self):
        pass

    @abstractmethod
    def supplements(self):
        pass


'''А вот это три конкретных класса'''


class Carbonara(Pasta):
    def pasta_name(self):
        return 'Карбонара'

    def pasta_type(self):
        return 'Спагетти'

    def sauce(self):
        return 'Соус из яиц и сыра "Пекарино Романо"'

    def filling(self):
        return 'Бекон'

    def supplements(self):
        return 'Чёрный перец'


class Bolognese(Pasta):
    def pasta_name(self):
        return 'Болоньезе'

    def pasta_type(self):
        return 'Тальятелле'

    def sauce(self):
        return 'Томатный соус'

    def filling(self):
        return 'Мясной фарш, томаты'

    def supplements(self):
        return 'Морковь, вино'


class Fettuccine(Pasta):
    def pasta_name(self):
        return 'Фетучини'

    def pasta_type(self):
        return 'Фетучини'

    def sauce(self):
        return "Грибной соус"

    def filling(self):
        return "Пармезан, сливочное масло"

    def supplements(self):
        return "Оливковое масло"


class PastaFactory:
    '''Непосредственно сама Фабрика где собираем пасту'''

    @staticmethod
    def create_pasta(pasta_choice):
        if pasta_choice == 1:
            return Carbonara()
        elif pasta_choice == 2:
            return Bolognese()
        elif pasta_choice == 3:
            return Fettuccine()
        else:
            raise ValueError('Пока на выбор только три пасты')


def pasta_menu():
    '''Небольшое меню для удобства тестирования'''
    choice = int(input('Выберите пасту:\n1 - Карбонара\n2 - Болоньезе\n3 - Фетучини\nВыш выбор: '))
    pasta = PastaFactory.create_pasta(choice)
    print(f'Вы выбрали пасту {pasta.pasta_name()}')
    print(f"Тип пасты: {pasta.pasta_type()}")
    print(f"Соус: {pasta.sauce()}")
    print(f"Начинка: {pasta.filling()}")
    print(f"Добавки: {pasta.supplements()}")

pasta_menu()
