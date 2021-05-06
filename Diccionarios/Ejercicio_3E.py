fruits = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruit = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruit in fruits:
    print(kg, 'kilos de', fruit, 'valen', fruits[fruit]*kg )
else: 
    print("Lo siento, la fruta", fruit, "no está disponible.")