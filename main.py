from tkinter import END
import symbolTable as TS
import grammar as g
from expressions import *
from instructions import *
from Exception import Excepcion


def procesar_imprimir(instr, ts, console):
    # console.insert(END, f"> {resolver_cadena(instr.cad, ts)}\n")
    print('> ', resolver_cadena(instr.cad, ts))


def procesar_definicion(instr, ts, signal=False):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)  # inicializamos con 0 como valor por defecto
    if simbolo.id in ts.simbolos:
        print(Excepcion("Semántico", f"Variable {simbolo.id} ya existe", 0, 0).toString())
    else:
        ts.agregar(simbolo)
        if signal:
            procesar_asignacion(instr, ts)


def procesar_asignacion(instr, ts):
    val = resolver_expresion_aritmetica(instr.expression, ts)
    simbolo = None

    if isinstance(instr.expression, ExpresionSimpleComilla):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CHAR, val)
    elif isinstance(instr.expression, ExpresionDobleComilla):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, val)
    elif isinstance(val, str):
        if val.lower() == "true":
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, True)
        elif val.lower() == "false":
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, False)
    else:
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)

    ts.actualizar(simbolo)


def procesar_definicion_asignacion(instr, ts):
    procesar_definicion(instr, ts, True)


def procesar_mientras(instr, ts, console):
    while resolver_expreision_logica(instr.expLogica, ts):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local, console)


def procesar_if(instr, ts, console):
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local, console)


def procesar_if_else(instr, ts, console):
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfVerdadero, ts_local, console)
    else:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfFalso, ts_local, console)


def procesar_func_main(instr, ts, console):
    ts_local = TS.TablaDeSimbolos(ts.simbolos)
    procesar_instrucciones(instr, ts_local, console)


def resolver_cadena(expCad, ts):
    if isinstance(expCad, ExpresionConcatenar):
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return str(exp1) + str(exp2)
    elif isinstance(expCad, ExpresionDobleComilla):
        return expCad.val
    elif isinstance(expCad, ExpresionSimpleComilla):
        return expCad.val
    elif isinstance(expCad, ExpresionIncrement):
        pass
    elif isinstance(expCad, ExpresionCadenaNumerico):
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    elif isinstance(expCad, ExpresionNumero):
        return str(expCad.val)
    elif isinstance(expCad, ExpresionIdentificador):
        if expCad.id.lower() == "true":
            return "true"
        elif expCad.id.lower() == "false":
            return "false"
        return ts.obtener(expCad.id).valor
    elif isinstance(expCad, ExpresionBinaria):
        return resolver_expresion_aritmetica(expCad, ts)
    elif isinstance(expCad, ExpresionLogica):
        val = resolver_expreision_logica(expCad, ts)
        if val:
            return True
        return False
    elif isinstance(expCad, ExpresionOperacionLogica):
        val = resolver_operador_logico(expCad, ts)
        return val
    else:
        print('Error: Expresión cadena no válida')


def resolver_expreision_logica(expLog, ts):
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
    if expLog.operador == OPERACION_LOGICA.MAYOR_QUE: return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_QUE: return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.MENORIGUAL_QUE: return exp1 <= exp2
    if expLog.operador == OPERACION_LOGICA.MAYORIGUAL_QUE: return exp1 >= exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL:
        if isinstance(exp1, bool) and isinstance(exp2, str):
            if exp1:
                temp = "true"
                return temp == exp2
            else:
                temp = "false"
                return temp == exp2
        elif isinstance(exp2, bool) and isinstance(exp1, str):
            if exp2:
                temp = "true"
                return temp == exp1
            else:
                temp = "false"
                return temp == exp1
        elif isinstance(exp1, bool) and isinstance(exp2, bool):
            return exp1 == exp2
        return str(exp1) == str(exp2)
    if expLog.operador == OPERACION_LOGICA.DIFERENTE: return exp1 != exp2


def resolver_operador_logico(expLog, ts):
    exp1 = resolver_expreision_logica(expLog.exp1, ts)
    if expLog.operador == OPERADOR_LOGICO.NOT:
        if not exp1:
            return True
    else:
        exp2 = resolver_expreision_logica(expLog.exp2, ts)
        if expLog.operador == OPERADOR_LOGICO.AND:
            if exp1 and exp2:
                return True
        if expLog.operador == OPERADOR_LOGICO.OR:
            if exp1 or exp2:
                return True
    return False


def resolver_expresion_aritmetica(expNum, ts):
    if isinstance(expNum, ExpresionBinaria):
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS:
            if isinstance(exp1, int) and isinstance(exp2, str):
                if isinstance(exp1, bool):
                    return f"1{exp2}"
                return str(exp1) + exp2
            elif isinstance(exp1, float) and isinstance(exp2, str):
                return str(exp1) + exp2
            elif isinstance(exp1, str) and isinstance(exp2, int):
                if isinstance(exp2, bool):
                    return f"{exp1}1"
                return exp1 + str(exp2)
            elif isinstance(exp1, str) and isinstance(exp2, float):
                return exp1 + str(exp2)
            elif isinstance(exp1, str) and isinstance(exp2, bool):
                return f"1{exp1}"

            return exp1 + exp2

        if expNum.operador == OPERACION_ARITMETICA.MENOS: return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR: return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO: return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.POTENCIA: return exp1 ** exp2
        if expNum.operador == OPERACION_ARITMETICA.MODULO: return exp1 % exp2

    elif isinstance(expNum, ExpresionNegativo):
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1

    elif isinstance(expNum, ExpresionNumero):
        return expNum.val

    elif isinstance(expNum, ExpresionCadenaNumerico):
        return expNum.exp

    elif isinstance(expNum, ExpresionIdentificador):
        if expNum.id.lower() == "true":
            return True
        elif expNum.id.lower() == "false":
            return False
        return ts.obtener(expNum.id).valor

    elif isinstance(expNum, ExpresionDobleComilla):
        return expNum.val

    elif isinstance(expNum, ExpresionSimpleComilla):
        return expNum.val


def procesar_instrucciones(instrucciones, ts, console):
    # lista de instrucciones recolectadas
    for instr in instrucciones:
        if isinstance(instr, Imprimir):
            procesar_imprimir(instr, ts, console)
        elif isinstance(instr, Definicion):
            procesar_definicion(instr, ts)
        elif isinstance(instr, Asignacion):
            procesar_asignacion(instr, ts)
        elif isinstance(instr, Definicion_Asignacion):
            procesar_definicion_asignacion(instr, ts)
        elif isinstance(instr, Mientras):
            procesar_mientras(instr, ts, console)
        elif isinstance(instr, If):
            procesar_if(instr, ts, console)
        elif isinstance(instr, IfElse):
            procesar_if_else(instr, ts, console)
        elif isinstance(instr, Funcion_Main):
            procesar_func_main(instr.instrucciones, ts, console)
        else:
            print('Error: instrucción no válida')


f = open("input.txt", "r")
input = f.read()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global, None)
