import pandas as pd
import numpy as np
from datetime import date, time, datetime

def dias(x):
    return x.replace('D','')


def mes(x):
  if x < 10:
    return '0'+str(x)
  else:
    return str(x)


def emision(df,fecha1, fecha2, magnitud, estacion):  
  return df[(df.FECHA > fecha1) & (df.FECHA < fecha2) & (df.MAGNITUD == magnitud) & (df.ESTACION == estacion)].loc[:,['FECHA','EMISION']]
  

def resumen_est_cot(df, estacion, magnitud):
  print(f'Maximo de emision en estacion: {estacion} y contaminante: {magnitud}: ',df[(df.ESTACION == estacion) & (df.MAGNITUD == magnitud)]['EMISION'].max())
  print(f'Minimo de emision en estacion: {estacion} y contaminante: {magnitud}: ',df[(df.ESTACION == estacion) & (df.MAGNITUD == magnitud)]['EMISION'].min())
  print(f'Media de emision en estacion: {estacion} y contaminante: {magnitud}: ',df[(df.ESTACION == estacion) & (df.MAGNITUD == magnitud)]['EMISION'].mean())


def emision_mes_estacion(df,anio, magnitud):  
  return df[(df.ANO == anio) & (df.MAGNITUD == magnitud)].groupby(['ESTACION','MES'])['EMISION'].mean().unstack('MES')


def emision_magnitud_mes(df,estacion):
  return df[(df.ESTACION == estacion) ].groupby(['MAGNITUD','MES'])['EMISION'].mean().unstack('MES')



def main():
    df_2016 = pd.read_csv('emisiones-2016.csv', sep = ';')
    df_2017 = pd.read_csv('emisiones-2017.csv', sep = ';')
    df_2018 = pd.read_csv('emisiones-2018.csv', sep = ';')
    df_2019 = pd.read_csv('emisiones-2019.csv', sep = ';')

    df = pd.concat([df_2016, df_2017, df_2018, df_2019])    

    df = df.melt(id_vars=['ESTACION', 'MAGNITUD',	'ANO', 'MES'], var_name='DIA', value_name = 'EMISION')

    df['DIA'] = df['DIA'].apply(lambda x: dias(x)) 

    df['MES'] = df['MES'].apply(lambda x: mes(x)) 

    df['FECHA'] = df['ANO'].astype('string')+'/'+df['MES']+'/'+df['DIA'].astype('string')

    df['FECHA'] = pd.to_datetime(df.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')

    df = df.drop(df[np.isnat(df.FECHA)].index)

    print('Estaciones: ',df['ESTACION'].unique())
    print('Magnitud: ',df['MAGNITUD'].unique())

    print(emision(df,'2016-05-11','2016-12-01',7,11))

    
    df['EMISION'] = df['EMISION'].astype('float64')
    # print(df.info())
    mag_max = df.groupby(['MAGNITUD'])['EMISION'].max()
    mag_min = df.groupby(['MAGNITUD'])['EMISION'].min()
    mag_mean = df.groupby(['MAGNITUD'])['EMISION'].mean()


    print(f'Maximo de emision por contaminante: {mag_max}')
    print(f'Minimo de emision por contaminante: {mag_min}')
    print(f'Media de emision por contaminante: {mag_mean}')

    print('Maximo de emision por estacion y contaminante: ',df.groupby(['ESTACION','MAGNITUD'])['EMISION'].max())
    print('Minimo de emision por estacion y contaminante: ',df.groupby(['ESTACION','MAGNITUD'])['EMISION'].min())
    print('Media de emision por estacion y contaminante: ',df.groupby(['ESTACION','MAGNITUD'])['EMISION'].mean())

    resumen_est_cot(df, 4, 12)

    print(emision_mes_estacion(df,2017, 6))

    print(emision_magnitud_mes(df,4))



if __name__ == "__main__":
    main()