#塔罗汉

def hanoi(n,x,y,z):
    if n ==1:
        print(x ,'-->',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'-->',z)
        hanoi(n-1,y,x,z)

n = int(input("请输入汉诺塔的层数:"))
hanoi(n,'X',"Y","Z")



dict1 = {"李宁":"一切皆有可能","耐克":"just do it ","Adidas":"Impossible is nothing"}



empty = {}
type(empty)

# dict  == > 创建字典
dict1 = dict((('F',70),('i',105),('s',115),('h',104),('C',67)))

# fromkeys() ==>创建字典

dict1 = {}
dict1.fromkeys((1,2,3))


dict2 = {}
dict2.fromkeys((1,2,3),"Number")

dict3 = {}
dict3.fromkeys((1,2,3),('one','two','three'))


# keys() values() items()

dict1 = {}

dict1 = dict1.fromkeys(range(32),"赞 ")
# dict1.keys()
# dict1.values()

dict1.get(31)
dict1.get(32,"木有")

# 这种清除不了 会出bug
a = {"姓名":"小甲鱼"}
b = a

a = {}
a
b


# 使用clear（）清除
a = {"姓名":"小甲鱼"}
b = a

a.clear()



# copy() 复制

a = {1:"one",2:"two",3:"three"}
b = a.copy()

id(a)

# pop() 弹出对应的值 popitem（） 弹出一个项
a = {1:"one",2:"two",3:"three",4:"four"}
# a.pop(2)
a.popitem()

#setdefault()与 get()  不同的是 他没有的话会自动添加一个
a = {1:'one',2:"two",3:"three",4:"four"}

a.setdefault(3)


a.setdefault(5) #>>自动添加了这个


#修改 更新  update（）


a = {"米奇":"老鼠","汤姆":"猫","小白":"猪"}
a.update(小白 = "狗")


# 手机参数 将参数打包成字典


def test(**params):
    print("有%d 个参数" % len(params))
    print("他们分别是： ",params)

test(a=1,b=2,c=3)
'''
有3 个参数
他们分别是：  {'a': 1, 'b': 2, 'c': 3}
'''