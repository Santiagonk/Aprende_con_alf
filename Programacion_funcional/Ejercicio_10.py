from datetime import datetime

def ZonaA(diccionario):
    antiguedad = datetime.now().year - diccionario["año"]
    return (diccionario["metros"]*1000 + diccionario["habitaciones"]*5000 + diccionario["habitaciones"]*15000)*(1 - antiguedad/100)  

def ZonaB(diccionario):
    antiguedad = datetime.now().year - diccionario["año"]
    return (diccionario["metros"]*1000 + diccionario["habitaciones"]*5000 + diccionario["habitaciones"]*15000)*(1 - antiguedad/100)*1.5  

def SelectByZone(lista):
    
    for diccionario in lista:
        if diccionario['zona'] == 'A':
            diccionario["precio"] = ZonaA(diccionario)
        elif diccionario['zona'] == 'B':
            diccionario["precio"] = ZonaB(diccionario)
    
    return lista

def EnElPresupuesto(lista, presupuesto):
    aptos_presupuesto = []
    for diccionario in lista:
        if diccionario['precio'] <= presupuesto:
            aptos_presupuesto.append(diccionario)
    
    return aptos_presupuesto

def Select_aptos(inmuebles, presupuesto):
    seleccionados = SelectByZone(inmuebles)
    seleccionados = EnElPresupuesto(inmuebles, presupuesto)
    return seleccionados
            



def main():
    presupuesto = float(input("Ingrese su presupuesto: "))
    inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
                    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
                    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
                    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
                    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}] 
    print(f'Los apartamentos en la lista son: \n')
    personas = map(lambda x: x,SelectByZone(inmuebles))
    for persona in personas:
        print("\n"+str(persona))
    print(f'Los apartamentos seleccionados son: ') 
    personas = map(lambda x: x,Select_aptos(inmuebles, presupuesto))
    for persona in personas:
        print("\n"+str(persona))     

if __name__ == "__main__":
    main()