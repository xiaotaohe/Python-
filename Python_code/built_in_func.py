# coding=utf8
from filecmp import cmp
from pip._vendor.pytoml.writer import long

#测试内置函数

def main():
    a = 0;b = 1;
    tmp = cmp(a,b)
    print("tmp = ",tmp) #前者小 -1，反之 1，== 0
    print(str(a))
    print(type(a))
    print(bool(a))
    print(int(a))
    print(long(a))
    print(float(a))
    print(complex(a))
    return 
if __name__ == '__main__':
    main()
        
    