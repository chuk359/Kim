print("Задание 1")
l = ['1', '11', '12', '22', '2', '13', '30', '33']
print(sorted(filter(lambda x : int(x) % 2 !=0, l), key = int))

print("Задание 2")
l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
s = []
def unpack(l,level):
    if len(l) != 0:
        for i in l:
            if isinstance(i, list):
                level += 1
                unpack(i,level)
                level = 0 
            else:
                s.append(i)
                i += (1)*level
def sum_list(l):
    unpack (l, 0)
    print("Сумма:", sum(s))

sum_list(l)

print("Задание 3")

def fib(x):
    if x == 1:
       fib_num = [0]
    elif x == 2:
        fib_num = [0, 1]
    else:
        fib_num = [0, 1]
        fib1 = 0
        fib2 = 1
        i = 0
        while i < x-2:
            f = fib1+fib2
            fib1 = fib2
            fib2 = f
            fib_num.append(f)    
            i += 1
    print(fib_num)


fib(5)
fib(10)

