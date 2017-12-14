labels = []
temps = []


def create_temp(reset=False):
    if not reset:
        count = len(temps)
        temps.append("T" + str(count + 1))

    return temps[-1]


def create_label(label):
    count = len(labels) + 1
    lbl = 'LABEL' + str(count)

    if label:
        lbl = label + str(count)

    labels.append(lbl)
    return lbl


def generate_c3e(*args, separator=' '):
    line = ''
    for arg in args:
        line += "{0}{1}".format(str(arg), separator)

    return line


def invert_op(op):
    if op == '>':
        return '<='
    elif op == '<':
        return '>='
    elif op == '<=':
        return '>'
    elif op == '>=':
        return '<'
    elif op == '==':
        return '!='
    else:
        return "=="


class C3E:
    ARRAY_MULTIPLIER = '4'
    TIMES = '*'
    ASSIGNMENT = ':='
    GOTO = 'GOTO'
    IF = 'IF'
    ELSE = 'ELSE'


def print_c3e(code):
    if type(code) != str:
        for chunk in code:
            if isinstance(chunk, (list, tuple)):
                print_c3e(chunk)
            else:
                print(chunk)
