cursos = ['Matemáticas','Física','Química','Historia','Español']
notas =[]
for curso in cursos:
    nota = int(input(f'¿Cúal es tu nota es {curso}? '))    
    notas.append(nota)
for i in range(len(cursos)):
    print(f'En {cursos[i]} has sacado {notas[i]}')