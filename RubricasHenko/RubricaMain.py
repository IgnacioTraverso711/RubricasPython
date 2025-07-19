import os
import tkinter as tk
from tkinter import ttk

Ventana = tk.Tk()
Ventana.title("Rubricas HENKO")
Ventana.geometry("700x400")
Ventana.resizable(width=False, height=False)

def Crear_Punto_Rubrica(CantidadDeEjercicios, CantidadDeDivisiones):
    PuntoRubrica = []
    PuntajeRubrica = 100 / CantidadDeEjercicios
    for x in range(CantidadDeDivisiones - 1, -1, -1):
        try:
            PuntoRubrica.append(PuntajeRubrica / x)
        except ZeroDivisionError:
            PuntoRubrica.append(0)
    PuntoRubrica.sort()
    return PuntoRubrica
def Crear_Rubrica_Trabajo(CantidadDeEjercicios, Cantidad_Divisiones):
    Rubrica = []
    for x in range(CantidadDeEjercicios):
        Rubrica.append(Crear_Punto_Rubrica(CantidadDeEjercicios, Cantidad_Divisiones))
    return Rubrica
def Agregar_Puntuacion(Rubrica, PuntajeRubrica, PuntoActual):
    Puntaje = + Rubrica[PuntoActual - 1][PuntajeRubrica - 1]
    return Puntaje
def CalcularPuntaje(Rubrica):
    Puntaje = 0
    Lista_Referencia = []
    Lista_Puntaje = []
    if len(Rubrica[0]) == 2:
        Lista_Referencia = ["1-NO RESUELTO", "2-RESUELTO"]
    elif len(Rubrica[0]) == 3:
        Lista_Referencia = ["1-NO RESUELTO", "2-REGULAR", "3-PERFECTO"]
    elif len(Rubrica[0]) == 4:
        Lista_Referencia = ["1-NO RESUELTO", "2-REGULAR", "3-BIEN", "4-PERFECTO"]
    elif len(Rubrica[0]) == 5:
        Lista_Referencia = ["1-NO RESUELTO", "2-MAL", "3-BIEN", "4-MUY BIEN", "5-PERFECTO"]
    for x in range(0, len(Rubrica), 1):
        print("Punto actual:", x + 1)
        print(Lista_Referencia)
        PuntajeUsuario = int(input("Ingrese Numero de puntaje:"))
        Puntaje += Agregar_Puntuacion(Rubrica, PuntajeUsuario, x)
        os.system('cls')
    return Puntaje
def MenuConsola():
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
                if CantidadDeEjercicios >= 2 and Cantidad_Divisiones >= 2 and Cantidad_Divisiones <= 5:
                    print("SE CREO LA RUBRICA EXITOSAMENTE")
                    estabien = True
                else:
                    print("HUBO UN ERROR INTENTA OTRA VEZ")
                    estabien = False


        elif Seleccion == 2:
            Rubrica = Crear_Rubrica_Trabajo(CantidadDeEjercicios, Cantidad_Divisiones)
            PuntajeTotal = CalcularPuntaje(Rubrica)
            print(PuntajeTotal)
        elif Seleccion == 3:
            print("MOSTRAR INFO")
        elif Seleccion == 4:
            Sigue = False
        else:
            print("Numero no disponible usa uno disponible")


def MenuVentana():
    notebook = ttk.Notebook(Ventana)
    notebook.pack(fill='both', expand=True)

    # Pestaña principal
    frame1 = ttk.Frame(notebook)
    notebook.add(frame1, text='RUBRICAS')
    Boton_Definir = tk.Button(frame1, text="Definir Rubrica",height=5,width=30, command=lambda: Menu_Designar_Rubrica())
    Boton_Calificar = tk.Button(frame1, text="Calificar",height=5,width=30)
    Boton_Salir = tk.Button(frame1, text="Salir",height=5,width=30, command=Ventana.destroy)
    Boton_Definir.pack(pady=10)
    Boton_Calificar.pack(pady=10)
    Boton_Salir.pack(pady=10)

    # Pestaña informacion
    frame2 = ttk.Frame(notebook)
    label1 = tk.Label(frame2, text="""
    Se pueden generar hasta 5 calificaciones por punto, las calificaciones seran las siguientes:
    
    Para 2 calificaciones: ["1-NO RESUELTO", "2-RESUELTO"]
    
    Para 3 calificaciones: ["1-NO RESUELTO", "2-REGULAR", "3-PERFECTO"]
    
    Para 4 calificaciones: ["1-NO RESUELTO", "2-REGULAR", "3-BIEN", "4-PERFECTO"]
    
    Para 5 calificaciones: ["1-NO RESUELTO", "2-MAL", "3-BIEN", "4-MUY BIEN", "5-PERFECTO"]
    
    El programa va a dividir equitativamente los puntos maximos de cada ejercicio
    Por ejemplo si son 5 ejercicios cada uno va a valer 20 puntos
    Luego va dividir esos 20 puntos en la cantidad de calificaciones que queramos
    y va a asignar a cada una un puntaje relativo a cuanto del total es (1/N siendo 0)
    """)
    label1.pack(pady=10, padx=10)
    Boton_Legacy = tk.Button(frame2, text="Ejecutar Programa Consola", height=5, width=30, command=MenuConsola )
    Boton_Legacy.pack(pady=10, padx=10)
    notebook.add(frame2, text='INFO')


    Ventana.mainloop()

def Menu_Designar_Rubrica():
    nueva_ventana = tk.Toplevel(Ventana)
    nueva_ventana.title("Definir Rubricas")
    nueva_ventana.geometry("400x250")
    nueva_ventana.resizable(width=False, height=False)
    etiqueta_nueva_ventana = ttk.Label(nueva_ventana, text="Esta es la nueva ventana")
    etiqueta_nueva_ventana.pack(padx=20, pady=20)

    textoejercicios = tk.Label(nueva_ventana, text="Ingrese Cantidad Ejercicios")
    textoejercicios.pack(pady=10, padx=10)
    entrada_ejercicios = tk.Entry(nueva_ventana)
    entrada_ejercicios.pack()
    textodivisiones = tk.Label(nueva_ventana, text="Ingrese Cantidad Divisiones")
    textodivisiones.pack(pady=10, padx=10)
    entrada_divisiones = tk.Entry(nueva_ventana)
    entrada_divisiones.pack()
    Boton_Definir = tk.Button(nueva_ventana, text="Definir", height=2, width=20,)
    Boton_Definir.pack(pady=10, padx=10)

MenuVentana()
