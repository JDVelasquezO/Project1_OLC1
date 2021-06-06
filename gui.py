import time
from tkinter import *
from tkinter import filedialog as FileDialog, scrolledtext
from io import open
from main import *
import grammar as g

ruta = ""  # La utilizaremos para almacenar la ruta del fichero


def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Ficheros de texto", "*"),),
        title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")


def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero",
                                       mode="w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


def executeProgram():
    t0 = time.time()

    console.delete("1.0", END)
    instrucciones = g.parse(texto.get("1.0", END))
    ts_global = TS.TablaDeSimbolos()

    procesar_instrucciones(instrucciones, ts_global, console)
    t1 = time.time()
    console.insert(END, f"\n\n> Ejecución terminada en: {round(t1 - t0, 6)} segundos")


# Configuración de la raíz
root = Tk()
root.title("JPR Ide")

# Menú superior
menubar = Menu(root)
menuTools = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

fMenuTools = Menu(menuTools, tearoff=0)
fMenuTools.add_command(label="Ejecutar", command=executeProgram)
fMenuTools.add_command(label="Depurar", command=executeProgram)

menubar.add_cascade(menu=filemenu, label="Archivo")
menubar.add_cascade(menu=filemenu, label="Edición")
menubar.add_cascade(menu=fMenuTools, label="Herramientas")
menubar.add_cascade(menu=filemenu, label="Analizar")
menubar.add_cascade(menu=filemenu, label="Reportes")
menubar.add_cascade(menu=filemenu, label="Ayuda")

# Frame general
frame = Frame(root, width=240, height=120)
frame.pack(fill='both', expand=1)
frame.config(bd=25, bg="slate gray")

label = Label(frame, text="JPR Ide", font=("Arial", 25))
label.config(bg="slate gray")
label.grid(row=0, column=0)

labelCounter = Label(frame, text="0")
labelCounter.config(bg="slate gray")
labelCounter.grid(row=0, column=1)

labelLine = Label(frame, text="[3, 1]")
labelLine.config(bg="slate gray")
labelLine.grid(row=1, column=0)


def actionNext():
    print("Hola mundo!")


btnNext = Button(frame, text="Siguiente", command=actionNext)
btnNext.grid(row=1, column=1)

labelIn = Label(frame, text="input:")
labelIn.config(bg="slate gray")
labelIn.grid(row=2, column=0)

labelOut = Label(frame, text="output:")
labelOut.config(bg="slate gray")
labelOut.grid(row=2, column=1)

# Editor
texto = Text(frame)
texto.config(bd=0, highlightbackground="white", highlightcolor="white", highlightthickness=8, width=50, height=10,
             padx=6, pady=4, font=("Consolas", 12))
texto.grid(row=3, column=0, padx=20, pady=20)

# Console
console = Text(frame)
console.config(bd=0, bg="gray14", highlightbackground="black", highlightcolor="black",
               highlightthickness=8, width=50, height=10,
               padx=6, pady=4, font=("Consolas", 12))
console.grid(row=3, column=1)

# Frame for tables
tables1 = Frame(frame, width=240, height=120)
tables1.config(bd=25, bg="slate gray")
tables1.grid(row=4, column=0)

tables2 = Frame(frame, width=240, height=120)
tables2.config(bd=25, bg="slate gray")
tables2.grid(row=4, column=1)

# take the data of symbols
lst = [('#', 'Id', 'Tipo', 'Dim', 'Val', 'Amb', 'Ref'),
       (1, '$t1', 'INT', 1, 0, 'gl', 0),
       (2, '$t2', 'STR', 1, 0, 'gl', 0),
       (3, '$t3', 'CHAR', 1, 0, 'lc', 0),
       (4, '$t4', 'INT', 1, 0, 'gl', 0),
       (5, '$t5', 'STR', 1, 0, 'lc', 0),
       ]
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# take the data of errors
lst2 = [('#', 'Tipo', 'Desc', 'Linea', 'Col'),
        (1, '$t1', 'INT', 1, 0),
        (2, '$t2', 'STR', 1, 0),
        (3, '$t3', 'CHAR', 1, 0),
        (4, '$t4', 'INT', 1, 0),
        (5, '$t5', 'STR', 1, 0)
        ]
# find total number of rows and
# columns in list
total_rows2 = len(lst2)
total_columns2 = len(lst2[0])


class TableSymbols:
    def __init__(self, root):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=5, fg='white',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


class TableErrors:
    def __init__(self, root):
        # code for creating table
        for i in range(total_rows2):
            for j in range(total_columns2):
                self.e = Entry(root, width=5, fg='white',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst2[i][j])


tableSymbols = TableSymbols(tables1)
tableErrors = TableErrors(tables2)

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a JPR Ide")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# Finalmente bucle de la apliación
root.mainloop()
