def factorial (n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n."""
    if n == 1:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    
    print(factorial(4))
    print(factorial(5))
    print(factorial(10))