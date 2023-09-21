class A:
    def m1(self):
        print("Método de A")

class B:
    def m2(self):
        print("Método de B")

    def m3(self):
        print("Método M3")

class C:
    def m2(self):
        print("Método de C")

    def m4(self):
        print("Método M4")

class D(B, C):
    def m2(self):
        super().m2()

if __name__ == '__main__':
    d = D()
    d.m2()
    d.m3()
    d.m4()
    print(D.mro())
    print(D.__mro__)