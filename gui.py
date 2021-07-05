import os
import subprocess
import time
from tkinter import *
from tkinter import filedialog as FileDialog, scrolledtext
from io import open
from main import *
import grammar as g

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())

ruta = ""  # La utilizaremos para almacenar la ruta del fichero
symbolTables = []


def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")


def abrir():
    # main.errores = []
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
    global ast

    console.delete("1.0", END)
    instrucciones = g.parse(texto.get("1.0", END))
    ts_global = TS.TablaDeSimbolos()
    ast = Tree(instrucciones)
    ast.setTSglobal(ts_global)

    # PRIMERA PASADA
    for instr in ast.getInstrs():
        if isinstance(instr, Function):
            procesar_func(instr, ts_global, console)
        elif isinstance(instr, Definicion):
            procesar_definicion(instr, ts_global, console)
        elif isinstance(instr, Asignacion):
            procesar_asignacion(instr, ts_global, console, symbolTables)
        elif isinstance(instr, Definicion_Asignacion):
            procesar_definicion_asignacion(instr, ts_global, console, symbolTables)

    symbolTables.append(ts_global)

    # SEGUNDA PASADA
    for instr in ast.getInstrs():
        if isinstance(instr, Funcion_Main):
            procesar_func_main(instr.instrucciones, ts_global, console, symbolTables)
    t1 = time.time()

    if len(g.errores) > 0:
        for e in g.errores:
            console.insert(END, f"> {e.toString()}\n")

    console.insert(END, f"\n\n> Ejecución terminada en: {round(t1 - t0, 6)} segundos")


def generateReport():
    print(len(errores))
    f = open('reporte.html', 'w')

    f.write(f"<!DOCTYPE html>\n"
            f"<html>\n"
            f"<head>\n"
            f"<meta charset=\"utf-8\">\n"
            f"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            f"<title>OLC1</title>\n"
            f"<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css\">\n"
            f"</head>\n"
            f"<body>\n"
            f"<section class=\"section\">\n"
            f"<div class=\"container\">\n"
            f"<h1 class=\"title\">\n"
            f"Generador de Errores\n"
            f"</h1>\n"

            f"<div class=\"container\">\n"
            f"<table class=\"table is-bordered is-striped is-narrow is-hoverable is-fullwidth\">\n"
            f"<thead>\n"
            f"<tr>\n"
            f"<th><abbr title=\"Position\">Pos</abbr></th>\n"
            f"<th abbr>Tipo de Error</th>\n"
            f"<th><abbr title=\"Played\">Descripción</abbr></th>"
            f"<th><abbr title=\"Won\">Línea</abbr></th>"
            f"<th><abbr title=\"Drawn\">Columna</abbr></th>"
            f"</tr>\n"
            f"</thead>\n"
            f"<tbody>\n")
    i = 1
    for e in errores:
        f.write(
            "f<tr>\n"
            f"<th>{i}</th>\n"
            f"<td>{e.type}</td>\n"
            f"<td>{e.desc}</td>\n"
            f"<td>{e.row}</td>\n"
            f"<td>{e.col}</td>\n"
            f"</tr>\n"
        )
        i += 1

    j = 1
    for e in g.errores:
        f.write(
            "f<tr>\n"
            f"<th>{j}</th>\n"
            f"<td>{e.type}</td>\n"
            f"<td>{e.desc}</td>\n"
            f"<td>{e.row}</td>\n"
            f"<td>{e.col}</td>\n"
            f"</tr>\n"
        )
        j += 1

    f.write("f</tbody>\n"
            "f</table>\n"
            "</div>\n"
            "</div>\n"
            "</section>\n"
            "</body>\n"
            "</html>")

    f.close()

    nombreArchivo = 'reporte.html'
    subprocess.call(['xdg-open', nombreArchivo])


def generateReportST():
    print(len(errores))
    f = open('reporteTS.html', 'w')

    f.write(f"<!DOCTYPE html>\n"
            f"<html>\n"
            f"<head>\n"
            f"<meta charset=\"utf-8\">\n"
            f"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            f"<title>OLC1</title>\n"
            f"<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css\">\n"
            f"</head>\n"
            f"<body>\n"
            f"<section class=\"section\">\n"
            f"<div class=\"container\">\n"
            f"<h1 class=\"title\">\n"
            f"Tabla de Símbolos\n"
            f"</h1>\n"

            f"<div class=\"container\">\n"
            f"<table class=\"table is-bordered is-striped is-narrow is-hoverable is-fullwidth\">\n"
            f"<thead>\n"
            f"<tr>\n"
            f"<th><abbr>Identificador</abbr></th>\n"
            f"<th abbr>Tipo</th>\n"
            f"<th><abbr>Tipo de Dato</abbr></th>"
            f"<th><abbr>Entorno</abbr></th>"
            f"<th><abbr>Valor</abbr></th>"
            f"<th><abbr>Línea</abbr></th>"
            f"<th><abbr>Columna</abbr></th>"
            f"</tr>\n"
            f"</thead>\n"
            f"<tbody>\n")
    i = 1
    ids = []
    for st in symbolTables:
        for symbol in st.simbolos:
            # print(symbol)
            sym = st.simbolos[symbol]
            if sym.id not in ids:
                ids.append(sym.id)
                if sym.tipo == Type.NULL:
                    f.write(
                        "f<tr>\n"
                        f"<th>{sym.id}</th>\n"
                        f"<td>Funcion</td>\n"
                        f"<td>{sym.tipo}</td>\n"
                        f"<td>----</td>\n"
                        f"<td>----</td>\n"
                        f"<td>{sym.col}</td>\n"
                        f"<td>{sym.row}</td>\n"
                        f"</tr>\n"
                    )
                else:
                    f.write(
                        "f<tr>\n"
                        f"<th>{sym.id}</th>\n"
                        f"<td>Variable</td>\n"
                        f"<td>{sym.tipo}</td>\n"
                        f"<td>Main</td>\n"
                        f"<td>{sym.valor}</td>\n"
                        f"<td>{sym.col}</td>\n"
                        f"<td>{sym.row}</td>\n"
                        f"</tr>\n"
                    )
                i += 1

    f.write("f</tbody>\n"
            "f</table>\n"
            "</div>\n"
            "</div>\n"
            "</section>\n"
            "</body>\n"
            "</html>")

    f.close()

    nombreArchivo = 'reporteTS.html'
    subprocess.call(['xdg-open', nombreArchivo])


def generateAst():
    init = Node("ROOT")
    instrs = Node("INSTRUCTIONS")

    for instr in ast.getInstrs():
        instrs.agregarHijoNodo(instr.getNode())
    init.agregarHijoNodo(instrs)
    graph = ast.getDot(init)
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'ast.dot')
    file = open(path, 'w+')
    file.write(graph)
    file.close()
    os.system('dot -T pdf -o ast.pdf ast.dot')
    subprocess.call(['xdg-open', "ast.pdf"])


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Configuración de la raíz
root = Tk()
root.title("JPR Ide")

# Menú superior
menubar = Menu(root)
menuTools = Menu(root)
menuReports = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Resetear", command=restart_program)

fMenuTools = Menu(menuTools, tearoff=0)
fMenuTools.add_command(label="Ejecutar", command=executeProgram)

fMenuReports = Menu(menuReports, tearoff=0)
fMenuReports.add_command(label="Reporte de Errores", command=generateReport)
fMenuReports.add_command(label="Reporte de Árbol AST", command=generateAst)
fMenuReports.add_command(label="Reporte de Tabla de Símbolos", command=generateReportST)

menubar.add_cascade(menu=filemenu, label="Archivo")
menubar.add_cascade(menu=fMenuTools, label="Herramientas")
menubar.add_cascade(menu=fMenuReports, label="Reportes")

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


labelIn = Label(frame, text="input:")
labelIn.config(bg="slate gray")
labelIn.grid(row=2, column=0)

labelOut = Label(frame, text="output:")
labelOut.config(bg="slate gray")
labelOut.grid(row=2, column=1)

# Editor
texto = scrolledtext.ScrolledText(frame)
texto.config(bd=0, highlightbackground="white", highlightcolor="white", highlightthickness=8,
             width=60, height=20,
             padx=3, pady=4, font=("Consolas", 12))
texto.grid(row=3, column=0, padx=5, pady=20)

# Console
console = scrolledtext.ScrolledText(frame)
console.config(bd=0, bg="gray14", highlightbackground="black", highlightcolor="black",
               highlightthickness=8, width=60, height=20,
               padx=3, pady=4, font=("Consolas", 12))
console.grid(row=3, column=1)


# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a JPR Ide")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# Finalmente bucle de la apliación
root.mainloop()
