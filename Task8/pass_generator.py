import random
len = int(input('Введите длинну пароля:'))
sp = input('Использовать спец символы? y/n:')
y = int(input('Какое количество паролей требуется? '))

while sp != 'y' and sp != 'n':
    sp = input('Использовать спец символы? y/n:')
if sp == 'y':
    simb = list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*()=+-_/?.,*')
else:
    simb = list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')

def pass_generator(len,simb):
    pas = ''
    for x in range(len):
        pas = pas + random.choice(simb)
    return pas

def passprint(len, simb):
    while True:
        yield pass_generator(len, simb)

for i in range(y):
    password = iter(passprint(len, simb))
    print(next(password))