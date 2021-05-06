def words_file(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        file = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        content = file.read()
        return len(content.split())

def main():

    print(words_file('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))
    print(words_file('https://no-existe.txt'))

if __name__ == "__main__":
    main()