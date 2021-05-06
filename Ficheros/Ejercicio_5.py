from urllib import request
from urllib.error import URLError

def det_pib(url, country = 'ES'):
  '''
  Funcion toma una url y un codigo de pais, y devuelve diccionario con los PIBs por año del pais seleccionado
  - url variable tipo string con la url deseada
  - country el codigo del pais
  '''
  
  try:
     f = request.urlopen(url)
  except URLError:
    return('!la url ' + url + 'no existe!')
  else:
    data = f.read().decode('utf-8').split('\n') # tomamos datos y codificamos a utf-8 y separamos por /n queden filas con datos por pais
    data = [i.split('\t') for i in data] #separamos cada fila por /n queden separados por años
    data = [list(map(str.strip, i)) for i in data] #Retiramos los espacios vacios de cada string con la funcion strip dentro del map
    for i in data:
      i[0] = i[0].split(',')[-1] #Tomamos el codigo de cada pais
    data[0][0] = 'year' # renombramos el espacio de la primera columna y primera fila con 'año'
    
    
    data = {i[0]:i[1:] for i in data} # pasamos a un diccionario con la informacion por cada pais
    result ={data['year'][i]:data[country][i] for i in range(len(data['year']))} # guardamos el pib por año del pais seleccionado
    return result


def main():
    country = input('Introduce el codigo del país: ')
    url ='https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true'

    result= det_pib(url, country)
    print('El PIB por año de ',country,' es: ')
    print('año','\t', 'PIB')

    for word in result:
        print(word + '\t' + result[word])
 

if __name__ == "__main__":
    main()