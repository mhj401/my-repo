#중첩함수
def outter():
    def inner():
        print("inner")
    print(locals())
    inner()

outter()