import pandas as pd
import numpy as np


def notas_summary(datos):
  datos = pd.DataFrame(datos)
  s ={'minimo': datos['nota'].min(), 'maxima':datos['nota'].max(), 'media': np.mean(datos['nota']), 'desviacion': np.std(datos['nota'])}
  return pd.Series(s)


def main():
    print(notas_summary(datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],         
         'nota':[3.5, 5, 4.5, 2]}))

if __name__ == "__main__":
    main()