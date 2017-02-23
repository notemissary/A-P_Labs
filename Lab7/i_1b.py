# Dyma Volodymyr. KNIT16-A
# Дана непустая последовательность слов из строчных букв; между соседними
# словами -- запятая, за последним словом -- точка. Вывести на экран в
# алфавитном порядке все гласные буквы, которые входят в каждое слово.

ru_alpha = {"а", "е", "ё", "о", "у", "э", "я", "ю", "ы", "и"}
while True:
    inp = input().lower()
    if inp.endswith('.'):
        inp = set(inp.split(', '))
        if '.' in inp:
            inp.remove('.')
        res = set()
        t = None
        for i in ru_alpha:
            c = 0
            flag = False
            for j in inp:
                temp = set(j)
                if i in temp:
                    c += 1
                    flag = True
                    continue
                break
            if flag and c == len(inp):
                res.add(i)
                continue
        if len(res) > 0:
            print(sorted(res))
        else:
            print('Результат - пустое множество. '
                  'Возможно, ошибка ввода.')
    else:
        print('Последовательность должна заканчиваться точкой.')
    if input('Нажмите Enter, чтобы продолжить...') != '':
        break
