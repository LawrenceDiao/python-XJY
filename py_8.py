'''
打开文件
open(file,mode = 'r',buffering = -1,encoding = None,errors = None,newline = None,closed = True,
opener = None)
关闭文件
close()
encoding='UTF-8'
'''

f = open('record.txt', encoding='UTF-8')

'''
read() readline() list() 

read() 文件按字节读取 不舍参数 直接到最后

tell（） 读取多少行
'''

f.read()
f.tell()

# 书签 seek（offset，from）
# from  0 表示启示位置 1表示当前位置 2 表示末尾 偏移offset个字节
# 设置为启示位置 就是seek(0,0)
f.seek(0,0)
'''
readline() 读取一整行 遇到\n结束
  
'''

