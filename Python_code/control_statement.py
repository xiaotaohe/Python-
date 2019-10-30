# coding=utf8
import sys
import datetime
from pip._vendor.distlib.compat import raw_input

param = 100

if len(sys.argv)>1:
    param = int(sys.argv[1])
if param is None:
    print("Alert")
    print("The param is set")
elif param<-10:
    print("The param is small")
elif param>10:
    print("The param is big")
else:
    print("The param is middle")
#循环语句
mylist = ["English","chinese","Japanese","German","France"]
for language in mylist:
    print("Current element is: ",language)
while len(mylist)>0:
    print("pop element out ",mylist.pop())

count = 0;
while True:
    break #快速逃过，测试下面
    input = raw_input("Enter quit: ")
    #检测非法密码
    if input == "quit":
        break
    count = count+1
    if count%3>0:
        continue
    elif count%3 == 0:
        break
print("please input quit")
print("Quit loop successfully!")

#嵌套语句，通过嵌套语句实现冒泡排序
mylist = [1,5,4,3,2,6,10,7,8]
print("before sort: ")
print(mylist)

lenlist = len(mylist)
for i in range(0,lenlist):
    for j in range(i+1,lenlist):
        if mylist[i]>mylist[j]:
            mylist[i],mylist[j] = mylist[j],mylist[i]
print("after sort: ")
print(mylist)    

#变长参数
#1.元组变长参数
def show_message(message,*tupleName):
    for name in tupleName:
        print(message,",",name)
if __name__ == '__main__':
    show_message("Good morning","Jack","Evens","Rose Hase",893,"Zion")
#2.字典变长参数
def check_book(**dictparam):
    if 'Price' in dictparam:
        price = int(dictparam['Price'])
        if price > 100:
            print("*******I want buy this book!*****")
    print("the book information are as follow:")
    for key in dictparam.keys():
        print(key,": ",dictparam[key])
    print("")
if __name__ == '__main__':
    check_book(author ='James',Title = 'Economic Introduction')
    check_book(author = 'Linda',Title = 'Deepin in Python',Price = 302)
    check_book(Date = "2019-3-10",Tile = 'Cooking',Price = 20)

#匿名函数
def nameFunc(a):
    return "I'm named function with param %s" % a
def call_func(func,param):
    print(datetime.datetime.now())
    print(func(param))
    print("")
if __name__ == '__main__':
    call_func(nameFunc, "hello")
    call_func(lambda x:x*2,9)
    call_func(lambda y:print(y),-4)
#异常
try:
    result = 3/0
    print("This never been called")
except:
    print("Excption happened")
finally:
    print("Process finished!")    
    
#多个ecept块捕捉异常
try:
    mylist = [4,6]
    print(mylist[10])
    print("this is never been called")
except ZeroDivisionError:
    print("ZeroDivisionError happened")
except IndexError:
    print("IndexError happened")
except EOFError:
    print("EOFError happened")
else:
    print("No exception happened")
finally:
    print("Process finished")

#自定义异常

class MyError(Exception):
    def __str__(self):
        return "I'm a self-defined Error!"
def main():
    try:
        #raw_input();
        print("********Start of main********")
        if False:
            raise MyError()
        print("***********End of main***********")
    except MyError:
        print("myerror happened")
if __name__ == '__main__':
    main()
a = 10;b = 12
print(a+b)


    