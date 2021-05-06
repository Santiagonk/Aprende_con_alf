
renta = float(input('¿Cuál es tu renta? '))

if renta < 10000:
    print('Tu impositivo es del 5%')
elif renta >= 10000 and renta < 20000:
    print('Tu impositivo es del 15%')
elif renta >= 20000 and renta < 35000:
    print('Tu impositivo es del 20%')
elif renta >= 35000 and renta < 60000:
    print('Tu impositivo es del 30%')
else:
    print('Tu impositivo es del 45%')
