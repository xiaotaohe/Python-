# coding=utf8
#目标练习Python面向对象的基础语法
from distutils.command.install import install

class MyClass(object):
        message = 'Hello,Developer.'       
        #1.构造函数
        def __init__(self):
            print("the __init__ been called!")
        #2.析构函数
        def __def__(self):
            print("destructor is called")
        #成员函数
        def show(self):
            print(self.message)
mc = MyClass()
mc.show()

class MyClass1(object):
    message = "hello,Developer."
    #1.构造函数&私有成员 __
    def __init__(self,name="unset",color="black"):
        print("Constructor is called with param: ",name," ",color)
        self.__name = name
        self.__color = color
    #2.析构函数
    def __def__(self):
        print("destructor is called")
    #成员函数
    def show(self):
        print(self.message)
    #3.静态函数
    @staticmethod
    def printMessage():
        print("printMessage is called")
        print(MyClass1.message)
    #4.类函数
    @classmethod
    def creatObject(cls,name,color):
        print("Object will be created: %s(%s,%s)"%(cls.__name__,name,color))
        return cls(name,color)
def test():
    inst = MyClass1()
    inst.show()
    
    inst1 = MyClass1("David")
    inst1.show()
    
    del inst,inst1
    inst2 = MyClass1("Lisa","Yellow")
    inst2.show()
    
    inst3 = MyClass1(color = "Green")
    inst3.show()
    del inst2,inst3
    #测试静态函数与类函数
    MyClass1.printMessage()
    inst = MyClass1.creatObject("Toby","Red")
    print(inst.message)
    #测试私有成员
    #print(inst.__color) #类外访问私有会报错
    del inst
    
if __name__ == '__main__':
    test()
    
    
#继承测试（练习）
class Base(object):
    def __init__(self):
        print("Constructor of Base is called!")
    def __del__(self):
        print("Destructor of Base is called!")
    def move(self):
        print("move called in Base!")
class SubA(Base):
    def __init__(self):
        print("Constructor of SubA is called")
    def move(self):
        print("move called in SubA")
class SubB(Base):
    def __del__(self):
        print("Destructor of SubB is called!")
        super(SubB,self).__del__()
instA = SubA()
instA.move()
del instA

print("----------------------------")
instB = SubB()
instB.move()
del instB

