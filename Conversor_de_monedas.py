# La librería empleada es yfinance
import yfinance as yf 

# Código para obtener el valor de un instrumento financiero 
def precio(id):
    # Lo que hace este comando es crear una función que tome como parámetro el ID de un instrumento 
    instrumento = yf.Ticker(id)
    # En base al ID emplea la función .ticker de yfinance para buscar el instrumento y añadirlo a una variable llamada instrumento
    historico = instrumento.history()
    # Busca el historial del instrumento seleccionado y lo guarda en una variable llamada historico como un DF
    cierre = historico['Close'].iloc[-1] 
    # Busca el último precio de cierre del DF del historico del instrumeno
    print(cierre)
    # Por último lo imprime 
# Código para obtener la conversión de una cifra, de una divisa a otra 
def convertir_divisa(cantidad, divisa):
    # Crea una función que tiene como parámetros la cantidad que se desea convertir y la divisa
    instrumento = yf.ticker(divisa)
    # Usa la función ticker de yfinance para buscar la divisa seleccionada y añadirla a una variable llamada instrumento
    historico = instrumento.history()
    # En base al instrumento seleccionado se busca su historial para así ser añadido a una variable llamada histórico
    cierre = historico['close'].iloc[-1]
    # Se busca dentro del Dataframe correspondiente el último precio de cierre del instrumento
    cantidad = cantidad/cierre
    # Por último se divide la cantidad que se desea convertir entre el último precio de cierre de la divisa y se imprime 
    print(cantidad)
precio('GBPUSD=X')
def historico(id):
    instrumento = yf.Ticker(id)
    historico = instrumento.history()
    print(historico)
historico('GBPUSD=X')


