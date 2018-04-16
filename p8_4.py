# 读取 pickle（）

import pickle

pickle_file = open('e:\\my_list.pkl','rb')
my_list = pickle.load(pickle_file)
print(my_list)