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


