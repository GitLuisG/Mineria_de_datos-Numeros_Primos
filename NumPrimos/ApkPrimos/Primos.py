class NumerosPrimos(object):
    def __init__(self):
        pass

    def es_primo(self, i):
        i_es_primo = True
        for j in range(2, i, 1):
            if i % j == 0:
                i_es_primo = False
                break
        return i_es_primo   

print('Introduce el valor de "N":')
n = int(input())
npInstance = NumerosPrimos()
lista_primos = []
for i in range(2, n+1, 1):
    if npInstance.es_primo(i):
        lista_primos.append(str(i))
print('Total de numeros primos: {}', format(len(lista_primos)))
print(', '.join(lista_primos))
