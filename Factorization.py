def Carpanlara_Ayirma(n):
    carpanlar = []
    for i in range(1, n+1):
        if n % i == 0:
            carpanlar.append(i)

    return carpanlar

Carpanlara_Ayirma(12)
