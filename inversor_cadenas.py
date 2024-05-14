def invertir(cadena): # Esto invierte el caracter o conjunto de caracteres ingresados
    inversa = []
    derecha = len(cadena) - 1
    for elemento in cadena: 
        inversa.append(cadena[derecha])
        derecha -= 1
    inversa = "".join(inversa) 
    return inversa