def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

numeros = [3, 4, 8, 5, 5, 22, 13]
primos = [numero for numero in numeros if es_primo(numero)]

print(primos)
