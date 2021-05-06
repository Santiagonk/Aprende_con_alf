cursos = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
pasados = []
for curso in cursos:
    nota = float(input(f'¿Qué nota tienes en {curso}? '))
    if nota >= 5:
        pasados.append(curso)
for curso in pasados:
    cursos.remove(curso)
print(f'Tienes que repetir: ')
print(cursos)