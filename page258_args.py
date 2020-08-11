def argsfunc(*args):
    i = 0
    for x in args:
        i += 1
    print("인수의 개수%d" % i)
    print(args)


argsfunc(1, 2, (3, 4, 5))
argsfunc(1, [7, 55], "test", {'a': 1, 'b': 100})

a = 1;
b = (3, 6, 9);
c = {'x': 0, 'y': 99}
argsfunc(a, b, c)


def dictsfunc(**dicts):
    i = 0
    for x in dicts.keys():
        i += 1
    print("인수의 개수: %d" % i)
    print(dicts)


# 키워드 인수 형태
dictsfunc(a=1, b=2, c=3)
# 사전 형태
dictsfunc(**{'a': 1, 'b': 2, 'c': 3})