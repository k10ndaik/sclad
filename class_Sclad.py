
class Sclad():
#класс склад
    def __init__(self, programm):
#нициализируем объекты класса
        self.programm = programm
#программа перемещений
        self.saveLine = []
#линия хранения ящиков
        self.work_engjy = 0
#затраченные ресурсы на перемещение
    def start(self):
        for box in self.programm:
            # цикл перебора ящиков во входяшеей программе перемещения
            work_box = box[0]
            # присваеваем тип действия над ящиков
            name_box = box[1]
            # присваеваем номер ящика
            if name_box in self.saveLine and work_box == 'принять':
                # проверяем нет ли ящик на хранение уже на линии
                print(f"Ящик {name_box} уже на линии хранения")
                continue
            # если есть то завершаем итерацию цикла
            elif work_box == 'принять':
                # приимаем ящики на хранение
                if name_box % 2 == 0:
                    self.saveLine.insert(0, name_box)
                    self.work_engjy += 1
                # не четные добавляем в конец
                else:
                    self.saveLine.append(name_box)
                    self.work_engjy += 1
            # четные в начало
            # распределяем ящики в конец или начало линии хранения
            # в зависимости от количества я щиков на линии
            elif work_box == 'выгрузить':
                if not name_box in self.saveLine:
                    print(f'Нет такого ящика {name_box} на хранение')
                    continue
                # проверяем есть ли такой ящик перед разгрузкой
                else:
                    number_box = self.saveLine.index(name_box)
                    # место харанения с 0
                    numbers_boxs = len(self.saveLine)
                    # определяем количество ящиков
                    self.work_engjy += (numbers_boxs - number_box)
                    # подсчет затрат на выгрузку
                    del self.saveLine[number_box]
        # выгружаем ящик
        print(f'остаток {self.saveLine}')
        print(f'затрачено ресурсов {self.work_engjy}')
    def energy(self):
        self.start()
        return self.work_engjy
    def ostatok(self):
        self.start()
        return self.saveLine