# Дыма Владимир. КНИТ16-А
sign = {'+', '-', '*'}
digit = {range(10)}


def tr(text):
    """
    Simple text calculator.
    
    :param text: Takes text.
    :return: Returns calculated result.
    """
    num = []
    sgn = []
    res = 0
    text = text.replace('.', '')
    if text.isdigit():
        return text
    a = ''
    for i in range(len(text)):
        if text[i].isdigit():
            a += text[i]
        elif text[i] in sign and i != 0:
            num.append(int(a))
            sgn.append(text[i])
            a = ''
        elif text[i] == ' ':
            pass
        else:
            return 'Error'
    num.append(int(a))
    res += num[0]
    for i in range(len(sgn)):
        if sgn[i] == '+':
            res += num[i+1]
        elif sgn[i] == '-':
            res -= num[i+1]
        else:
            res *= num[i+1]
    return res

while True:
    t = input('=')
    if t[0] in sign or t[-1] in sign:
        print('Start with an integer and end with it.')
        continue
    print('Result: {}'.format(tr(t)))
