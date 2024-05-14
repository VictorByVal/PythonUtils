from inversor_cadenas import * # Importaré este código debido a que voy a usarlo 

# Conversor de números a código binario 

def convertir_a_binario(numero): # Esto me va a dar el número binario pero invertido 
    binario = ""
    while numero > 0: 
        if numero % 2 == 0: 
            binario = binario + "0"
        if numero % 2 != 0 and numero != 1: 
            binario = binario + "1"
        if numero == 1: 
            binario = binario + "1"
            break
        numero = (numero - (numero % 2))/2
    print(invertir(binario)) # Aqui uso el código importado para usarlo con el resultado de la función anterior 
