l = list(map(int,input('Введите список неповторяющихся целых чисел по возрастанию через пробел:  ').split()))
def get_ranges(list):
    l_new = []
    l_new.append(list[0])
    for i  in range (1, len(list)-1):
        if list[i]+1 == list[i+1]:
            continue
        else:
            l_new.append(list[i])
            l_new.append(list[i+1])
    l_new.append(list[-1])
    print(sorted(set(l_new)))
get_ranges(l)
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10])
get_ranges([2, 3, 8, 9])


