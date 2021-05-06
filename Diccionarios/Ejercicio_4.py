meses = {'01':'Enero',
        '02':'Febrero',
        '03':'Marzo',
        '04':'Abril',
        '05':'Mayo',
        '06':'Junio',
        '07':'Julio',
        '08':'Agosto',
        '09':'Septiembre',
        '10':'Octubre',
        '11':'Noviembre',
        '12':'Diciembre'}
print('Ingrese la fecha en el formato dd/mm/aaaa: ')
dia = input('dia: ')
mes = input('mes: ')
año = input('año: ')
print(dia," de ",meses[mes]," de ",año)
