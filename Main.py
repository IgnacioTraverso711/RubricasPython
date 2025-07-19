import os
def Crear_Punto_Rubrica(CantidadDeEjercicios,CantidadDeDivisiones):
    PuntoRubrica = []
    PuntajeRubrica = 100/CantidadDeEjercicios
    for x in range(CantidadDeDivisiones-1,-1,-1):
        try:
            PuntoRubrica.append(PuntajeRubrica/x)
        except ZeroDivisionError:
            PuntoRubrica.append(0)
    PuntoRubrica.sort()
    return PuntoRubrica

def Crear_Rubrica_Trabajo(CantidadDeEjercicios,Cantidad_Divisiones):
    Rubrica = []
    for x in range(CantidadDeEjercicios):
        Rubrica.append(Crear_Punto_Rubrica(CantidadDeEjercicios,Cantidad_Divisiones))
    return Rubrica

def Agregar_Puntuacion(Rubrica,PuntajeRubrica,PuntoActual):
        Puntaje =+ Rubrica[PuntoActual-1][PuntajeRubrica-1]
        return Puntaje

def CalcularPuntaje(Rubrica):
    Puntaje = 0
    Lista_Referencia = []
    Lista_Puntaje = []
    if len(Rubrica[0]) == 2:
        Lista_Referencia = ["1-NO RESUELTO","2-RESUELTO"]
    elif len(Rubrica[0]) == 3:
        Lista_Referencia = ["1-NO RESUELTO","2-REGULAR","3-PERFECTO"]
    elif len(Rubrica[0]) == 4:
        Lista_Referencia = ["1-NO RESUELTO","2-REGULAR","3-BIEN","4-PERFECTO"]
    elif len(Rubrica[0]) == 5:
        Lista_Referencia = ["1-NO RESUELTO","2-MAL","3-BIEN","4-MUY BIEN","5-PERFECTO"]
    for x in range(0,len(Rubrica),1):
        print("Punto actual:", x+1)
        print(Lista_Referencia)
        PuntajeUsuario = int(input("Ingrese Numero de puntaje:"))
        Puntaje += Agregar_Puntuacion(Rubrica,PuntajeUsuario,x)
        os.system('cls')
    return Puntaje

def Menu():
    Sigue = True
    while Sigue:
        Seleccion = int(input("""
                           
                                                SUPER RUBRICAS HENKO
                                                1- Determinar Rubrica
                                                2- Calificar
                                                3- INFO
                                                4- Terminar
                            
        """))
        os.system('cls')
        if Seleccion == 1:
            estabien = 0
            while not estabien:
                CantidadDeEjercicios = int(input("INGRESA CANTIDAD DE PUNTOS(minimo 2): "))
                Cantidad_Divisiones = int(input("INGRESA CANTIDAD DE DIVISIONES (minimo 2, maximo 5)"))
                os.system('cls')
                if  CantidadDeEjercicios >= 2 and Cantidad_Divisiones >=2 and Cantidad_Divisiones<=5:
                    print("SE CREO LA RUBRICA EXITOSAMENTE")
                    estabien = True
                else:
                    print("HUBO UN ERROR INTENTA OTRA VEZ")
                    estabien = False


        elif Seleccion == 2:
            Rubrica = Crear_Rubrica_Trabajo(CantidadDeEjercicios,Cantidad_Divisiones)
            PuntajeTotal = CalcularPuntaje(Rubrica)
            print(PuntajeTotal)
        elif Seleccion == 3:
            print("MOSTRAR INFO")
        elif Seleccion == 4:
            Sigue = False
        else:
            print("Numero no disponible usa uno disponible")


