class Tiler:
    def prepare_floor(self):
        return 'Пол подготовлен'

    def lay_tiles(self):
        return 'Плитка уложена'


class Finisher:
    def apply_putty(self):
        return 'Шпаклёвка нанесена'

    def plaster_the_walls(self):
        return 'Стены отштукатурены'


class Painter:
    def prime_the_walls(self):
        return 'Стены загрунтованы'

    def paint_the_walls(self):
        return 'Стены покрашены'


class Foreman:
    def __init__(self):
        self.tiler = Tiler()
        self.finisher = Finisher()
        self.painter = Painter()

    def make_floors(self):
        result = f'Делаем полы:\n\t{self.tiler.prepare_floor()}\n\t{self.tiler.lay_tiles()}'
        return result

    def level_walls(self):
        result = f'Обрабатываем стены:\n\t{self.finisher.apply_putty()}\n\t{self.finisher.plaster_the_walls()}'
        return result

    def paint_walls(self):
        result = f'Красим стены:\n\t{self.painter.prime_the_walls()}\n\t{self.painter.paint_the_walls()}'
        return result

    def turnkey_work(self):
        results = []
        results.append('Работа под ключ!')
        results.append(self.make_floors())
        results.append(self.level_walls())
        results.append(self.paint_walls())
        return '\n* '.join(results)


foreman = Foreman()
print(foreman.turnkey_work())
# print(foreman.paint_walls())
# finisher = Finisher()
# print(finisher.apply_putty())
