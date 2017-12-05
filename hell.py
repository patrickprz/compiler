labels = []
temps = []

'''
def last_temp():
    if len(temporaria) > 0:
        return temporaria[-1]


def reset_temp():
    del temporaria[:]
'''

def create_temp(reset=False):
    count = 0
    if not reset:
        count = len(temps)

    # if count < 2:
        temps.append("T" + str(count + 1))

    return temps[-1]


def create_label(lbl):
    count = len(labels) + 1
    label = 'LABEL' + str(count)

    if lbl:
        label = lbl + str(count)

    labels.append(label)
    return label


def generate_c3e(*args):
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
    ELSE = 'ELSE'
