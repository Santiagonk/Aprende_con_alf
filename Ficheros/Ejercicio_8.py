def call_csv(f):
  f = open(f, 'r')
  lineas = f.readlines()
  lineas = [i.replace('\n','').replace('%','').replace(',','.') for i in lineas] #.replace('.','').replace(',','.')
  lineas = [i.split(';') for i in lineas]
  return lineas

def lista_diccionarios(lineas):
  data = []
  for i in range(1,len(lineas)):
    diccionarios = {}
    for j in range(9):
      if lineas[i][j] == '':
        lineas[i][j] = '0'
      diccionarios[lineas[0][j]] = lineas[i][j]
    data.append(diccionarios)
  return data

def Nota_final(data):
  for j in data:

    if float(j["Parcial1"]) >= 4 or float(j["Parcial1"]) > float(j["Ordinario1"]):
      corte_1 = float(j["Parcial1"])
    else :
      corte_1 = float(j["Ordinario1"])

    if float(j["Parcial2"]) >= 4 or float(j["Parcial2"]) > float(j["Ordinario2"]):
      corte_2 = float(j["Parcial2"])
    else :
      corte_2 = float(j["Ordinario2"])

    if float(j["Practicas"]) >= 4 or float(j["Practicas"]) > float(j["OrdinarioPracticas"]):
      corte_p = float(j["Practicas"])
    else :
      corte_p = float(j["OrdinarioPracticas"])

    j["Nota Final"] = corte_1 * 0.3 +corte_2 * 0.3 + corte_p * 0.4
  
  return data

def aprobados_reprobados(data):
  aprobados = []
  reprobados = []
  for j in data:
    if j['Nota Final'] >= 4 and float(j['Asistencia']) >= 75:
      aprobados.append(j)
    else:
      reprobados.append(j)
  return aprobados, reprobados

def imprimir(lista):
  for j in lista:
    for word in j.keys():
      print(word," : ", str(j[word]))
    print("\n")

def main():
  f = 'calificaciones.csv'
  lineas = call_csv(f)
  lineas = lista_diccionarios(lineas)
  lineas = Nota_final(lineas)
  aprobados, reprobados = aprobados_reprobados(lineas)
  opcion = input('Desea ver lista de Aprobados 1) , de Reprobados 2): ')
  if opcion == '1':
    imprimir(aprobados)
  else:
    imprimir(reprobados)

if __name__ == "__main__":
    main()