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
    # if simbolo.id in ts.simbolos:
    #     print(Excepcion("Semántico", f"Variable {simbolo.id} ya existe", 0, 0).toString())
    # else:
    val = ts.agregar(simbolo)
    if isinstance(val, Exception):
        print(val)
        return val
    if signal:
        procesar_asignacion(instr, ts)


def procesar_asignacion(instr, ts):
    val = resolver_expresion_aritmetica(instr.expression, ts)

    if isinstance(instr.expression, ExpresionSimpleComilla):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CHAR, val)
    elif isinstance(instr.expression, ExpresionDobleComilla):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, val)
    elif isinstance(instr.expression, ExpresionLogica):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, val)
    elif isinstance(instr.expression, ExpresionBoolean):
        if val:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, True)
        else:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, False)
    elif isinstance(instr.expression, ExpresionLogicaNot):
        if val:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, True)
        else:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, False)
    elif isinstance(val, str):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CHAR, val)
    elif isinstance(instr.expression, ExpresionIncrement):
        if instr.expression.operation == OPERACION_ARITMETICA.INCREMENTO:
            val = ts.obtener(instr.id).valor + 1
        else:
            val = ts.obtener(instr.id).valor - 1

        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    else:
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)

    ts.actualizar(simbolo)


def procesar_definicion_asignacion(instr, ts):
    procesar_definicion(instr, ts, True)


def procesar_while(instr, ts, console):
    while resolver_operador_logico(instr.expLogica, ts):
        ts_local = TS.TablaDeSimbolos(ts)
        procesar_instrucciones(instr.instrucciones, ts_local, console)


def procesar_if(instr, ts, console):
    val = True
    if isinstance(instr.expLogica, ExpresionOperacionLogica):
        val = resolver_operador_logico(instr.expLogica, ts)
    elif isinstance(instr.expLogica, ExpresionLogica):
        val = resolver_expreision_logica(instr.expLogica, ts)
    elif isinstance(instr.expLogica, ExpresionLogicaNot):
        val = resolver_operador_not(instr.expLogica, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts)
        procesar_instrucciones(instr.instrucciones, ts_local, console)


def procesar_if_else(instr, ts, console):
    val = True
    if isinstance(instr.expLogica, ExpresionOperacionLogica):
        val = resolver_operador_logico(instr.expLogica, ts)
    elif isinstance(instr.expLogica, ExpresionLogica):
        val = resolver_expreision_logica(instr.expLogica, ts)
    elif isinstance(instr.expLogica, ExpresionLogicaNot):
        val = resolver_operador_not(instr.expLogica, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts)
        procesar_instrucciones(instr.instrIfVerdadero, ts_local, console)
    else:
        ts_local = TS.TablaDeSimbolos(ts)
        procesar_instrucciones(instr.instrIfFalso, ts_local, console)


def procesar_else_if(instr, ts, console):
    val = True
    if isinstance(instr.expLogica, ExpresionOperacionLogica):
        val = resolver_operador_logico(instr.expLogica, ts)
    elif isinstance(instr.expLogica, ExpresionLogica):
        val = resolver_expreision_logica(instr.expLogica, ts)
    elif isinstance(instr.expLogica, ExpresionLogicaNot):
        val = resolver_operador_not(instr.expLogica, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts)
        procesar_instrucciones(instr.instrIfVerdadero, ts_local, console)
    else:
        # for instruction in instr.instrElse.instrIfVerdadero:
        ts_local = TS.TablaDeSimbolos(ts)
        procesar_instrucciones(instr.instrElse.instrIfVerdadero, ts_local, console)


def procesar_switch(instr, ts, console):
    ts_local = TS.TablaDeSimbolos(ts)
    if isinstance(instr.expLogica, ExpresionIdentificador):
        val = ts_local.obtener(instr.expLogica.id).valor
    else:
        val = instr.expLogica.val
    for case in instr.cases:
        if val == case.expression.val:
            procesar_instrucciones(case.instrucciones, ts_local, console)
            if case.break_instr.col:
                return
    procesar_instrucciones(instr.default.instrucciones, ts_local, console)


def procesar_for(instr, ts, console):
    val = True
    ts_local = TS.TablaDeSimbolos(ts)
    if isinstance(instr.exp1, Definicion_Asignacion):
        procesar_definicion_asignacion(instr.exp1, ts_local)
    elif isinstance(instr.exp1, Asignacion):
        procesar_asignacion(instr.exp1, ts_local)

    if isinstance(instr.expLogica, ExpresionLogica):
        val = resolver_expreision_logica(instr.expLogica, ts_local)
    elif isinstance(instr.expLogica, ExpresionOperacionLogica):
        val = resolver_operador_logico(instr.expLogica, ts_local)

    while val:
        # ts = TS.TablaDeSimbolos(ts)
        procesar_instrucciones(instr.instrucciones, ts_local, console)
        counter = resolver_expresion_increment(instr.reAsign, ts_local)

        num = ExpresionNumero(counter)
        logic = ExpresionLogica(num, instr.expLogica.exp2, instr.expLogica.operador)

        if isinstance(instr.expLogica, ExpresionLogica):
            val = resolver_expreision_logica(logic, ts_local)
        elif isinstance(instr.expLogica, ExpresionOperacionLogica):
            val = resolver_operador_logico(logic, ts_local)


def procesar_func_main(instr, ts, console):
    ts_local = TS.TablaDeSimbolos(ts)
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
        return ts.obtener(expCad.id.lower()).valor
    elif isinstance(expCad, ExpresionBoolean):
        return True if expCad.val == 'true' else False
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
    elif isinstance(expCad, ExpresionLogicaNot):
        val = resolver_operador_not(expCad, ts)
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
    exp1 = True
    exp2 = True
    if isinstance(expLog, ExpresionBoolean):
        return resolver_operador_bool(expLog)
    elif isinstance(expLog.exp1, ExpresionBoolean):
        exp1 = resolver_operador_bool(expLog.exp1)
    elif isinstance(expLog.exp1, ExpresionOperacionLogica):
        exp1 = resolver_operador_logico(expLog.exp1, ts)
    elif isinstance(expLog.exp1, ExpresionLogica):
        exp1 = resolver_expreision_logica(expLog.exp1, ts)
    elif isinstance(expLog.exp1, ExpresionLogicaNot):
        exp1 = resolver_operador_not(expLog.exp1.exp1, ts)

    if isinstance(expLog.exp2, ExpresionBoolean):
        exp2 = resolver_operador_bool(expLog.exp2)
    elif isinstance(expLog.exp2, ExpresionOperacionLogica):
        exp2 = resolver_operador_logico(expLog.exp2, ts)
    elif isinstance(expLog.exp2, ExpresionLogica):
        exp2 = resolver_expreision_logica(expLog.exp2, ts)
    elif isinstance(expLog.exp2, ExpresionLogicaNot):
        exp2 = resolver_operador_not(expLog.exp2, ts)

    if expLog.operador == OPERADOR_LOGICO.AND:
        if exp1 and exp2:
            return True
    if expLog.operador == OPERADOR_LOGICO.OR:
        if exp1 or exp2:
            return True
    return False


def resolver_operador_not(expLog, ts):
    if isinstance(expLog, ExpresionLogica):
        exp1 = resolver_expreision_logica(expLog, ts)
    elif isinstance(expLog.exp1, ExpresionLogica):
        exp1 = resolver_expreision_logica(expLog.exp1, ts)
    elif isinstance(expLog.exp1, ExpresionIdentificador):
        exp1 = ts.obtener(expLog.exp1.id.lower()).valor
    else:
        exp1 = resolver_operador_logico(expLog.exp1, ts)
    # else:
    #     exp1 = ts.obtener(expLog.exp1.id).valor
    if not exp1:
        return True
    return False


def resolver_operador_bool(expLog):
    if expLog.val == 'true':
        return True
    return False


def resolver_expresion_increment(expLog, ts):
    if expLog.operation == OPERACION_ARITMETICA.INCREMENTO:
        val = ts.obtener(expLog.expression.id).valor + 1
    else:
        val = ts.obtener(expLog.expression.id).valor - 1

    simbolo = TS.Simbolo(expLog.expression.id, TS.TIPO_DATO.NUMERO, val)
    ts.actualizar(simbolo)
    return val


def resolver_expresion_aritmetica(expNum, ts):
    if isinstance(expNum, ExpresionBinaria):
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS:
            if isinstance(exp1, int) and isinstance(exp2, str):
                if isinstance(exp1, bool):
                    if exp1:
                        return f"true{exp2}"
                    else:
                        return f"false{exp2}"
                return str(exp1) + exp2
            elif isinstance(exp1, float) and isinstance(exp2, str):
                return str(exp1) + exp2
            elif isinstance(exp1, str) and isinstance(exp2, int):
                if isinstance(exp2, bool):
                    if exp2:
                        return f"{exp1}true"
                    else:
                        return f"{exp1}false"
                return exp1 + str(exp2)
            elif isinstance(exp1, str) and isinstance(exp2, float):
                return exp1 + str(exp2)
            elif isinstance(exp1, str) and isinstance(exp2, bool):
                if exp2:
                    return f"true{exp1}"
                else:
                    return f"false{exp1}"
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
        return ts.obtener(expNum.id.lower()).valor

    elif isinstance(expNum, ExpresionBoolean):
        if expNum.val.lower() == "true":
            return True
        elif expNum.val.lower() == "false":
            return False

    elif isinstance(expNum, ExpresionDobleComilla):
        return expNum.val

    elif isinstance(expNum, ExpresionSimpleComilla):
        return expNum.val

    elif isinstance(expNum, ExpresionLogica):
        return resolver_expreision_logica(expNum, ts)

    elif isinstance(expNum, ExpresionLogicaNot):
        return resolver_operador_not(expNum, ts)

    elif isinstance(expNum, ExpresionOperacionLogica):
        return resolver_operador_logico(expNum, ts)

    elif isinstance(expNum, ExpresionIncrement):
        return resolver_expresion_increment(expNum, ts)


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
        elif isinstance(instr, While):
            procesar_while(instr, ts, console)
        elif isinstance(instr, If):
            procesar_if(instr, ts, console)
        elif isinstance(instr, IfElse):
            procesar_if_else(instr, ts, console)
        elif isinstance(instr, ElseIf):
            procesar_else_if(instr, ts, console)
        elif isinstance(instr, Switch):
            procesar_switch(instr, ts, console)
        elif isinstance(instr, Funcion_Main):
            procesar_func_main(instr.instrucciones, ts, console)
        elif isinstance(instr, ExpresionIncrement):
            resolver_expresion_increment(instr, ts)
        elif isinstance(instr, For):
            procesar_for(instr, ts, console)
        else:
            print('Error: instrucción no válida')


f = open("input.txt", "r")
input = f.read()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global, None)
