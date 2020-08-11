# 함수 내부에 yield를 사용하면 제너레이터 함수가 된다.

def my_gen():
    n = 0
    while n <= 10:
        yield n
        n += 1


a = my_gen()
type(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

