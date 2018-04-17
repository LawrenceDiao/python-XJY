class Turtle:
    color =  'green'
    weight = 10
    legs =4
    shell = True
    mouth = '大嘴'

    def climb(self):
        print("正在爬行")
    def run(self):
        print('正在跑')
    def bite(self):
        print('咬死你')
    def eat(self):
        print('吃豆豆')
    def sleep(self):
        print("睡觉哦")


t = Turtle()

t.sleep()