import pandas as pd
import numpy as np

def menor_edad(x):
  if x < 18:
    return True
  else:
    return False

def main():

    df = pd.read_csv('titanic.csv')

    filas, columnas = df.shape
    print(f'Numero de columnas: {columnas}\nNumero de filas: {filas}')
    print(f'Primeras 10 filas:\n {df.head(10)}')
    print(f'Ultimas 10 filas:\n {df.tail(10)}')

    print(df[df.PassengerId == 148])

    print(df[(df.PassengerId+1)%2 == 0])

    print(df[df.Pclass == 1].Name.sort_values())

    total_survived = df[df.Survived == 1].Survived.count()
    total_nonsurvived = df[df.Survived == 0].Survived.count()
    total = df.PassengerId.count()
    print(f'Porcentaje pasajeros sobrevivieron: {total_survived/total * 100} %\nPorcentaje pasajeros fallecieron: {total_nonsurvived/total *100} %')

    sobrevivieron = df[df.Survived == 1]
    P1 = sobrevivieron[sobrevivieron.Pclass == 1].PassengerId.count()
    P2 = sobrevivieron[sobrevivieron.Pclass == 2].PassengerId.count()
    P3 = sobrevivieron[sobrevivieron.Pclass == 3].PassengerId.count()
    print(f'Porcentaje pasajeros 1era clase: {P1/(P1 + P2 + P3) * 100} %\nPorcentaje pasajeros 2da clase: {P2/(P1 + P2 + P3) * 100} %\nPorcentaje pasajeros 3ra clase: {P3/(P1 + P2 + P3) * 100} %')

    df.reindex(index = pd.notna(df['Age']))
    df_Age = df.loc[pd.notna(df['Age']), : ]
    print(df_Age) 

    mujeres = df_Age[df_Age.Sex == 'female']
    P1_mujeres = mujeres[mujeres.Pclass == 1]
    P2_mujeres = mujeres[mujeres.Pclass == 2]
    P3_mujeres = mujeres[mujeres.Pclass == 3]
    print(f'Edad media mujeres 1era clase: {np.mean(P1_mujeres.Age)} \nEdad media mujeres 2da clase: {np.mean(P2_mujeres.Age)}\nEdad media mujeres 3era clase: {np.mean(P3_mujeres.Age)}')
  
    df_Age['Menor_edad']=df_Age['Age'].apply(lambda x: menor_edad(x))

    Primera_clase = df_Age[df_Age.Pclass == 1]
    Segunda_clase = df_Age[df_Age.Pclass == 2]
    Tercera_clase = df_Age[df_Age.Pclass == 3]

    men_P1_S =  Primera_clase[Primera_clase.Menor_edad == True]['Survived'].sum()/ len(Primera_clase[Primera_clase.Menor_edad == True])
    ma_P1_S =   Primera_clase[Primera_clase.Menor_edad == False]['Survived'].sum()/ len(Primera_clase[Primera_clase.Menor_edad == False])
    print(f'Porcentaje de menores de edad sobrevivieron en 1era clase: {men_P1_S * 100}\nPorcentaje de mayores de edad sobrevivieron en 1era clase: {ma_P1_S * 100}')

    men_P2_S =  Segunda_clase[Segunda_clase.Menor_edad == True]['Survived'].sum()/ len(Segunda_clase[Segunda_clase.Menor_edad == True])
    ma_P2_S =   Segunda_clase[Segunda_clase.Menor_edad == False]['Survived'].sum()/ len(Segunda_clase[Segunda_clase.Menor_edad == False])
    print(f'Porcentaje de menores de edad sobrevivieron en 2da clase: {men_P2_S * 100}\nPorcentaje de mayores de edad sobrevivieron en 2da clase: {ma_P2_S * 100}')

    men_P3_S =  Tercera_clase[Tercera_clase.Menor_edad == True]['Survived'].sum()/ len(Tercera_clase[Tercera_clase.Menor_edad == True])
    ma_P3_S =   Tercera_clase[Tercera_clase.Menor_edad == False]['Survived'].sum()/ len(Tercera_clase[Tercera_clase.Menor_edad == False])
    print(f'Porcentaje de menores de edad sobrevivieron en 3era clase: {men_P3_S * 100}\nPorcentaje de mayores de edad sobrevivieron en 3era clase: {ma_P3_S * 100}')

if __name__ == "__main__":
    main()