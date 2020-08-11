def returnTuple(x, y, z):
    return x, y, z
#return은 한 개만 할 수 있다
x, y, z = returnTuple(1, 2, 3)
print(x)

#여러개인 경우 tuple을 만들어 한 개를 반환!!
print(returnTuple(1, 2, 3))

a, b = (1, 2)
print(a)