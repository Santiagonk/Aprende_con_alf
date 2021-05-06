import pandas as pd

def ventas_año(años):
  ventas ={}
  for año in años:
    sales_per_year = []
    venta = float(input(f'Ingrese las ventas del {año}: '))
    sales_per_year.append(venta)
    sales_per_year.append(venta * 0.9)
    ventas[año] = sales_per_year
  return pd.Series(ventas)

def main():
    print(ventas_año(['2010', '2011', '2011', '2012', '2013']))

if __name__ == "__main__":
    main()