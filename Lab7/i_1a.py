# Dyma Volodymyr. KNIT16-A
# Дана последовательность целых чисел а_1...а_n (могут быть повторяющиеся).
# Вывести на экран все числа, которые входят в последовательность по одному
# разу.

while True:
    try:
        a = input('Input integers separated by space: ')
        b = sorted(set(a.split()))
        c = set()
        if len(b) == 0:
            print('Enter something!')
            break
        set(map(int, b))
        for i in b:
            if a.count(i) == 1:
                c.add(i)
        if len(c) == 0:
            print('Result is an empty set.')
        else:
            print(sorted(c))
    except ValueError:
        print('Input integers, separated by spaces!')
    if input('Press Enter to continue...') != '':
        break
