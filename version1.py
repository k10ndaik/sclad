
def analyse(programm: list = [(str, int)]):
#функция обработки программы перемещений ящиков на складе
    saveLine = []
#линия хранения ящиков
    work_engjy = 0
#затраченные ресурсы на перемещение
    for box in programm:
#цикл перебора ящиков во входяшеей программе перемещения
        work_box = box[0]
#присваеваем тип действия над ящиков
        name_box = box[1]
#присваеваем номер ящика
        if name_box in saveLine and work_box == 'принять':
#проверяем нет ли ящик на хранение уже на линии
            print(f"Ящик {name_box} уже на линии хранения")
            continue
#если есть то завершаем итерацию цикла
        elif work_box == 'принять':
#приимаем ящики на хранение
            if name_box % 2 == 0:
                saveLine.insert(0, name_box)
                work_engjy += 1
#не четные добавляем в конец
            else:
                saveLine.append(name_box)
                work_engjy += 1
#четные в начало
#распределяем ящики в конец или начало линии хранения
# в зависимости от количества я щиков на линии
        elif work_box == 'выгрузить':
            if not name_box in saveLine:
                print(f'Нет такого ящика {name_box} на хранение')
                continue
#проверяем есть ли такой ящик перед разгрузкой
            else:
                number_box = saveLine.index(name_box)
#место харанения с 0
                numbers_boxs = len(saveLine)
#определяем количество ящиков
                work_engjy += (numbers_boxs - number_box)
#подсчет затрат на выгрузку
                del saveLine[number_box]
#выгружаем ящик
    print(f'остаток на складе {saveLine}')
    print(f'затарчено ресурсов{work_engjy}')
    return work_engjy
programm = [
 ('принять', 1),
 ('принять', 2),
 ('выгрузить', 1),
 ('принять', 3),
 ('принять', 4),
 ('выгрузить', 3),
]

analyse(programm)

def test_sclad(rez, program_rez):
    if rez == analyse(programm):
        print("Тест  пройден")
    else:
        print("Тест не пройден")

if __name__ == '__main__':
    analyse(programm)
    test_sclad(6, programm)


