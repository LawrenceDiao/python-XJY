"""
内部嵌套

def fun1():
    print()
    def fun2():
        print()
    fun2() >> 直接调用里面的 如果 调用fun1()就不会出 fun2
"""


# 闭包

def funX(x):
    def funY(y):
        return x * y
    return funY

i = funX(8)
i(5)
funX(8)(5)
'''>>>40'''


# 通过容器解决内部为局部变量的问题
def funX():
    x = [5]
    def funY():
        x[0] *= x[0]
        return  x[0]
    return funY
funX()()
""">>>25"""


# lambda 表达方式

def ds(x):
    return 2 * x +1

# 用 lambda 方式表示
lambda x : 2*x +1

#     ↑  原函数 参数  ：  返回值

#  filter() 函数过滤

temp = filter(None,[1,0,False,True])
list(temp)
[1,True]


'''利用filter 写一个奇数筛选器'''

def odd(x):
    return  x % 2

temp = filter(odd,range(10))
list(temp)

list(filter(lambda x : x % 2, range(10)))



#map ()映射

list(map(lambda x:x*2,range(10)))
#[0,2,4,6,8,10,12,14,16,18]


