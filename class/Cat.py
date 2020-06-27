class Cat:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("%s mao eat..." % self.name)
    def drink(self):
        print("%s mao drink..." % self.name)
    def __str__(self):
        return self.name


# python 初始化 先分配内存空间 然后默认调用__init__
tom = Cat('Tom')
tom.eat()
tom.drink()

addr = id(tom)
print("tom's memory address:", addr)
print("tom's memory address: %x ->" % addr)

# python 可以实时增加属性
tom.name = 'Jimmy'
print("tom: ", tom)

class A:
    def __init__(self):
        self.name = 'nasa'
        self.num = 100
        self.__num2 = 200
    def __test(self):
        print("我是一个私有方法：%s, %d" % (self.name, self.__num2))
    def pub_test(self):
        print("我是一个共有方法：%s, %d" % (self.name, self.__num2))
    pass
class B(A):
    def __test(self):
        pass

    pass
class C(B,object):

    pass


b = B()
print("b: ", b.pub_test(), "----->", b)
c =C()
print("c: ", c.pub_test())