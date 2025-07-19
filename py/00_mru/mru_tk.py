# Ejercicio 1.

# Se desea calcualr la distancia recorrida (m) por un móvil que tiene velocidad constante (m/s) durante un tiempo t (s). Considerar que es un MRU (Movimiento Rectilíneo Uniforme).

import tkinter as tk

def function_click():
    velocidad = float(entry_velocidad.get))
    tiempo = float(entry_tiempo.get))
    distancia = velocidad*tiempo
    labelrespult.configure(text=f"resultado:{distancia}")

    root = tk.Tk()
    root = title("paython-tkinter")
    root = resizable(0, 0)
    root = minsize(1000,700)
    # elements
    #label
    labelrespult = tk.Label(root, text="RESULTADO:")
    final = tk.Label(root, text="DISTANCIAS RECORRIDA:")
    primero =tk.Label(root, text="VELOCIDAD:")
    segundo = tk.Label(root,text="TIEMPO:")

    #agregar una caja de texto
    partidos_ganados = tk.StringVar()

    #textbox
    text_velocidad = tk.StringVar()
    text_tiempo = tk.StringVar()

    #entry 
    entry_velocidad = tk.entry(root,width=20,textvaribale=text_velocidad)
    text_tiempo = tk.entry(root,width=20,textvaribale=text_tiempo)

    # boton 
    button=tk.Button(root.text="calcular", command=function_click)
    
    #position
    final.gird(column=6, row=2)
    primero.grid(column=1, row=2)
    segundo.grid(column=3, row=2)
    entry_velocidad.grid(column=2, row=2)
    entry_tiempo.grid(column=4, row=2)
    labelresult.grid(column=0, row=0)
    button.grid(column=0, row=1)


    root.mainloop()
    