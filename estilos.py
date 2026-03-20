import tkinter as tk
colores = {"fondo": "#688D9D",
           "neuronas_borde": "#F2A750",
           "neuronas_centro": "#F2CA50",
           "axon": "#50C2F2",
           "bordes":"#5F736E",
           "titulos": "#50F2CB"}
def interfaz():
    app = tk.Tk()
    app.configure(background=colores["fondo"])
    return app
def cuadro(raiz):
    F = tk.Frame(raiz)
    F.configure(background=colores["fondo"],highlightthickness= 3,highlightbackground = colores["bordes"], highlightcolor = colores["bordes"],borderwidth=3)
    return F