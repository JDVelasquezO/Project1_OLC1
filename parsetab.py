
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONCATleftMASMENOSleftPORDIVIDIDOMODleftELEVADOrightUMENOSCADENA CHAR CONCAT DECIMAL DIVIDIDO ELEVADO ELSE ENTERO FALSE ID IF IGUAL IGUALQUE LLAVDER LLAVIZQ MAIN MAS MAYQUE MENOS MENQUE MIENTRAS MOD NIGUALQUE PARDER PARIZQ POR PRINT PTCOMA TRUE VARinit       : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion\n                         | emptyinstruccion      : func_main\n                        | imprimir_instr\n                        | definicion_instr\n                        | asignacion_instr\n                        | def_asig_instr\n                        | mientras_instr\n                        | if_instr\n                        | if_else_instrfunc_main  : MAIN PARIZQ PARDER LLAVIZQ instrucciones LLAVDERimprimir_instr     : PRINT PARIZQ print_expresion_general PARDER def_instr_primaprint_expresion_general  :  expresion_numerica\n                                | expresion_cadena\n                                | expresion_id\n                                | expresion_boolean\n                                | expresion_char\n                                | expresion_logicaexpresion_id   : IDexpresion_boolean  : TRUE\n                          | FALSEdefinicion_instr   : VAR ID def_instr_primadef_instr_prima   : PTCOMA\n                        | emptyempty :asignacion_instr   : ID IGUAL asign_expresion_general def_instr_primaasign_expresion_general  :  expresion_numerica\n                            | expresion_cadena\n                            | expresion_id\n                            | expresion_boolean\n                            | expresion_chardef_asig_instr     : VAR ID IGUAL asign_def_expresion_general def_instr_primaasign_def_expresion_general  :  expresion_numerica\n                                    | expresion_cadena\n                                    | expresion_id\n                                    | expresion_boolean\n                                    | expresion_charmientras_instr     : MIENTRAS PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDERif_instr           : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDERif_else_instr      : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDERexpresion_numerica : expresion_numerica MAS expresion_numerica\n                        | expresion_numerica MENOS expresion_numerica\n                        | expresion_numerica POR expresion_numerica\n                        | expresion_numerica DIVIDIDO expresion_numerica\n                        | expresion_numerica ELEVADO expresion_numerica\n                        | expresion_numerica MOD expresion_numerica\n                        | expresion_numerica MAS expresion_char\n                        | expresion_cadena MAS expresion_cadena\n                        | expresion_cadena MAS expresion_numerica\n                        | expresion_cadena MAS expresion_char\n                        | expresion_numerica MAS expresion_cadena\n                        | expresion_char MAS expresion_char\n                        | expresion_char MAS expresion_cadena\n                        | expresion_char MAS expresion_numericaexpresion_numerica : MENOS expresion_numerica %prec UMENOSexpresion_numerica : PARIZQ expresion_numerica PARDERexpresion_numerica : ENTERO\n                        | DECIMALexpresion_numerica   : IDexpresion_char   : CHARexpresion_cadena     : CADENAexpresion_cadena     : expresion_numericaexpresion_logica : expresion_numerica MAYQUE expresion_numerica\n                        | expresion_numerica MENQUE expresion_numerica\n                        | asign_def_expresion_general IGUALQUE asign_def_expresion_general\n                        | expresion_numerica NIGUALQUE expresion_numerica'
    
_lr_action_items = {'MAIN':([0,2,3,4,5,6,7,8,9,10,11,12,19,22,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,58,59,61,65,66,78,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,111,112,113,114,115,117,118,119,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-27,-59,-60,-21,-63,-22,-23,-62,-24,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,13,-61,-27,-57,-27,-35,-36,-39,-28,13,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,13,13,-13,13,13,-40,-41,13,13,-42,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,19,22,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,58,59,61,65,66,78,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,111,112,113,114,115,117,118,119,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-27,-59,-60,-21,-63,-22,-23,-62,-24,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,14,-61,-27,-57,-27,-35,-36,-39,-28,14,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,14,14,-13,14,14,-40,-41,14,14,-42,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,19,22,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,58,59,61,65,66,78,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,111,112,113,114,115,117,118,119,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-27,-59,-60,-21,-63,-22,-23,-62,-24,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,15,-61,-27,-57,-27,-35,-36,-39,-28,15,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,15,15,-13,15,15,-40,-41,15,15,-42,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,15,19,21,22,23,24,25,27,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,58,59,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,111,112,113,114,115,117,118,119,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,22,-2,38,-27,38,38,38,65,65,-59,-60,-21,-63,-22,-23,-62,-24,38,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,16,-61,-27,65,65,65,65,65,65,65,65,65,65,65,-57,38,-27,-35,-36,-39,-28,16,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,16,16,-13,16,16,-40,-41,16,16,-42,]),'MIENTRAS':([0,2,3,4,5,6,7,8,9,10,11,12,19,22,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,58,59,61,65,66,78,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,111,112,113,114,115,117,118,119,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-27,-59,-60,-21,-63,-22,-23,-62,-24,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,17,-61,-27,-57,-27,-35,-36,-39,-28,17,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,17,17,-13,17,17,-40,-41,17,17,-42,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,19,22,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,58,59,61,65,66,78,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,111,112,113,114,115,117,118,119,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-27,-59,-60,-21,-63,-22,-23,-62,-24,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,18,-61,-27,-57,-27,-35,-36,-39,-28,18,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,18,18,-13,18,18,-40,-41,18,18,-42,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,22,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,58,59,65,66,78,80,81,82,83,84,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,111,114,115,119,],[-27,0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-27,-59,-60,-21,-63,-22,-23,-62,-24,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,-61,-27,-57,-27,-35,-36,-39,-28,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,-13,-40,-41,-42,]),'LLAVDER':([3,4,5,6,7,8,9,10,11,12,19,22,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,58,59,61,65,66,78,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,111,112,113,114,115,117,118,119,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-27,-59,-60,-21,-63,-22,-23,-62,-24,-25,-26,-27,-29,-30,-31,-32,-33,-37,-38,-27,-61,-27,-57,-27,-35,-36,-39,-28,111,-58,-14,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,-34,-27,-27,-13,114,115,-40,-41,-27,119,-42,]),'PARIZQ':([13,14,17,18,21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[20,21,24,25,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'IGUAL':([16,22,],[23,45,]),'PARDER':([20,28,29,30,31,32,33,34,36,37,38,39,40,41,42,54,58,59,60,62,65,78,81,82,83,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,],[26,66,-15,-16,-17,-18,-19,-20,-59,-60,-21,-63,-22,-23,-62,85,-37,-38,86,88,-61,-57,-35,-36,-39,-58,-43,-49,-53,-44,-45,-46,-47,-48,-65,-66,-68,-50,-51,-52,-54,-55,-56,-67,]),'MENOS':([21,23,24,25,27,29,35,36,37,38,39,42,45,49,55,62,65,67,68,69,70,71,72,73,74,75,76,77,78,79,81,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,],[35,35,35,35,35,68,35,-59,-60,-61,-63,-62,35,68,68,68,-61,35,35,35,35,35,35,35,35,35,35,35,-57,35,68,-58,-43,-49,-53,-44,-45,-46,-47,-48,68,68,68,-50,-51,-52,-54,-55,-56,]),'ENTERO':([21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'DECIMAL':([21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'CADENA':([21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'TRUE':([21,23,24,25,45,79,],[40,40,40,40,40,40,]),'FALSE':([21,23,24,25,45,79,],[41,41,41,41,41,41,]),'CHAR':([21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'PTCOMA':([22,36,37,38,39,40,41,42,48,49,50,51,52,53,58,59,65,66,78,80,81,82,83,88,90,91,92,93,94,95,96,97,101,102,103,104,105,106,],[46,-59,-60,-21,-63,-22,-23,-62,46,-29,-30,-31,-32,-33,-37,-38,-61,46,-57,46,-35,-36,-39,-58,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,]),'LLAVIZQ':([26,85,86,116,],[61,109,110,117,]),'MAS':([29,30,33,36,37,38,39,42,49,50,53,55,56,57,62,63,64,65,78,81,82,83,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,],[67,76,77,-59,-60,-61,-63,-62,67,76,77,67,77,76,67,77,76,-61,-57,67,76,77,-58,-43,-49,-53,-44,-45,-46,-47,-48,67,67,67,-50,-51,-52,-54,-55,-56,]),'POR':([29,36,37,38,39,42,49,55,62,65,78,81,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,],[69,-59,-60,-61,-63,-62,69,69,69,-61,-57,69,-58,69,-49,-53,69,-45,-46,-47,-48,69,69,69,-50,69,-52,-54,-55,69,]),'DIVIDIDO':([29,36,37,38,39,42,49,55,62,65,78,81,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,],[70,-59,-60,-61,-63,-62,70,70,70,-61,-57,70,-58,70,-49,-53,70,-45,-46,-47,-48,70,70,70,-50,70,-52,-54,-55,70,]),'ELEVADO':([29,36,37,38,39,42,49,55,62,65,78,81,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,],[71,-59,-60,-61,-63,-62,71,71,71,-61,-57,71,-58,71,-49,-53,71,71,71,-47,71,71,71,71,-50,71,-52,-54,-55,71,]),'MOD':([29,36,37,38,39,42,49,55,62,65,78,81,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,],[72,-59,-60,-61,-63,-62,72,72,72,-61,-57,72,-58,72,-49,-53,72,-45,-46,-47,-48,72,72,72,-50,72,-52,-54,-55,72,]),'IGUALQUE':([29,30,31,32,33,36,37,38,39,40,41,42,43,55,56,57,58,59,65,78,88,90,91,92,93,94,95,96,97,101,102,103,104,105,106,],[-35,-36,-37,-38,-39,-59,-60,-21,-63,-22,-23,-62,79,-35,-39,-36,-37,-38,-61,-57,-58,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,]),'MAYQUE':([29,36,37,38,39,42,55,65,78,88,90,91,92,93,94,95,96,97,101,102,103,104,105,106,],[73,-59,-60,-61,-63,-62,73,-61,-57,-58,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,]),'MENQUE':([29,36,37,38,39,42,55,65,78,88,90,91,92,93,94,95,96,97,101,102,103,104,105,106,],[74,-59,-60,-61,-63,-62,74,-61,-57,-58,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,]),'NIGUALQUE':([29,36,37,38,39,42,55,65,78,88,90,91,92,93,94,95,96,97,101,102,103,104,105,106,],[75,-59,-60,-61,-63,-62,75,-61,-57,-58,-43,-49,-53,-44,-45,-46,-47,-48,-50,-51,-52,-54,-55,-56,]),'ELSE':([115,],[116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,61,109,110,117,],[2,87,112,113,118,]),'instruccion':([0,2,61,87,109,110,112,113,117,118,],[3,19,3,19,3,3,19,19,3,19,]),'empty':([0,22,48,61,66,80,109,110,117,],[4,47,47,4,47,47,4,4,4,]),'func_main':([0,2,61,87,109,110,112,113,117,118,],[5,5,5,5,5,5,5,5,5,5,]),'imprimir_instr':([0,2,61,87,109,110,112,113,117,118,],[6,6,6,6,6,6,6,6,6,6,]),'definicion_instr':([0,2,61,87,109,110,112,113,117,118,],[7,7,7,7,7,7,7,7,7,7,]),'asignacion_instr':([0,2,61,87,109,110,112,113,117,118,],[8,8,8,8,8,8,8,8,8,8,]),'def_asig_instr':([0,2,61,87,109,110,112,113,117,118,],[9,9,9,9,9,9,9,9,9,9,]),'mientras_instr':([0,2,61,87,109,110,112,113,117,118,],[10,10,10,10,10,10,10,10,10,10,]),'if_instr':([0,2,61,87,109,110,112,113,117,118,],[11,11,11,11,11,11,11,11,11,11,]),'if_else_instr':([0,2,61,87,109,110,112,113,117,118,],[12,12,12,12,12,12,12,12,12,12,]),'print_expresion_general':([21,],[28,]),'expresion_numerica':([21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[29,49,55,55,62,78,81,90,93,94,95,96,97,98,99,100,102,106,81,]),'expresion_cadena':([21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[30,50,57,57,64,64,82,92,64,64,64,64,64,64,64,64,101,105,82,]),'expresion_id':([21,23,24,25,45,79,],[31,51,58,58,58,58,]),'expresion_boolean':([21,23,24,25,45,79,],[32,52,59,59,59,59,]),'expresion_char':([21,23,24,25,27,35,45,67,68,69,70,71,72,73,74,75,76,77,79,],[33,53,56,56,63,63,83,91,63,63,63,63,63,63,63,63,103,104,83,]),'expresion_logica':([21,24,25,],[34,54,60,]),'asign_def_expresion_general':([21,24,25,45,79,],[43,43,43,80,107,]),'def_instr_prima':([22,48,66,80,],[44,84,89,108,]),'asign_expresion_general':([23,],[48,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',156),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','grammar.py',161),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',167),
  ('instrucciones -> empty','instrucciones',1,'p_instrucciones_instruccion','grammar.py',168),
  ('instruccion -> func_main','instruccion',1,'p_instruccion','grammar.py',173),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','grammar.py',174),
  ('instruccion -> definicion_instr','instruccion',1,'p_instruccion','grammar.py',175),
  ('instruccion -> asignacion_instr','instruccion',1,'p_instruccion','grammar.py',176),
  ('instruccion -> def_asig_instr','instruccion',1,'p_instruccion','grammar.py',177),
  ('instruccion -> mientras_instr','instruccion',1,'p_instruccion','grammar.py',178),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','grammar.py',179),
  ('instruccion -> if_else_instr','instruccion',1,'p_instruccion','grammar.py',180),
  ('func_main -> MAIN PARIZQ PARDER LLAVIZQ instrucciones LLAVDER','func_main',6,'p_func_main','grammar.py',192),
  ('imprimir_instr -> PRINT PARIZQ print_expresion_general PARDER def_instr_prima','imprimir_instr',5,'p_instruccion_imprimir','grammar.py',197),
  ('print_expresion_general -> expresion_numerica','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',202),
  ('print_expresion_general -> expresion_cadena','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',203),
  ('print_expresion_general -> expresion_id','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',204),
  ('print_expresion_general -> expresion_boolean','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',205),
  ('print_expresion_general -> expresion_char','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',206),
  ('print_expresion_general -> expresion_logica','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',207),
  ('expresion_id -> ID','expresion_id',1,'p_expresionId','grammar.py',212),
  ('expresion_boolean -> TRUE','expresion_boolean',1,'p_expresionBoolean','grammar.py',217),
  ('expresion_boolean -> FALSE','expresion_boolean',1,'p_expresionBoolean','grammar.py',218),
  ('definicion_instr -> VAR ID def_instr_prima','definicion_instr',3,'p_instruccion_definicion','grammar.py',224),
  ('def_instr_prima -> PTCOMA','def_instr_prima',1,'p_instrDef_prima','grammar.py',229),
  ('def_instr_prima -> empty','def_instr_prima',1,'p_instrDef_prima','grammar.py',230),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',235),
  ('asignacion_instr -> ID IGUAL asign_expresion_general def_instr_prima','asignacion_instr',4,'p_asignacion_instr','grammar.py',240),
  ('asign_expresion_general -> expresion_numerica','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',245),
  ('asign_expresion_general -> expresion_cadena','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',246),
  ('asign_expresion_general -> expresion_id','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',247),
  ('asign_expresion_general -> expresion_boolean','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',248),
  ('asign_expresion_general -> expresion_char','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',249),
  ('def_asig_instr -> VAR ID IGUAL asign_def_expresion_general def_instr_prima','def_asig_instr',5,'p_definicion_asignacion','grammar.py',254),
  ('asign_def_expresion_general -> expresion_numerica','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',259),
  ('asign_def_expresion_general -> expresion_cadena','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',260),
  ('asign_def_expresion_general -> expresion_id','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',261),
  ('asign_def_expresion_general -> expresion_boolean','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',262),
  ('asign_def_expresion_general -> expresion_char','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',263),
  ('mientras_instr -> MIENTRAS PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER','mientras_instr',7,'p_mientras_instr','grammar.py',268),
  ('if_instr -> IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER','if_instr',7,'p_if_instr','grammar.py',273),
  ('if_else_instr -> IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER','if_else_instr',11,'p_if_else_instr','grammar.py',278),
  ('expresion_numerica -> expresion_numerica MAS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',283),
  ('expresion_numerica -> expresion_numerica MENOS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',284),
  ('expresion_numerica -> expresion_numerica POR expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',285),
  ('expresion_numerica -> expresion_numerica DIVIDIDO expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',286),
  ('expresion_numerica -> expresion_numerica ELEVADO expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',287),
  ('expresion_numerica -> expresion_numerica MOD expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',288),
  ('expresion_numerica -> expresion_numerica MAS expresion_char','expresion_numerica',3,'p_expresion_binaria','grammar.py',289),
  ('expresion_numerica -> expresion_cadena MAS expresion_cadena','expresion_numerica',3,'p_expresion_binaria','grammar.py',290),
  ('expresion_numerica -> expresion_cadena MAS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',291),
  ('expresion_numerica -> expresion_cadena MAS expresion_char','expresion_numerica',3,'p_expresion_binaria','grammar.py',292),
  ('expresion_numerica -> expresion_numerica MAS expresion_cadena','expresion_numerica',3,'p_expresion_binaria','grammar.py',293),
  ('expresion_numerica -> expresion_char MAS expresion_char','expresion_numerica',3,'p_expresion_binaria','grammar.py',294),
  ('expresion_numerica -> expresion_char MAS expresion_cadena','expresion_numerica',3,'p_expresion_binaria','grammar.py',295),
  ('expresion_numerica -> expresion_char MAS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',296),
  ('expresion_numerica -> MENOS expresion_numerica','expresion_numerica',2,'p_expresion_unaria','grammar.py',317),
  ('expresion_numerica -> PARIZQ expresion_numerica PARDER','expresion_numerica',3,'p_expresion_agrupacion','grammar.py',322),
  ('expresion_numerica -> ENTERO','expresion_numerica',1,'p_expresion_number','grammar.py',327),
  ('expresion_numerica -> DECIMAL','expresion_numerica',1,'p_expresion_number','grammar.py',328),
  ('expresion_numerica -> ID','expresion_numerica',1,'p_expresion_id','grammar.py',333),
  ('expresion_char -> CHAR','expresion_char',1,'p_expresion_char','grammar.py',338),
  ('expresion_cadena -> CADENA','expresion_cadena',1,'p_expresion_cadena','grammar.py',354),
  ('expresion_cadena -> expresion_numerica','expresion_cadena',1,'p_expresion_cadena_numerico','grammar.py',359),
  ('expresion_logica -> expresion_numerica MAYQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','grammar.py',364),
  ('expresion_logica -> expresion_numerica MENQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','grammar.py',365),
  ('expresion_logica -> asign_def_expresion_general IGUALQUE asign_def_expresion_general','expresion_logica',3,'p_expresion_logica','grammar.py',366),
  ('expresion_logica -> expresion_numerica NIGUALQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','grammar.py',367),
]
