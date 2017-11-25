labels = []


def cria_label(lbl):
    count = len(labels) + 1
    label = 'LABEL' + str(count)

    if lbl:
        label = lbl + str(count)

    labels.append(label)
    return label


def gera(*args):
    line = ''
    for arg in args:
        line += str(arg)

    print(line)


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
    GOTO = 'GOTO '
    IF = 'IF '
