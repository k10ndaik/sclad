from class_Sclad import Sclad
programm = [
 ('принять', 1),
 ('принять', 2),
 ('выгрузить', 1),
 ('принять', 3),
 ('принять', 4),
 ('выгрузить', 3),
]

dpd = Sclad(programm)


def test_sclad(rez, program_rez):
    if rez == program_rez:
        print("Тест  пройден")
    else:
        print("Тест не пройден")

test_sclad(6, dpd.energy())