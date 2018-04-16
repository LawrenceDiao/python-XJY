# pickle() 方法存储为二进制文件

import pickle

my_list = [123,'abc','小呆呆',['another list']]
pickle_file = open('e:\\my_list.pkl','wb')
pickle.dump(my_list,pickle_file)

#dump 保存
pickle_file.close()

