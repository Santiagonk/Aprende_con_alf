import pandas as pd
import numpy as np

def paso_numero(x):

  if len(x) > 5: 
    x = float(x.replace('.',''))
  else:    
    x = float(x) 

  return x

def main():
    df = pd.read_csv('cotizacion.csv', sep=';')
    df['Final'] = df['Final'].apply(lambda x: float(x.replace(',','.')))
    df['Máximo'] = df['Máximo'].apply(lambda x: float(x.replace(',','.')))
    df['Mínimo'] = df['Mínimo'].apply(lambda x: float(x.replace(',','.')))
    df['Volumen'] = df['Volumen'].apply(lambda x: paso_numero(x))
    df['Efectivo'] = df['Efectivo'].apply(lambda x: float(x.replace(',','.')))
    datos = { 'Nombre':['Final', 'Máximo',  'Mínimo', 'Volumen', 'Efectivo'],
          'Media':[np.mean(df['Final']), np.mean(df['Máximo']),  np.mean(df['Mínimo']), np.mean(df.Volumen), np.mean(df.Efectivo)],
          'Máximo':[ max(df.Final), max(df.Máximo),  max(df.Mínimo), max(df.Volumen), max(df.Efectivo)],
          'Mínimo':[ min(df.Final), min(df.Máximo),  min(df.Mínimo), min(df.Volumen), min(df.Efectivo)]}
    print(pd.DataFrame(datos))      

if __name__ == "__main__":
    main()