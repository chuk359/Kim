import data
import re

def calculation(expresion: str) -> str: 
    while (match := re.search(data.priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), calculation(match.group(1))) 
    for symbol, action in data.actions.items():
        while (match := re.search(data.action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
    return expresion

def choise(c):
    while c not in {'y','n'}:
        c = input('Произвести еще вычисление? y/n: ')
    if c == 'y':
        l = input('Введите выражение: ')
        print('Ответ:', calculation(l))
        c = input('Произвести еще вычисление? y/n: ')
        choise(c)
