'''
创建集合
1：用大括号括起来
2：使用 set（）

set() 唯一 就是重复的会自动删除**

'''

set1 = {1,2,3,4,5,6}
set2 = set([1,2,3,4,5,6,])


# 去除重复元素

# 方法一

list1 = [1,2,3,4,5,5,3,1,0]
temp = list1[:]

list1.clear()
for each in temp:
    if each not in list1:
        list1.append(each)


# 方法2

list1 = [1,2,3,4,5,5,3,1,0]
list1 = list(set(list1))


# 访问 循环出来

set1 = {1,2,3,4,5,6,7,8,9}

for each in set1:
    print(each,end=",")

# 1,2,3,4,5,6,7,8,9,

# 冰冻集合 frozen（）
set1 = frozenset({1,2,3,4,5})
set1.add(6)


