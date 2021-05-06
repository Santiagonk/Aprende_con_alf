from urllib import request

def main():
    f = request.urlopen('https://www.gutenberg.org/cache/epub/2000/pg2000.txt')

    datos = f.read()
    datos = datos.decode('utf-8')
    
    datos_format = datos.replace("#"," ").replace("\n"," ").replace("\r"," ").replace("(","").replace(")","").replace(":","").split(" ")
    
    datos_format2 = []
    for word in datos_format:
        if word == '':
            pass
        else:
            datos_format2.append(word)
    print(len(datos_format2))


if __name__ == "__main__":
    main()