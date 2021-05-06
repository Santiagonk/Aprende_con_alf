import pandas as pd
import numpy as np


def ordenar_notas(notas):
  s = pd.Series(notas)
  return s.sort_values(ascending=False)


def main():
    print(ordenar_notas({'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}))


if __name__ == "__main__":
    main()