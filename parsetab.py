
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEleftPOWERINT REAL ID PLUS MINUS DIVIDE MULTIPLY EQUALS POWER LEFT_PAR RIGHT_PAR SEMICOLON WHILE IF ELSE RL_OP LEFT_BRACES RIGHT_BRACES FLOAT VAR INTVAR COMMA LEFT_BRACKET RIGHT_BRACKET\n     p_program_p : program\n                 | program p_program_p\n    \n    program : expression\n            | expression_ctrl\n            | var_assign\n            | VAR var_type var_declaration SEMICOLON\n    \n    var_declaration : var_type_id\n                    | var_declaration SEMICOLON var_type var_type_id\n    \n    var_type_id : id_class\n                | var_type_id COMMA id_class\n    \n    var_type : REAL\n             | INTVAR\n    \n    id_class : ID\n             | ID LEFT_BRACKET INT RIGHT_BRACKET\n             | ID LEFT_BRACKET ID RIGHT_BRACKET\n    \n    var_assign : id_class EQUALS expression SEMICOLON\n    \n    expression : id_class\n    \n    expression : expression MULTIPLY expression\n               | expression DIVIDE expression\n               | expression PLUS expression\n               | expression MINUS expression\n               | expression POWER expression\n    \n    expression : INT\n               | FLOAT\n    \n    expression : LEFT_PAR expression RIGHT_PAR\n    \n    expression_co : var_assign\n                  | expression_ctrl\n    \n    expression_c : expression_co\n                 | expression_co expression_c\n    \n    expression_bra : LEFT_BRACES expression_c RIGHT_BRACES\n    \n    expression_rl : expression RL_OP expression\n    \n    expression_ctrl : WHILE LEFT_PAR expression_rl RIGHT_PAR expression_bra\n                    | IF LEFT_PAR expression_rl RIGHT_PAR expression_bra\n                    | IF LEFT_PAR expression_rl RIGHT_PAR expression_bra ELSE expression_bra\n    '
    
_lr_action_items = {'$end':([2,3,4,8,9,10,11,12,13,22,28,32,33,34,35,36,37,45,49,50,51,55,57,65,67,],[-5,-3,-23,-17,-13,-24,0,-1,-4,-17,-2,-18,-21,-22,-19,-20,-25,-6,-16,-14,-15,-32,-33,-30,-34,]),'RIGHT_BRACKET':([42,43,],[50,51,]),'COMMA':([9,29,30,50,51,52,58,],[-13,44,-9,-14,-15,-10,44,]),'POWER':([3,4,8,9,10,22,23,32,33,34,35,36,37,39,41,50,51,56,],[19,-23,-17,-13,-24,-17,19,19,19,-22,19,19,-25,19,19,-14,-15,19,]),'ELSE':([57,65,],[64,-30,]),'SEMICOLON':([4,9,10,22,29,30,31,32,33,34,35,36,37,41,50,51,52,58,],[-23,-13,-24,-17,-7,-9,45,-18,-21,-22,-19,-20,-25,49,-14,-15,-10,-8,]),'VAR':([0,2,3,4,8,9,10,12,13,22,32,33,34,35,36,37,45,49,50,51,55,57,65,67,],[1,-5,-3,-23,-17,-13,-24,1,-4,-17,-18,-21,-22,-19,-20,-25,-6,-16,-14,-15,-32,-33,-30,-34,]),'LEFT_BRACES':([46,48,64,],[54,54,54,]),'INTVAR':([1,45,],[15,15,]),'REAL':([1,45,],[16,16,]),'INT':([0,2,3,4,5,8,9,10,12,13,17,18,19,20,21,22,24,25,26,27,32,33,34,35,36,37,45,47,49,50,51,55,57,65,67,],[4,-5,-3,-23,4,-17,-13,-24,4,-4,4,4,4,4,4,-17,4,4,4,42,-18,-21,-22,-19,-20,-25,-6,4,-16,-14,-15,-32,-33,-30,-34,]),'MINUS':([3,4,8,9,10,22,23,32,33,34,35,36,37,39,41,50,51,56,],[18,-23,-17,-13,-24,-17,18,-18,-21,-22,-19,-20,-25,18,18,-14,-15,18,]),'LEFT_BRACKET':([9,],[27,]),'RIGHT_BRACES':([49,55,57,59,60,61,62,65,66,67,],[-16,-32,-33,65,-27,-28,-26,-30,-29,-34,]),'LEFT_PAR':([0,2,3,4,5,6,7,8,9,10,12,13,17,18,19,20,21,22,24,25,26,32,33,34,35,36,37,45,47,49,50,51,55,57,65,67,],[5,-5,-3,-23,5,24,25,-17,-13,-24,5,-4,5,5,5,5,5,-17,5,5,5,-18,-21,-22,-19,-20,-25,-6,5,-16,-14,-15,-32,-33,-30,-34,]),'DIVIDE':([3,4,8,9,10,22,23,32,33,34,35,36,37,39,41,50,51,56,],[20,-23,-17,-13,-24,-17,20,-18,20,-22,-19,20,-25,20,20,-14,-15,20,]),'IF':([0,2,3,4,8,9,10,12,13,22,32,33,34,35,36,37,45,49,50,51,54,55,57,60,61,62,65,67,],[7,-5,-3,-23,-17,-13,-24,7,-4,-17,-18,-21,-22,-19,-20,-25,-6,-16,-14,-15,7,-32,-33,-27,7,-26,-30,-34,]),'ID':([0,2,3,4,5,8,9,10,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,32,33,34,35,36,37,44,45,47,49,50,51,53,54,55,57,60,61,62,65,67,],[9,-5,-3,-23,9,-17,-13,-24,9,-4,9,-12,-11,9,9,9,9,9,-17,9,9,9,43,-18,-21,-22,-19,-20,-25,9,-6,9,-16,-14,-15,9,9,-32,-33,-27,9,-26,-30,-34,]),'FLOAT':([0,2,3,4,5,8,9,10,12,13,17,18,19,20,21,22,24,25,26,32,33,34,35,36,37,45,47,49,50,51,55,57,65,67,],[10,-5,-3,-23,10,-17,-13,-24,10,-4,10,10,10,10,10,-17,10,10,10,-18,-21,-22,-19,-20,-25,-6,10,-16,-14,-15,-32,-33,-30,-34,]),'RIGHT_PAR':([4,9,10,22,23,32,33,34,35,36,37,38,40,50,51,56,],[-23,-13,-24,-17,37,-18,-21,-22,-19,-20,-25,46,48,-14,-15,-31,]),'RL_OP':([4,9,10,22,32,33,34,35,36,37,39,50,51,],[-23,-13,-24,-17,-18,-21,-22,-19,-20,-25,47,-14,-15,]),'MULTIPLY':([3,4,8,9,10,22,23,32,33,34,35,36,37,39,41,50,51,56,],[17,-23,-17,-13,-24,-17,17,-18,17,-22,-19,17,-25,17,17,-14,-15,17,]),'EQUALS':([8,9,50,51,63,],[26,-13,-14,-15,26,]),'WHILE':([0,2,3,4,8,9,10,12,13,22,32,33,34,35,36,37,45,49,50,51,54,55,57,60,61,62,65,67,],[6,-5,-3,-23,-17,-13,-24,6,-4,-17,-18,-21,-22,-19,-20,-25,-6,-16,-14,-15,6,-32,-33,-27,6,-26,-30,-34,]),'PLUS':([3,4,8,9,10,22,23,32,33,34,35,36,37,39,41,50,51,56,],[21,-23,-17,-13,-24,-17,21,-18,-21,-22,-19,-20,-25,21,21,-14,-15,21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression_rl':([24,25,],[38,40,]),'var_type':([1,45,],[14,53,]),'id_class':([0,5,12,14,17,18,19,20,21,24,25,26,44,47,53,54,61,],[8,22,8,30,22,22,22,22,22,22,22,22,52,22,30,63,63,]),'expression_ctrl':([0,12,54,61,],[13,13,60,60,]),'expression_bra':([46,48,64,],[55,57,67,]),'p_program_p':([0,12,],[11,28,]),'var_type_id':([14,53,],[29,58,]),'program':([0,12,],[12,12,]),'expression_c':([54,61,],[59,66,]),'var_assign':([0,12,54,61,],[2,2,62,62,]),'expression':([0,5,12,17,18,19,20,21,24,25,26,47,],[3,23,3,32,33,34,35,36,39,39,41,56,]),'expression_co':([54,61,],[61,61,]),'var_declaration':([14,],[31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> p_program_p","S'",1,None,None,None),
  ('p_program_p -> program','p_program_p',1,'p_program_p','program.py',95),
  ('p_program_p -> program p_program_p','p_program_p',2,'p_program_p','program.py',96),
  ('program -> expression','program',1,'p_program','program.py',103),
  ('program -> expression_ctrl','program',1,'p_program','program.py',104),
  ('program -> var_assign','program',1,'p_program','program.py',105),
  ('program -> VAR var_type var_declaration SEMICOLON','program',4,'p_program','program.py',106),
  ('var_declaration -> var_type_id','var_declaration',1,'p_var_declaration','program.py',112),
  ('var_declaration -> var_declaration SEMICOLON var_type var_type_id','var_declaration',4,'p_var_declaration','program.py',113),
  ('var_type_id -> id_class','var_type_id',1,'p_var_type_id','program.py',119),
  ('var_type_id -> var_type_id COMMA id_class','var_type_id',3,'p_var_type_id','program.py',120),
  ('var_type -> REAL','var_type',1,'p_var_type','program.py',125),
  ('var_type -> INTVAR','var_type',1,'p_var_type','program.py',126),
  ('id_class -> ID','id_class',1,'p_id_class','program.py',132),
  ('id_class -> ID LEFT_BRACKET INT RIGHT_BRACKET','id_class',4,'p_id_class','program.py',133),
  ('id_class -> ID LEFT_BRACKET ID RIGHT_BRACKET','id_class',4,'p_id_class','program.py',134),
  ('var_assign -> id_class EQUALS expression SEMICOLON','var_assign',4,'p_var_assign','program.py',139),
  ('expression -> id_class','expression',1,'p_expression_var','program.py',145),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','program.py',151),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','program.py',152),
  ('expression -> expression PLUS expression','expression',3,'p_expression','program.py',153),
  ('expression -> expression MINUS expression','expression',3,'p_expression','program.py',154),
  ('expression -> expression POWER expression','expression',3,'p_expression','program.py',155),
  ('expression -> INT','expression',1,'p_expression_int_float','program.py',163),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','program.py',164),
  ('expression -> LEFT_PAR expression RIGHT_PAR','expression',3,'p_expression_par','program.py',170),
  ('expression_co -> var_assign','expression_co',1,'p_expression_co','program.py',176),
  ('expression_co -> expression_ctrl','expression_co',1,'p_expression_co','program.py',177),
  ('expression_c -> expression_co','expression_c',1,'p_expression_c','program.py',183),
  ('expression_c -> expression_co expression_c','expression_c',2,'p_expression_c','program.py',184),
  ('expression_bra -> LEFT_BRACES expression_c RIGHT_BRACES','expression_bra',3,'p_expression_bra','program.py',190),
  ('expression_rl -> expression RL_OP expression','expression_rl',3,'p_expression_rl','program.py',196),
  ('expression_ctrl -> WHILE LEFT_PAR expression_rl RIGHT_PAR expression_bra','expression_ctrl',5,'p_cmd_rl','program.py',202),
  ('expression_ctrl -> IF LEFT_PAR expression_rl RIGHT_PAR expression_bra','expression_ctrl',5,'p_cmd_rl','program.py',203),
  ('expression_ctrl -> IF LEFT_PAR expression_rl RIGHT_PAR expression_bra ELSE expression_bra','expression_ctrl',7,'p_cmd_rl','program.py',204),
]
