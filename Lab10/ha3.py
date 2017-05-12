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
    flag1 = False
    flag = False
    sgn = []
    res = 0
    text = text.replace('.', '')
    if text.isdigit():
        return text
    a = ''
    for i in range(len(text)):
        if text[i] == '(':
            if not flag1:
                num.append(0)
                sgn.append('+')
            flag = True
            if sgn[-1] == '+':
                res += tr(text[i+1:]) + num[-1]
            elif sgn[-1] == '-':
                res += tr(text[i+1:]) - num[-1]
            elif sgn[-1] == '*':
                res += tr(text[i+1:]) * num[-1]
        else:
            flag1 = True
            if text[i].isdigit():
                a += text[i]
            elif text[i] in sign and i != 0:
                num.append(int(a))
                sgn.append(text[i])
                a = ''
            elif text[i] == ' ' or text[i] == ')':
                pass
            else:
                return 'Error'
    if not flag:
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
    if t[0] not in digit and t[-1] != '.':
        print('Start with an integer and end with the dot. Otherwise it\'s not a formula.')
        continue
    if t is '.':
        print('You\'ve input a dot. It\'s not a formula.')
        continue
    print('Result: {}'.format(tr(t)))
