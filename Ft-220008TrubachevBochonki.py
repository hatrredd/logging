import random as ran
import logging
logging.basicConfig(level=logging.DEBUG, filename='logging.log', format='%(levelname)s (%(asctime)s): %(message)s', datefmt='%d/%m/%Y %I:%M:%S', encoding='utf-8')
logging.info('Программа была запущена')
Nmas = []
N = int(input("Введите число бочонков в мешочке: "))
while N < 1:
    N = int(input("Вы ввели некорректное число, попробуйте ещё раз: "))
logging.info("Число бочонков в мешочке: " + str(N))
for i in range(N):
    Nmas.append(i+1)
print("Нажмите Enter, чтобы достать бочонок из мешочка\nВведите 'Stop', чтобы завершить программу")
while len(Nmas) > 0:
    cont = input()
    cont.lower()
    if cont == "stop":
        break
    else:
        b = ran.randint(0, len(Nmas)-1)
        print("Вы достали бочонок под номером - ", Nmas[b], end="")
        logging.info('Вы достали бочонок под номером - ' + str(Nmas[b]))
        Nmas.pop(b)
logging.info('Программа была завершена')