# locals() 지역 이름공간

global_var = 77


def myfunc():
    global global_var
    global_var += 1
    print(global_var)


myfunc()

var = 77


def func():
    global var
    var = 100
    print(locals())


func()
print(var)


def local_func():
    var = 100
    print(locals())

local_func()