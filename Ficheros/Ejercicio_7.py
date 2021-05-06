import csv


def get_list(f):
  f = open(f, 'r')
  lineas = f.readlines()
  lineas = [i.replace('\n','').replace('.','').replace(',','.') for i in lineas]
  lineas = [i.split(';') for i in lineas]  

  return lineas

def By_columns(df):
  dic = {}
  lista = []
  for j in range(len(df[0][:])):
    for i in range(1,len(df)):
      lista.append(df[i][j])
    if j != 0:
      num = []
      for k in lista:
        num.append(float(k))
      lista = num 

    dic[df[0][j]] = lista
    lista = []

  return dic

def media(lista):
  return sum(lista)/len(lista)

def Summary(dic,g):
  myData = []
  for i in dic.keys():
    if i == 'Nombre':
      myData.append(["Nombre", "Minimo", "Maximo","Media"])
      
    else:
      lista = dic[i]
      myData.append([i, min(lista), max(lista), media(lista) ])

  myFile = open(g, 'w')
  with myFile:
      writer = csv.writer(myFile)
      writer.writerows(myData)

def main():
  f = 'cotizacion.csv'
  lista = get_list(f)
  lista = By_columns(lista)
  for i in lista.keys():
    print(f'Los valores de {i} son: \n{lista[i]}')
  g = "06_01_2021.csv"
  Summary(lista,g)




if __name__ == "__main__":
    main()
