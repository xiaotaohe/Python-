# coding=utf8
#print("hello world!")

#����time��
import time
print("hello world!")

#����
def fbis(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
def print_fbis(num):
    a = 0; b = 1;
    print(a)
    print(b)
    i = 2;
    while(i<num):
        i += 1
        tmp = a+b
        a = b
        b = tmp
        print(tmp)
    return
def main():
    print_fbis(10)
    result = fbis(10)
    fobj = open('C:\Python_txt\\fbis.txt','w+')
    for i,num in enumerate(result):
        print (u"第%d个数是：%d" % (i,num))
        fobj.write("%d"%num)
        time.sleep(1)
if __name__ == '__main__':
    main()