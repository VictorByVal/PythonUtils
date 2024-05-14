import random # Esta es una biblioteca estándar de Python 
'''Esta función genera un volado de manera individual y lo regresa al usuario'''
moneda = {"cara":1, "cruz":2}
def volado():
    volado = random.randint(0,3)
    def seleccion(volado): 
        if volado == moneda["cara"]:
            print("Cara")
        else: 
            print("Cruz")
    seleccion(volado)
# Volado multiple
'''Genera un volado por cada número de veces establecido por el usuario, regresa la cantidad de veces que salió cara y que salió cruz'''
lista = []
def voladosmultiples(veces):
    vez = 0
    while vez < veces: 
        volado = random.randint(0,3)
        if volado == moneda["cara"]: 
            lista.append("Cara")
        else: 
            lista.append("Cruz") 
        vez += 1            
# Porcentaje de victorias y derrotas 
'''Crea una función que retorna un valor porcentual de victorias sobre las caras y cruces de una cantidad de volados determinada por el usuario'''
def porcentaje_de_victorias(veces):
    contadorcaras = 0
    contadorcruces = 0
    voladosmultiples(veces)
    for elemento in lista: 
        if elemento == "Cara": 
            contadorcaras += 1
        if elemento == "Cruz":
            contadorcruces += 1
    porcentajecaras = (contadorcaras/len(lista))*100
    porcentajecruces = (contadorcruces/len(lista))*100
    print(f"El porcentaje de victoria para las caras fue de: {porcentajecaras}%")
    print(f"El porcentaje de victorias para las cruces fue de: {porcentajecruces}%")


