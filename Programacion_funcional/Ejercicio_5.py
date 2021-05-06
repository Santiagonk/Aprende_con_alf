def diccionario(lista):
    dic = {}
    for i in range(len(lista)):
        dic[lista[i]]=len(lista[i])

    return dic

def divide_per_words(lista):

    per_words = lista.replace("!"," ")
    per_words = per_words.replace(",","").replace(".","").replace("(","").replace(")","").split(" ")
    per_words = minusculas(per_words)
    return per_words


def minusculas(lista):
  for i in range(len(lista)):
    lista[i]=lista[i].lower()
  return lista


def words_to_dic(frase):
    frase = divide_per_words(frase)
    dictionary, longitud = diccionario(frase)


def main():
    frase = input("Ingresa una frase: ")
    frase = divide_per_words(frase)
    frase = diccionario(frase)
    print(f'el diccionario es el siguiente:\n {frase}')

    


if __name__ == "__main__":
    main()