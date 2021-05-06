
num = int(input('Ingrese un numero entero: '))

if num == 1:
    primo = False
elif num == 2:
    primo = True
else:
    primo = True

for i in range(2,num):
    
    if num % i == 0:
        primo = False
    else:
        pass

if primo:
    print(f'{num} es un numero primo')
else:
    print(f'{num} no es un numero primo')