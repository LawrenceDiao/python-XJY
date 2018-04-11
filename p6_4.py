def discount(price,rate):
    final_price = price * rate
    old_price = 50 # 这里试图改便全局变量的值
    print("在全局变中修改old_prince现在的值：", old_price)
    return final_price

old_price = float(input("请输入原价："))
rate = float(input('请输入折扣率'))
new_price = discount(old_price,rate)
print('全局变量 old_price 现在的值是',old_price)
print('打印后价格是：',new_price)



count = 5
def myFun():

    global  count
    count = 10
    print(count)

myFun()
# 10
count
#  5  global 后 变为10
# globe 将局部变量修改为全局变量




