def binario(num):
    binario = []
    
    while num > 0:
        binario.append(str(num % 2))
        num //=2
    binario.reverse()        
    return ''.join(binario)
def decimal(n):
    n = list(str(n))
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

if __name__ == "__main__":
    print(decimal(10110))
    
    print(binario(22))
 