""" Créditos de ayuda: José Puac Auxiliar de OLC1 e Ing Navarro"""

from tkinter import END
import symbolTable as TS
import grammar as g
from expressions import *
from instructions import *
from Exception import Excepcion

errores = []


def procesar_imprimir(instr, ts, console):
    # console.insert(END, f"> {resolver_cadena(instr.cad, ts)}\n")
    print('> ', resolver_cadena(instr.cad, ts))


def procesar_definicion(instr, ts, signal=False):
    # inicializamos con 0 como valor por defecto
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NULL, None, instr.row, instr.col)
    val = ts.agregar(simbolo)
    if isinstance(val, Excepcion):
        # print(val.toString())
        errores.append(val)
        return val
    if signal:
        procesar_asignacion(instr, ts)


def procesar_asignacion(instr, ts):
    val = resolver_expresion_aritmetica(instr.expression, ts)

    if isinstance(instr.expression, ExpresionSimpleComilla):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CHAR, val, instr.row, instr.col)

    elif isinstance(instr.expression, ExpresionDobleComilla):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, val, instr.row, instr.col)

    elif isinstance(instr.expression, ExpresionLogica):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, val, instr.row, instr.col)

    elif isinstance(instr.expression, ExpresionBoolean):
        if val:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, True, instr.row, instr.col)
        else:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, False, instr.row, instr.col)

    elif isinstance(instr.expression, ExpresionLogicaNot):
        if val:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, True, instr.row, instr.col)
        else:
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEAN, False, instr.row, instr.col)

    elif isinstance(val, str):
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, val, instr.row, instr.col)
    elif isinstance(val, Excepcion):
        print(val.toString())
        return val.toString()

    elif isinstance(instr.expression, ExpresionIncrement):
        if instr.expression.operation == OPERACION_ARITMETICA.INCREMENTO:
            val = ts.obtener(instr.id).valor + 1
        else:
            val = ts.obtener(instr.id).valor - 1

        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val, instr.row, instr.col)

    elif isinstance(instr.expression, ExpresionNull):
        return resolver_expresion_null(instr.id, ts)

    else:
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val, instr.row, instr.col)

    ts.actualizar(simbolo, errores)


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
            if case.break_instr is not None:
                if case.break_instr.col:
                    return
    procesar_instrucciones(instr.default.instrucciones, ts_local, console)


def procesar_for(instr, ts, console):
    ts_local = TS.TablaDeSimbolos(ts)
    procesar_definicion_asignacion(instr.exp1, ts_local)
    while resolver_operador_logico(instr.expLogica, ts_local):
        ts_instr = TS.TablaDeSimbolos(ts_local)
        procesar_instrucciones(instr.instrucciones, ts_instr, console)
        resolver_expresion_increment(instr.reAsign, ts_local)
        # resolver_operador_logico(logic, ts_local)


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
        return resolver_expresion_increment(expCad, ts)

    elif isinstance(expCad, ExpresionCadenaNumerico):
        return str(resolver_expresion_aritmetica(expCad.exp, ts))

    elif isinstance(expCad, ExpresionNumero):
        return str(expCad.val)

    elif isinstance(expCad, ExpresionIdentificador):
        if expCad.id.lower() == "true":
            return "true"
        elif expCad.id.lower() == "false":
            return "false"
        try:
            val = ts.obtener(expCad.id.lower()).valor
            return val
        except AttributeError:
            err = Excepcion("Error semantico", "No existe el id", expCad.row, expCad.col)
            errores.append(err)
            return err.toString()

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

    elif isinstance(expCad, Call):
        val = call_func(expCad.name, ts, None, expCad.params)
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
        elif isinstance(exp1, int) and isinstance(exp2, float):
            return exp1 == exp2
        elif isinstance(exp1, float) and isinstance(exp2, int):
            return exp1 == exp2
        return str(exp1) == str(exp2)
    if expLog.operador == OPERACION_LOGICA.DIFERENTE: return exp1 != exp2


def resolver_operador_logico(expLog, ts):
    exp1 = True
    exp2 = True
    if isinstance(expLog, ExpresionBoolean):
        return resolver_operador_bool(expLog)
    elif isinstance(expLog, ExpresionLogica):
        return resolver_expreision_logica(expLog, ts)
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
    elif isinstance(expLog.exp1, ExpresionLogicaNot):
        exp1 = resolver_operador_not(expLog.exp1, ts)
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
    if expLog.val:
        return True
    return False


def resolver_expresion_increment(expLog, ts):
    if expLog.operation == OPERACION_ARITMETICA.INCREMENTO:
        val = ts.obtener(expLog.expression.id).valor + 1
    else:
        val = ts.obtener(expLog.expression.id).valor - 1

    simbolo = TS.Simbolo(expLog.expression.id, TS.TIPO_DATO.NUMERO, val, expLog.row, expLog.col)
    ts.actualizar(simbolo, errores)
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

        if expNum.operador == OPERACION_ARITMETICA.MENOS:
            try:
                res = exp1 - exp2
                return res
            except TypeError:
                err = Excepcion("Error semantico", "No es posible la resta", expNum.row, expNum.col)
                errores.append(err)
                return err.toString()
        if expNum.operador == OPERACION_ARITMETICA.POR:
            try:
                res = exp1 * exp2
                return res
            except TypeError:
                err = Excepcion("Error semantico", "No es posible el producto", expNum.row, expNum.col)
                errores.append(err)
                return err.toString()
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO:
            try:
                res = exp1 / exp2
                return res
            except TypeError:
                err = Excepcion("Error semantico", "No es posible la division", expNum.row, expNum.col)
                errores.append(err)
                return err.toString()
            except ZeroDivisionError:
                err = Excepcion("Error semantico", "Division por 0", expNum.row, expNum.col)
                errores.append(err)
                return err.toString()
        if expNum.operador == OPERACION_ARITMETICA.POTENCIA:
            try:
                res = exp1 ** exp2
                return res
            except TypeError:
                err = Excepcion("Error semantico", "No es posible la potencia", expNum.row, expNum.col)
                errores.append(err)
                return err.toString()
        if expNum.operador == OPERACION_ARITMETICA.MODULO:
            try:
                res = exp1 % exp2
                return res
            except TypeError:
                err = Excepcion("Error semantico", "No es posible el modulo", expNum.row, expNum.col)
                errores.append(err)
                return err.toString()
            except ZeroDivisionError:
                err = Excepcion("Error semantico", "Division por 0", expNum.row, expNum.col)
                errores.append(err)
                return err.toString()

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
        return expNum.val

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

    elif isinstance(expNum, Cast):
        return resolver_casteo(expNum, ts)

    elif isinstance(expNum, ExpresionNull):
        return


def resolver_casteo(expNum, ts):
    val = expNum.value
    if isinstance(expNum.value, ExpresionIdentificador):
        val = ts.obtener(expNum.value.id).valor
    try:
        if expNum.data == 'int':
            return int(val)
        elif expNum.data == 'double':
            return float(val)
        elif expNum.data == 'string':
            return str(val)
        elif expNum.data == 'char':
            if len(str(val)) == 1:
                return str(val)
    except ValueError:
        return Excepcion("Error semántico", "No es posible este casteo", expNum.row, expNum.col)


def resolver_expresion_null(expNum, ts):
    ts.delete_data_type(expNum)


def procesar_func(instr, ts, console):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NULL, instr.instructions, instr.params, instr.row, instr.col)
    ts.agregar(simbolo)


def call_func(name: Function, ts, console, params=[]):
    ts_local = TS.TablaDeSimbolos(ts)
    func = ts.obtener(name)
    if len(func.params[0]) > 0:
        if len(func.params) == len(params):
            i = 0
            for param in func.params:
                if isinstance(params[i], ExpresionBinaria):
                    value = resolver_expresion_aritmetica(params[i], ts)
                elif isinstance(params[i], ExpresionOperacionLogica):
                    value = resolver_operador_logico(params[i], ts)
                elif (param["type"] == 'int' or param["type"] == 'double' and isinstance(params[i], ExpresionNumerica)) \
                        or (param["type"] == 'boolean' and isinstance(params[i], ExpresionBoolean))\
                        or (param["type"] == 'string' and isinstance(params[i], ExpresionCadena)):
                    value = params[i].val
                else:
                    return Excepcion("Semantico", "Tipo de dato diferente", func.row, func.col).toString()
                simbol = TS.Simbolo(param["id"], param["type"], value, 0, 0)
                ts_local.agregar(simbol)
                i += 1
        else:
            return Excepcion("Semantico", "Numero de parametros diferente", func.row, func.col).toString()
    val = procesar_instrucciones(func.valor, ts_local, console)
    if val:
        res = resolver_expresion_aritmetica(val, ts_local)
        simbolo = TS.Simbolo(func.id, TS.TIPO_DATO.NUMERO, res, func.row, func.col)
        ts_local.actualizar(simbolo, None)
        return res


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
        elif isinstance(instr, Function):
            procesar_func(instr, ts, console)
        elif isinstance(instr, Call):
            call_func(instr.name, ts, console, instr.params)
        elif isinstance(instr, Return):
            return instr.exp
        else:
            print('Error: instrucción no válida')


f = open("tests/input.txt", "r")
input = f.read()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global, None)
