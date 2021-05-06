
word = input('Introduce una palabra: ')

while word.lower() != 'salir':
    print(word,word[-1]*10,end ='!!!!')
    
    word = input('Introduce una palabra: ')