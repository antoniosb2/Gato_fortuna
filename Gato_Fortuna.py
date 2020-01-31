from random import randint
from time import sleep
c = c2 = 0
gemas = int(input('Quantidade de gemas: '))
while True:
    c += 1
    if gemas>=20:
        sort1= randint(20,28)-20
        gemas += sort1
        print(f'Ganho de gemas [20,28]: \033[1;36m{sort1}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)

    else:
        print('Quantidade insuficiente de gemas!')
        break
    if gemas>=30:
        sort2= randint(30,48)-30
        gemas += sort2
        print(f'Ganho de gemas [30,48]: \033[1;36m{sort2}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)
    else:
        print('Quantidade insuficiente de gemas!')
        break
    if gemas>=65:
        sort3= randint(65,88)-65
        gemas += sort3
        print(f'Ganho de gemas [65,88]: \033[1;36m{sort3}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)
    else:
        print('Quantidade insuficiente de gemas!')
        break
    if gemas>=150:
        sort4= randint(150,188)-150
        gemas += sort4
        print(f'Ganho de gemas [150,188]: \033[1;36m{sort4}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)
    else:
        print('Quantidade insuficiente de gemas!')
        break
    if gemas>=240:
        sort5= randint(240,288)-240
        gemas += sort5
        print(f'Ganho de gemas [240,288]: \033[1;36m{sort5}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)
    else:
        print('Quantidade insuficiente de gemas!')
        break
    if gemas>=330:
        sort6= randint(330,388)-330
        gemas += sort6
        print(f'Ganho de gemas [330,388]: \033[1;36m{sort6}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)
    else:
        print('Quantidade insuficiente de gemas!')
        break
    if gemas>=500:
        sort7= randint(500,588)-500
        gemas += sort7
        print(f'Ganho de gemas [500,588]: \033[1;36m{sort7}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)
    else:
        print('Quantidade insuficiente de gemas para próxima rodada!!')
        break
    if gemas>=660:
        sort8 = randint(660,888)-660
        gemas += sort8
        print(f'Ganho de gemas [660,888]: \033[1;36m{sort8}\033[0;0m')
        print(f'TOTAL ACUMULADO: \033[1;32m{gemas}\033[0;0m')
        sleep(1)
        print('\033[1;33m=.=\033[0;0m' * 10)
        break




