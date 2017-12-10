import ply.lex as lex
import ply.yacc as yacc
from hell import *
stack_expression = []

tokens = [

    'INT',
    'REAL',
    'ID',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'POWER',
    'LEFT_PAR',
    'RIGHT_PAR',
    'SEMICOLON',
    'WHILE',
    'IF',
    'ELSE',
    'RL_OP',
    'LEFT_BRACES',
    'RIGHT_BRACES',
    'FLOAT',
    'VAR',
    'INTVAR',
    'COMMA',
    'LEFT_BRACKET',
    'RIGHT_BRACKET'

]

reserved = {
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'real': 'REAL',
    'var': 'VAR',
    'int': 'INTVAR',
}

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_POWER = r'\^'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'
t_SEMICOLON = r'\;'
t_RL_OP = r'==|<>|<=|>=|<|>'
t_LEFT_BRACES = r'\{'
t_RIGHT_BRACES = r'\}'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_COMMA = r'\,'
t_ignore = r' '

stack = []


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'POWER')
)


def p_program_p(p):
    '''
     p_program_p : program
                 | program p_program_p
    '''
    p[0] = p[1]
    # SEE LATER
    for i in stack:
       print(i)
    # print(stack)

def p_program(p):
    '''
    program : expression

            | cmd_rl
            | var_assign
            | VAR var_type var_declaration SEMICOLON
    '''
    p[0] = p[1]


def p_var_declaration_repeat(p):
    '''
    var_declaration_repeat : var_declaration SEMICOLON var_type var_type_id
    '''
    p[0] = (p[1], p[2], p[3], p[4])


def p_var_declaration(p):
    '''
    var_declaration : var_type_id
                    | var_declaration_repeat
    '''
    p[0] = p[1]


def p_var_rec(p):
    '''
    var_rec : var_type_id COMMA id_class
    '''
    p[0] = p[1]


def p_var_type_id(p):
    '''
    var_type_id : id_class
                | var_rec
    '''
    p[0] = p[1]


def p_var_type(p):
    '''
    var_type : REAL
             | INTVAR
    '''
    p[0] = p[1]


def p_id_array(p):
    '''
    id_array : ID LEFT_BRACKET INT RIGHT_BRACKET
             | ID LEFT_BRACKET ID RIGHT_BRACKET
    '''

    temp = create_temp()
    value = (temp + " = ", p[3], " * ", "4")
    p[0] = (p[1], p[2], value, p[4])


def p_id_class(p):
    '''
    id_class : ID
             | id_array
    '''
    p[0] = p[1]


def p_var_assign(p):
    '''
    var_assign : id_class EQUALS expression SEMICOLON
    '''
    # stack_expression = []
    expression = generate_c3e(p[1], p[2], p[3])

    # stack.append(expression)
    s = ""
    for i in stack_expression:
        s += str(i)

    stack_expression.clear()

    expression= s + expression
    p[0] = expression # "#(p[1], p[2], p[3])


def p_expression_var(p):
    '''
    expression : id_class
    '''
    p[0] = p[1]


def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
               | expression POWER expression
    '''

    # TODO: otimizar
    #    if last_temp() == 'T2' and ('T2' == p[1] or 'T2' == p[3]):
    #        temp = last_temp()
    #        reset_temp()
    #    else:
    temp = create_temp()
    expression = (temp + " = ", p[1], p[2], p[3])

    #  print(expression)
    if type(p[1]) is tuple and str(p[1][0]).startswith("T") and type(p[3]) and str(p[3][0]).startswith("T"):
        expression = generate_c3e(temp, " = ", p[1][0], p[2], p[3][0])
    else:
        expression = generate_c3e(temp, " = ", p[1], p[2], p[3])
    # print(expression)

        stack_expression.append(expression)
    p[0] = temp # expression # (temp, "=", p[1], p[2], p[3])


def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = (p[1])


def p_expression_par(p):
    '''
    expression : LEFT_PAR expression RIGHT_PAR
    '''
    p[0] = p[2]


def p_expression_co(p):
    '''
    expression_co : var_assign
                  | cmd_rl
    '''
    p[0] = p[1]


def p_expression_cr(p):
    '''
    expression_cr : expression_co expression_c
    '''
    p[0] = (p[1], p[2])


def p_expression_c(p):
    '''
    expression_c : expression_co
                 | expression_cr
    '''
    p[0] = p[1]


def p_expression_bra(p):
    '''
    expression_bra : LEFT_BRACES expression_c RIGHT_BRACES
    '''
    p[0] = p[2]


def p_expression_rl(p):
    '''
    expression_rl : expression RL_OP expression
    '''
    p[0] = ('expression_rl', p[1], p[2], p[3])


def p_cmd_if(p):
    '''
    cmd_if : IF LEFT_PAR expression_rl RIGHT_PAR expression_bra
    '''

    label_end = create_label('END')

    # S.cod: = E.cod ||

    e_local = str(p[3][1]) + ' '
    op = invert_op(p[3][2]) + ' '
    value = str(p[3][3]) + ' '
    s1_cod = p[5]

    code1 = generate_c3e(C3E.IF, e_local, op, value, C3E.GOTO, label_end)
    code2 = generate_c3e(s1_cod)
    code3 = generate_c3e(label_end, ':')

    # print(p[3][2])

    p[0] = (code1, code2, code3)


def p_cmd_ifelse(p):
    '''
    cmd_ifelse : IF LEFT_PAR expression_rl RIGHT_PAR expression_bra ELSE expression_bra
    '''
    label_end = create_label('END')
    label_else = create_label('ELSE')

    e_local = str(p[3][1]) + ' '
    op = invert_op(p[3][2]) + ' '
    value = str(p[3][3]) + ' '
    s1_cod = p[5]
    s2_cod = p[7]

    # TODO: ver conteúdo do p[0]
    c1 = generate_c3e(C3E.IF, e_local, op, value, C3E.GOTO, label_else)
    c2 = generate_c3e(s1_cod)
    c3 = generate_c3e(C3E.GOTO, label_end)
    c4 = generate_c3e(label_else, ":")
    c5 = generate_c3e(s2_cod)
    c6 = generate_c3e(label_end, ':')

    stack.append(c1)
    stack.append(c2)
    stack.append(c3)
    stack.append(c4)
    stack.append(c5)
    stack.append(c6)

    p[0] = (c1, c2, c3, c4, c5, c6)


def p_cmd_while(p):
    '''
    cmd_while : WHILE LEFT_PAR expression_rl RIGHT_PAR expression_bra
    '''

    e_cod = p[3]
    s1_cod = p[5]

    s_begin = create_label('WHILE')
    e_false = create_label('END')

    code = generate_c3e(s_begin, ':')
    code += generate_c3e(e_cod, ' ', C3E.GOTO, e_false)
    code += generate_c3e(s1_cod)
    code += generate_c3e(C3E.GOTO, s_begin)
    code += generate_c3e(e_false, ':')

    p[0] = code
    # ('cmd_while', p[1])


def p_cmd_rl(p):
    '''
    cmd_rl : cmd_while
                    | cmd_if
                    | cmd_ifelse
    '''
    p[0] = p[1]


def p_error(p):
    print("Syntax error found!")


parser = yacc.yacc()

with open("samples/if.txt", "r") as f:
    s = f.read().replace('\n', ' ')
    parser.parse(s)
