import pandas as pd
import numpy as np


def Balance_por_mes(df, meses):
  df['Balance'] = df.Ventas - df.Gastos
  return df[df.Mes.isin(meses)].Balance.sum()


def main():
    df = pd.DataFrame([{'Mes': 'Enero', 'Ventas': 30500, 'Gastos': 22000},
              {'Mes': 'Febrero', 'Ventas': 35600, 'Gastos': 23400},
              {'Mes': 'Marzo', 'Ventas': 28300, 'Gastos': 18100},
              {'Mes': 'Abril', 'Ventas': 33900, 'Gastos': 20700}])

    meses = ['Marzo', 'Febrero']

    print(Balance_por_mes(df, meses))


if __name__ == "__main__":
    main()