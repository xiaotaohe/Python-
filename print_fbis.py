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

def main():
    result = fbis(10)
    fobj = open('C:\Python_txt\\fbis.txt','w+')
    for i,num in enumerate(result):
        print (u"第%d个数是：%d" % (i,num))
        fobj.write("%d"%num)
        time.sleep(1)
if __name__ == '__main__':
    main()