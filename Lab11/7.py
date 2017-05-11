import os
os.chdir('D:/NewFold')
os.chdir('D:/NewFold/Anketa')
print('We\'re here now: {}'.format(os.getcwd()))
ans = []
while True:
    name = input('What\'s your name?\n'
                 '> ')
    if not (name.isalpha() and name.istitle()):
        print('Please input name!')
        continue
    age = input('How old are you?\n'
                '> ')
    if int(age) not in range(10, 101):
        print('You\'re too young or too old! Call someone else to take the '
              'test :)')
        continue
    phone = input('Your phone number?\n'
                  '> ')
    if not phone.startswith('+') or len(phone) != 13:
        print('Number must start with + and has length of 13!')
        continue
    email = input('Your e-mail?\n'
                  '> ')
    if not ('@' and '.') in email:
        print('Please, provide an actual email address!')
        continue
    with open('Anket.txt', 'w') as g:
        g.write('Имя: ' + name + '\n')
        g.write('Возраст: ' + age + '\n')
        g.write('Моб. номер: ' + phone + '\n')
        g.write('Электроннный адрес: ' + email + '\n')
    with open('Anket.txt') as f:
        line = f.readlines()
    for i in line:
        print(i, sep='')
    if input('Press Enter to continue...') != '':
        break
