import random
from timeit import default_timer
ficha = 50
apuestas = 0

def jugadas(apuestas, ficha):
 population = ["gano","perdió"]
 weights = [0.4 , 0.6]
 juego = 0

 while juego < 300 and ficha > 0:
        juego += 1
        if random.choices(population,weights) == ["perdió"] :
            ficha -= 1
            apuestas += 1
        else:
            ficha += 1
            apuestas += 1

 return (apuestas),(ficha)

promedio_apuestas = []
sesiones = 0
while sesiones < 20:
    Start = default_timer ()
    sesiones += 1
    apuestasos, fichas = jugadas(apuestas, ficha)
    End = default_timer () 
    print("tiempo de sesión", sesiones,"=", (End - Start) ,"segundos,","cantidad de apuestas",apuestasos, "cantidad de fichas que me quedaron de la sesión", fichas)
    promedio_apuestas.append(apuestasos)
    
    
       
print ("pudiste apostar en promedio despues de 20 intentos =",sum(promedio_apuestas)/sesiones)

