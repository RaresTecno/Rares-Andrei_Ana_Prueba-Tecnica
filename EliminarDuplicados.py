def eliminarDuplicados(lista):
    vistos = set()
    resultado = []
    for n in lista:
        if n not in vistos:
            vistos.add(n)
            resultado.append(n)
    return resultado

entrada = [3, 5, 2, 3, 8, 5, 2, 10]
salida = eliminarDuplicados(entrada)
print(salida)  #[3, 5, 2, 8, 10]


#Otra manera de hacerlo
def eliminarDuplicados2(lista):
    return list(dict.fromkeys(lista))

entrada2 = [3, 5, 2, 3, 8, 5, 2, 10]
salida2 = eliminarDuplicados(entrada2)
print(salida2)  #[3, 5, 2, 8, 10]