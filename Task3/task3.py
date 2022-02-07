size = int(input("Введите кол-во символов больше 35: ", ))
while size < 36:
    size = int(input("Вы ввели неверное число!"+'\n'+"Введите кол-во символов больше 35: ", ))
s = size+1
i = 0
z = 0
    
text = open('text.txt', 'r', encoding='utf-8')
tn = open('newtext.txt', 'w', encoding='utf-8')
t = (text.read())
l = len(t)+1
while z < l-size:
    z = t.rfind(' ', i, s)
    a = t.find('\n', i, z)
    if a > i:
        y = t[i:a]
        i = a
    else:
        y = t[i:z]
        m = len(y)
        x = 0
        while m < size:   
            b = y.find(' ', x, m)
            bb = y.rfind(' ',x, m)
            y = y[0:b]+'  '+y[b+1:m]
            x = b+2
            m +=1
            if b == bb:
                x = 0
        i = z+1
        y += '\n'
    tn = open('newtext.txt', 'a', encoding='utf-8')
    tn.write(y)
    s = i+size+1
tn.write(t[i:l])      
text.close()
tn.close()
print("Создан файл: newtext.txt")