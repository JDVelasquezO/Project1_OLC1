
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONCATleftMASMENOSleftPORDIVIDIDOrightUMENOSCADENA CONCAT DECIMAL DIVIDIDO ELSE ENTERO ID IF IGUAL IGUALQUE LLAVDER LLAVIZQ MAIN MAS MAYQUE MENOS MENQUE MIENTRAS NIGUALQUE PARDER PARIZQ POR PRINT PTCOMA VARinit       : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion      : func_main\n                        | imprimir_instr\n                        | definicion_instr\n                        | asignacion_instr\n                        | def_asig_instr\n                        | mientras_instr\n                        | if_instr\n                        | if_else_instrdef_funcs_vars   : definicion_instr\n                        | asignacion_instr\n                        | emptyfunc_main  : MAIN PARIZQ PARDER LLAVIZQ instrucciones LLAVDERimprimir_instr     : PRINT PARIZQ print_expresion_general PARDER def_instr_primaprint_expresion_general  :  expresion_numerica\n                            | expresion_cadena\n                            | expresion_idexpresion_id   : IDdefinicion_instr   : VAR ID def_instr_primadef_instr_prima   : PTCOMA\n                        | emptyempty :asignacion_instr   : ID IGUAL asign_expresion_general def_instr_primaasign_expresion_general  :  expresion_numerica\n                            | expresion_cadena\n                            | expresion_iddef_asig_instr     : VAR ID IGUAL asign_def_expresion_general def_instr_primaasign_def_expresion_general  :  expresion_numerica\n                                | expresion_cadena\n                                | expresion_idmientras_instr     : MIENTRAS PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDERif_instr           : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDERif_else_instr      : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDERexpresion_numerica : expresion_numerica MAS expresion_numerica\n                        | expresion_numerica MENOS expresion_numerica\n                        | expresion_numerica POR expresion_numerica\n                        | expresion_numerica DIVIDIDO expresion_numericaexpresion_numerica : MENOS expresion_numerica %prec UMENOSexpresion_numerica : PARIZQ expresion_numerica PARDERexpresion_numerica : ENTERO\n                        | DECIMALexpresion_numerica   : IDexpresion_cadena     : expresion_cadena CONCAT expresion_cadenaexpresion_cadena     : CADENAexpresion_cadena     : expresion_numericaexpresion_logica : expresion_numerica MAYQUE expresion_numerica\n                        | expresion_numerica MENQUE expresion_numerica\n                        | expresion_numerica IGUALQUE expresion_numerica\n                        | expresion_numerica NIGUALQUE expresion_numerica'
    
_lr_action_items = {'MAIN':([0,2,3,4,5,6,7,8,9,10,11,18,21,32,33,34,35,36,38,39,40,41,42,43,46,48,50,56,57,58,59,60,61,68,69,70,71,72,73,74,75,76,77,78,83,84,85,86,87,88,90,91,92,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-24,-42,-43,-20,-46,-21,-22,-23,-24,-26,-27,-28,-44,12,-24,-40,-24,-30,-31,-32,-25,12,-41,-16,-36,-37,-38,-39,-45,-47,-29,12,12,-15,12,12,-33,-34,12,12,-35,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,18,21,32,33,34,35,36,38,39,40,41,42,43,46,48,50,56,57,58,59,60,61,68,69,70,71,72,73,74,75,76,77,78,83,84,85,86,87,88,90,91,92,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-24,-42,-43,-20,-46,-21,-22,-23,-24,-26,-27,-28,-44,13,-24,-40,-24,-30,-31,-32,-25,13,-41,-16,-36,-37,-38,-39,-45,-47,-29,13,13,-15,13,13,-33,-34,13,13,-35,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,18,21,32,33,34,35,36,38,39,40,41,42,43,46,48,50,56,57,58,59,60,61,68,69,70,71,72,73,74,75,76,77,78,83,84,85,86,87,88,90,91,92,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-24,-42,-43,-20,-46,-21,-22,-23,-24,-26,-27,-28,-44,14,-24,-40,-24,-30,-31,-32,-25,14,-41,-16,-36,-37,-38,-39,-45,-47,-29,14,14,-15,14,14,-33,-34,14,14,-35,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,14,18,20,21,22,23,24,26,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,66,68,69,70,71,72,73,74,75,76,77,78,83,84,85,86,87,88,90,91,92,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,21,-2,34,-24,34,46,46,46,46,-42,-43,-20,-46,-21,34,-22,-23,-24,-26,-27,-28,-44,15,-24,46,46,46,46,46,-40,-24,-30,-31,-32,-25,46,46,46,46,15,-41,-16,-36,-37,-38,-39,-45,-47,-29,15,15,-15,15,15,-33,-34,15,15,-35,]),'MIENTRAS':([0,2,3,4,5,6,7,8,9,10,11,18,21,32,33,34,35,36,38,39,40,41,42,43,46,48,50,56,57,58,59,60,61,68,69,70,71,72,73,74,75,76,77,78,83,84,85,86,87,88,90,91,92,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-24,-42,-43,-20,-46,-21,-22,-23,-24,-26,-27,-28,-44,16,-24,-40,-24,-30,-31,-32,-25,16,-41,-16,-36,-37,-38,-39,-45,-47,-29,16,16,-15,16,16,-33,-34,16,16,-35,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,18,21,32,33,34,35,36,38,39,40,41,42,43,46,48,50,56,57,58,59,60,61,68,69,70,71,72,73,74,75,76,77,78,83,84,85,86,87,88,90,91,92,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-24,-42,-43,-20,-46,-21,-22,-23,-24,-26,-27,-28,-44,17,-24,-40,-24,-30,-31,-32,-25,17,-41,-16,-36,-37,-38,-39,-45,-47,-29,17,17,-15,17,17,-33,-34,17,17,-35,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,18,21,32,33,34,35,36,38,39,40,41,42,43,46,50,56,57,58,59,60,61,69,70,71,72,73,74,75,76,77,84,87,88,92,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-24,-42,-43,-20,-46,-21,-22,-23,-24,-26,-27,-28,-44,-24,-40,-24,-30,-31,-32,-25,-41,-16,-36,-37,-38,-39,-45,-47,-29,-15,-33,-34,-35,]),'LLAVDER':([3,4,5,6,7,8,9,10,11,18,21,32,33,34,35,36,38,39,40,41,42,43,46,50,56,57,58,59,60,61,68,69,70,71,72,73,74,75,76,77,84,85,86,87,88,91,92,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-24,-42,-43,-20,-46,-21,-22,-23,-24,-26,-27,-28,-44,-24,-40,-24,-30,-31,-32,-25,84,-41,-16,-36,-37,-38,-39,-45,-47,-29,-15,87,88,-33,-34,92,-35,]),'PARIZQ':([12,13,16,17,20,22,23,24,26,31,37,51,52,53,54,55,63,64,65,66,],[19,20,23,24,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'IGUAL':([15,21,],[22,37,]),'PARDER':([19,27,28,29,30,32,33,34,35,44,46,47,49,56,69,71,72,73,74,75,76,79,80,81,82,],[25,50,-17,-18,-19,-42,-43,-20,-46,62,-44,67,69,-40,-41,-36,-37,-38,-39,-45,-47,-48,-49,-50,-51,]),'MENOS':([20,22,23,24,26,28,31,32,33,34,37,41,45,46,49,51,52,53,54,55,56,58,63,64,65,66,69,71,72,73,74,76,79,80,81,82,],[31,31,31,31,31,52,31,-42,-43,-44,31,52,52,-44,52,31,31,31,31,31,-40,52,31,31,31,31,-41,-36,-37,-38,-39,52,52,52,52,52,]),'ENTERO':([20,22,23,24,26,31,37,51,52,53,54,55,63,64,65,66,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'DECIMAL':([20,22,23,24,26,31,37,51,52,53,54,55,63,64,65,66,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'CADENA':([20,22,37,55,],[35,35,35,35,]),'PTCOMA':([21,32,33,34,35,40,41,42,43,46,50,56,57,58,59,60,69,71,72,73,74,75,76,],[38,-42,-43,-20,-46,38,-26,-27,-28,-44,38,-40,38,-30,-31,-32,-41,-36,-37,-38,-39,-45,-47,]),'LLAVIZQ':([25,62,67,89,],[48,78,83,90,]),'MAS':([28,32,33,34,41,45,46,49,56,58,69,71,72,73,74,76,79,80,81,82,],[51,-42,-43,-44,51,51,-44,51,-40,51,-41,-36,-37,-38,-39,51,51,51,51,51,]),'POR':([28,32,33,34,41,45,46,49,56,58,69,71,72,73,74,76,79,80,81,82,],[53,-42,-43,-44,53,53,-44,53,-40,53,-41,53,53,-38,-39,53,53,53,53,53,]),'DIVIDIDO':([28,32,33,34,41,45,46,49,56,58,69,71,72,73,74,76,79,80,81,82,],[54,-42,-43,-44,54,54,-44,54,-40,54,-41,54,54,-38,-39,54,54,54,54,54,]),'CONCAT':([28,29,32,33,34,35,41,42,46,56,58,59,69,71,72,73,74,75,76,],[-47,55,-42,-43,-44,-46,-47,55,-44,-40,-47,55,-41,-36,-37,-38,-39,-45,-47,]),'MAYQUE':([32,33,45,46,56,69,71,72,73,74,],[-42,-43,63,-44,-40,-41,-36,-37,-38,-39,]),'MENQUE':([32,33,45,46,56,69,71,72,73,74,],[-42,-43,64,-44,-40,-41,-36,-37,-38,-39,]),'IGUALQUE':([32,33,45,46,56,69,71,72,73,74,],[-42,-43,65,-44,-40,-41,-36,-37,-38,-39,]),'NIGUALQUE':([32,33,45,46,56,69,71,72,73,74,],[-42,-43,66,-44,-40,-41,-36,-37,-38,-39,]),'ELSE':([88,],[89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,48,78,83,90,],[2,68,85,86,91,]),'instruccion':([0,2,48,68,78,83,85,86,90,91,],[3,18,3,18,3,3,18,18,3,18,]),'func_main':([0,2,48,68,78,83,85,86,90,91,],[4,4,4,4,4,4,4,4,4,4,]),'imprimir_instr':([0,2,48,68,78,83,85,86,90,91,],[5,5,5,5,5,5,5,5,5,5,]),'definicion_instr':([0,2,48,68,78,83,85,86,90,91,],[6,6,6,6,6,6,6,6,6,6,]),'asignacion_instr':([0,2,48,68,78,83,85,86,90,91,],[7,7,7,7,7,7,7,7,7,7,]),'def_asig_instr':([0,2,48,68,78,83,85,86,90,91,],[8,8,8,8,8,8,8,8,8,8,]),'mientras_instr':([0,2,48,68,78,83,85,86,90,91,],[9,9,9,9,9,9,9,9,9,9,]),'if_instr':([0,2,48,68,78,83,85,86,90,91,],[10,10,10,10,10,10,10,10,10,10,]),'if_else_instr':([0,2,48,68,78,83,85,86,90,91,],[11,11,11,11,11,11,11,11,11,11,]),'print_expresion_general':([20,],[27,]),'expresion_numerica':([20,22,23,24,26,31,37,51,52,53,54,55,63,64,65,66,],[28,41,45,45,49,56,58,71,72,73,74,76,79,80,81,82,]),'expresion_cadena':([20,22,37,55,],[29,42,59,75,]),'expresion_id':([20,22,37,],[30,43,60,]),'def_instr_prima':([21,40,50,57,],[36,61,70,77,]),'empty':([21,40,50,57,],[39,39,39,39,]),'asign_expresion_general':([22,],[40,]),'expresion_logica':([23,24,],[44,47,]),'asign_def_expresion_general':([37,],[57,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',138),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','grammar.py',143),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',149),
  ('instruccion -> func_main','instruccion',1,'p_instruccion','grammar.py',154),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','grammar.py',155),
  ('instruccion -> definicion_instr','instruccion',1,'p_instruccion','grammar.py',156),
  ('instruccion -> asignacion_instr','instruccion',1,'p_instruccion','grammar.py',157),
  ('instruccion -> def_asig_instr','instruccion',1,'p_instruccion','grammar.py',158),
  ('instruccion -> mientras_instr','instruccion',1,'p_instruccion','grammar.py',159),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','grammar.py',160),
  ('instruccion -> if_else_instr','instruccion',1,'p_instruccion','grammar.py',161),
  ('def_funcs_vars -> definicion_instr','def_funcs_vars',1,'p_beforeOfMain','grammar.py',166),
  ('def_funcs_vars -> asignacion_instr','def_funcs_vars',1,'p_beforeOfMain','grammar.py',167),
  ('def_funcs_vars -> empty','def_funcs_vars',1,'p_beforeOfMain','grammar.py',168),
  ('func_main -> MAIN PARIZQ PARDER LLAVIZQ instrucciones LLAVDER','func_main',6,'p_func_main','grammar.py',173),
  ('imprimir_instr -> PRINT PARIZQ print_expresion_general PARDER def_instr_prima','imprimir_instr',5,'p_instruccion_imprimir','grammar.py',178),
  ('print_expresion_general -> expresion_numerica','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',183),
  ('print_expresion_general -> expresion_cadena','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',184),
  ('print_expresion_general -> expresion_id','print_expresion_general',1,'p_expresionGeneralImprimir','grammar.py',185),
  ('expresion_id -> ID','expresion_id',1,'p_expresionId','grammar.py',190),
  ('definicion_instr -> VAR ID def_instr_prima','definicion_instr',3,'p_instruccion_definicion','grammar.py',195),
  ('def_instr_prima -> PTCOMA','def_instr_prima',1,'p_instrDef_prima','grammar.py',200),
  ('def_instr_prima -> empty','def_instr_prima',1,'p_instrDef_prima','grammar.py',201),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',206),
  ('asignacion_instr -> ID IGUAL asign_expresion_general def_instr_prima','asignacion_instr',4,'p_asignacion_instr','grammar.py',211),
  ('asign_expresion_general -> expresion_numerica','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',216),
  ('asign_expresion_general -> expresion_cadena','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',217),
  ('asign_expresion_general -> expresion_id','asign_expresion_general',1,'p_expresionGeneralAsignar','grammar.py',218),
  ('def_asig_instr -> VAR ID IGUAL asign_def_expresion_general def_instr_prima','def_asig_instr',5,'p_definicion_asignacion','grammar.py',223),
  ('asign_def_expresion_general -> expresion_numerica','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',228),
  ('asign_def_expresion_general -> expresion_cadena','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',229),
  ('asign_def_expresion_general -> expresion_id','asign_def_expresion_general',1,'p_expresionGeneralDefAsign','grammar.py',230),
  ('mientras_instr -> MIENTRAS PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER','mientras_instr',7,'p_mientras_instr','grammar.py',235),
  ('if_instr -> IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER','if_instr',7,'p_if_instr','grammar.py',240),
  ('if_else_instr -> IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER','if_else_instr',11,'p_if_else_instr','grammar.py',245),
  ('expresion_numerica -> expresion_numerica MAS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',250),
  ('expresion_numerica -> expresion_numerica MENOS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',251),
  ('expresion_numerica -> expresion_numerica POR expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',252),
  ('expresion_numerica -> expresion_numerica DIVIDIDO expresion_numerica','expresion_numerica',3,'p_expresion_binaria','grammar.py',253),
  ('expresion_numerica -> MENOS expresion_numerica','expresion_numerica',2,'p_expresion_unaria','grammar.py',265),
  ('expresion_numerica -> PARIZQ expresion_numerica PARDER','expresion_numerica',3,'p_expresion_agrupacion','grammar.py',270),
  ('expresion_numerica -> ENTERO','expresion_numerica',1,'p_expresion_number','grammar.py',275),
  ('expresion_numerica -> DECIMAL','expresion_numerica',1,'p_expresion_number','grammar.py',276),
  ('expresion_numerica -> ID','expresion_numerica',1,'p_expresion_id','grammar.py',281),
  ('expresion_cadena -> expresion_cadena CONCAT expresion_cadena','expresion_cadena',3,'p_expresion_concatenacion','grammar.py',286),
  ('expresion_cadena -> CADENA','expresion_cadena',1,'p_expresion_cadena','grammar.py',291),
  ('expresion_cadena -> expresion_numerica','expresion_cadena',1,'p_expresion_cadena_numerico','grammar.py',296),
  ('expresion_logica -> expresion_numerica MAYQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','grammar.py',301),
  ('expresion_logica -> expresion_numerica MENQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','grammar.py',302),
  ('expresion_logica -> expresion_numerica IGUALQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','grammar.py',303),
  ('expresion_logica -> expresion_numerica NIGUALQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','grammar.py',304),
]
