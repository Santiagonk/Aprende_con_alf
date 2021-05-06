def MCD(num_1, num_2):
    
    if num_1 > num_2:
        cociente = num_1 // num_2
        resto = num_1 - cociente * num_2
        if resto == 0:
            return num_2
        else:
            return MCD(num_2, resto)
    else:
        cociente = num_2 // num_1
        resto = num_2 - cociente * num_1
        if resto == 0:
            return num_1
        else:
            return MCD(num_1, resto) 

def MCM(num_1, num_2):
    return (num_1 * num_2)/MCD(num_1, num_2)

if __name__ == "__main__":
    print(MCD(24, 36))
    print(MCM(24, 36))