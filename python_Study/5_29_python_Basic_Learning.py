#  1.python基础语法
#     1.交互式编程
#     2.脚本式编程
#     3.标识符
#     4.保留字符(变量名)
#     5.行和缩进
#     6.多行语句(换行 \ )
#     7.引用（单双三）
#     8.注释
#     9.print('输出')
# 2.变量类型(variable types)
#     1.变量赋值
#       counter = 100 #整形
#       miles = 100.11 #浮点
#       name = "date" #字符串
# 3.标准数据类型
#     number(num ber)
#       int
#       flo at
#     string(str ing)
#     list(li st)
#     tuple(tu ple)
#     dictionary(dic tion ary)
#     boolend(bool end)
   
#     human = {
#       name = '啊秀'
#       man = ture
#       height = 175
#       hobby = ['sing','eat','']
#     }
# 4.Python元组(多种数据类型结合)
# 5.python算术运算符(+,-,*,/,%,**,//)
# 6.python比较运算符
# 7.python赋值运算符 -->

#  <-------------------------------------------------------------------------------------------------------------------------------------------------------->

# 创建类表包含

# 列表名 =  [字符串,整形,浮点,布尔,列表,元组,字典,集合]
#  list = [str,int,float,bool,list,tuple,dict,set]
# my_list = ['hello', 60, 16.4, True, False, ['docker', 'nginx'],
#            ("宝马", "共享单车"), {'age': 26, 'name': '啊秀'}, {27, 46}]


# # my_element(my_list)

# for i in my_list:
#     my_element(i)

# 循环遍历列表所有元素
#     如果
#     使用type()检查元素会得到一个值
#     值去匹配
#     否则

# for r in my_list:
#     # print(type(r))
#     if isinstance(r, str):
#         print(r, "这是str类型")
#     else:
#         print(r, "这不是一个str类型,而是：", type(r))
# for i in my_list:
#     if isinstance(i, dict):
#         print(i, "这是一个dict类型")
#     else:
#         print(i, "这个不是一个dict类型，而是一个：", type(i))

# print(type(my_list[1]))
# print(dir(my_list[1]))

# 使用print()系统函数输出所有列表对象的元素element
# for example
# print(list[1])
# print(my_list[7])

# 使用type()系统函数查看当前列表子元素的数据类型
# for example
# print(type(list[3]))
# print(type(my_list[8]))

# 使用dir()系统函数查看当前element对象的属性和方法
# print(type(my_list[0]))
# print(dir(my_list[0]))
# print(help([my_list[0]]))

# def my_element(x):
#  print(type(x))
# print(dir(x))
# print(help([x]))

# 使用help()系统函数查看当前element对象的帮助文档

# 自定义一个函数，该函数的功能就是封装 dir()

# 自定义循环，迭代出入列表的element并调阅自定义函数去输出对象的细节

# 练习判断语句

# 定义一个类模


# 类
