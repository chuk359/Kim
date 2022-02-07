l = list(map(int,input('Введите сумму, которую заплатил каждый участник через пробел:  ').split()))
t = int(input('Введите сумму чаевых: '))
s =sum(l)/len(l)
max_payed = []
min_payed = []
print("Счет без чаевых составил: ", sum(l)-t)
for i in range (len(l)):
    if s < l[i]:
        total = l[i] - s
        max_payed.insert(i, total)
        min_payed.insert(i, 0)
    elif s == l[i]:
        min_payed.insert(i, 0)
        max_payed.insert(i, 0)
        print("Участник", i+1, "расчитался за себя")
    else:   
        total = s - l[i]
        min_payed.insert(i,total)
        max_payed.insert(i, 0)
while sum(max_payed) > 0.01 and sum(min_payed) > 0.01:
    if max(max_payed) >= max(min_payed):
        a = max_payed.index(max(max_payed))
        b = min_payed.index(max(min_payed))
        print("Участник", b+1, "должен участнику", a+1 , round(min_payed[b],2))
        max_payed[a] -= min_payed[b]
        min_payed[b] -= min_payed[b]
    else:
        a = max_payed.index(max(max_payed))
        b = min_payed.index(max(min_payed))
        print("Участник", b+1, "должен участнику", a+1 ,round(max_payed[a],2))
        min_payed[b] -= max_payed[a]
        max_payed[a] -= max_payed[a]