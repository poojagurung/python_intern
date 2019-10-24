#1

class A:
    def process(self):
        print('A process()')


class B:
    pass


class C(A, B):
    pass


obj = C()  
obj.process()    
print(C.mro())   # print MRO for class C

#2

class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')

class C(A, B):
    pass

obj = C()
obj.process()

#3

class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    def process(self):
        print('C process()')


class D(C,B):
    pass


obj = D()
obj.process()

print(D.mro())
