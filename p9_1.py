file_name = input("请输入要打开的文件名： ")
f = open(file_name)
print("文件内容是")

for ech_line in f:
    print(ech_line)