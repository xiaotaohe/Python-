# coding=utf8


#目标：Sequence类型族
#序列类型族（String（字符串）、Tuple（元组）、List（列表））

#字符串操作
a = "Hello, I like python Web Practice"
b = a[1]
print("b = ",b)
b = a[7:13] # I like
print("b = ",b)
print(a[:13]) #Hello, I like
print(a[14:]) #pyth.....
print("like" in a) # True
print(a+"!!") # Hell........ !!
print(a)
print('ABC'*3) #重复生成
c = [2,4,"apple",5]
print(c[1:]) # 4,"apple" 5
print(b+" "+c[2]) #I like apple
#内置函数
b = [1,2,3,4]   #list
#1.迭代器enumerate
for i,num in enumerate(b):
    print(u"第%d个数是: %d"%(i,num))
for i,num in enumerate(b):
    print(num)
#2.函数len
print("b len is ",len(b))
#3.list,将b转换为list
print("b type is ",type(b))
c = list(b);
print("c type is ",type(c))
#4.max函数
print("max in b is ",max(b))
print("max in the Sequence is ",max(1,4,6,3))
#6.min函数
print("min in b is ",min(b))
print("min in the Sequence is ",min(2,3,1,7))
#7.reversed反转
c = reversed(b)
for i,num in enumerate(c):
    print(num)



# 1.String
str1 = "Hello,World!" #普通字符串
str2 = u"Hello,I'm unicode" #unicode字符串
str3 = u"你好，世界"  #unicode字符串
print(str1," ",str2," ",str3)
# 2.通用切片操作
print(str1[5])
print(str1[6:])
# 3.追加&删除
str1 += " I like Python"
#以下两种操作效果一样
#str1 = str1[:5]+str1[-7:]
str1 = str1[:5]+str1[19:]
print(str1)
# 4.字符串格式化
#1.格式化字符串指按照指定规则连接、替换字符串并返回新的符合要求的字符串
charA = 65
charB = 66
print(u"ASCII码65代表:%c "%charA)
print(u"ASCII码66代表:%c "%charB)
#2.格式标记字符串
print("%#x"%108) #十六进制数字 结果 0x6c
print("%x"%108)  #结果 6c
print('%E'%1234.567890) #科学计数法
print('Host: %s\tPost: %d'%('python',90)) #多个参数
print('MM/DD/YY = %02d/%02d/%d'%(2,5,95)) #数字前补零
#3.内置函数
#split
a = "hello, world!"
c = a.split(",")
print(c)
#isalpha
print(a.isalpha())


#  2.List
#1.基本操作
mylist = ['you',456,'English',9.34] #定义
print(mylist[2]) #读取元素
print(mylist[1:]) #读取下标为1之后的所有元素

mylist[2] = 'France' #可以修改内容
print(mylist[0:])

numlist = [1,6,9,8,5,6,13,12]
print(sorted(numlist)) #排序并打印
print(numlist) #排序后的numlist本身并不改变
print(sum(numlist)) #求和
#2.内置函数
numlist.append(67) #在列表末尾添加元素
print(numlist)
print(numlist.count(1)) #查找某元素出现的次数
numlist.reverse() #反向本身是对序列有改变的
print(numlist)
numlist.sort()
print(numlist)

#3.Set集合
#set定义普通集合 frozenset定义不可变集合
sample1 = set("understand") #用字符串初始化set
print(sample1)

sample2 = set(mylist) #用list初始化set
sample2.add(9)
print(sample2)

sample3 = frozenset(mylist)
print(sample3)
#操作符
print(6 in sample1) #判断6是否在集合中
print(sample2>=sample3) #判断子集关系
print(sample2-sample3) #差运算
print(sample2&sample3) #交运算
sample3 |= sample2 #对frozenset执行 |= 重新复制
print(sample3)

#内置函数 add update remove

# 4.Dictionary 类型
dict1 = {'Langage':'English','Title':'Python book','Page':450}
print(dict1['Title'])
dict1['Date'] = '2002-10-30' #增加新的key-value
print(dict1['Date'])
dict1['Langage'] = 'Chinese' #根据key跟新value
print(dict1)
#内置函数copy(拷贝副本)、clear(清楚字典中的键值对)
dict1.fromkeys(mylist)
print(dict1)

