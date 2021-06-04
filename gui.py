from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

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
        filetypes=(("Ficheros de texto", "*.txt"),),
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


# Configuración de la raíz
root = Tk()
root.title("JPR Ide")

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")
menubar.add_cascade(menu=filemenu, label="Edición")
menubar.add_cascade(menu=filemenu, label="Herramientas")
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
texto.config(bd=0, highlightbackground="white", highlightcolor="white", highlightthickness=8, width=50, height=20,
             padx=6, pady=4, font=("Consolas", 12))
texto.grid(row=3, column=0, padx=20, pady=20)

# Console
console = Frame(frame)
console.config(bg="gray14", highlightbackground="black", highlightcolor="black", highlightthickness=8,
               width=480, height=480)
console.grid(row=3, column=1)

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a JPR Ide")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# Finalmente bucle de la apliación
root.mainloop()
