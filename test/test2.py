"""新类和经典类"""


class A:
    def name(self):
        return "a"


class B(A):
    def b(self):
        return "b"


class C(A):
    def name(self):
        return "c"


class D(B, C):
    def d(self):
        return "d"


print(D().name())  # 输出的是C 说明是广度优先 D->B->C->A
print(type(A))  # """新类和经典类"""


class A():
    def name(self):
        return "a"


class B(A):
    def b(self):
        return "b"


class C(A):
    def name(self):
        return "c"


class D(B, C):
    def d(self):
        return "d"


print(D().name())  # 输出的是C 说明是广度优先 D->B->C->A
print(type(A))


class AA:
    pass


class BB():
    pass


class CC():
    pass


print(type(AA))  # <class 'type'>
print(type(BB))  # <class 'type'>
print(type(CC))  # <class 'type'>
