# Дыма Владимир. КНИТ16-А
sign = {'+', '-', '*'}
digit = {range(10)}


def tr(text):
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

print(tr(input('=')))
