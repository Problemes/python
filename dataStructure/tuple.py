# author: HR
# date: 2018/1/9
# 不可被修改的序列,类似于list结构

# 元组初始化 结论：直接用逗号分隔开一些值则自动会组建成元组；可要括号也可不要；如果声明一个元组只有一个值，则必须加上逗号；
Tuple = 1, 2, 3
Tuple1 = "string", "string2"
Tuple2 = (1, 2, 3, 4)
Tuple3 = ()
Tuple4 = (1,)
print(Tuple, Tuple1, Tuple2, Tuple3, Tuple4)
print(type(Tuple), type(Tuple1), type(Tuple2), type(Tuple3), type(Tuple4))

# 元组转换初始化
t1 = tuple([1, 2, 3])
t2 = tuple("string")
print(t1, t2)

# 元组访问
print(t2[1])
print(t2[0:3])

# 元组修改 但是元组是不允许修改的，但是 可以拼接
print(("a", "b", "c") + ("x", "y", "z"))

# 删除元组 元组中的元素是不允许修改删除的，但是可以删除整个元组
tx = (1, 2, 3)
print(tx)
del tx  # print(tx) 删除了整个定义

# 元组运算符
print("元组参数个数：", len(Tuple))
print("元组连接：", (1, 2, 3) + (4, 5, 6))
print("元组复制：", ("tuple",) * 3)
print("元组判断：", 3 in Tuple)

# 元组索引和截取
txIndex = ("s1", "s2", "s3")
print(txIndex[2])
print(txIndex[1:])
print(txIndex[-1:])

# 元组内置函数
print(max(Tuple))  # 求元组内最大值
print(min(Tuple2))  # 求元组内最小值
listDemo = [1, 2, 3]
print("list:", listDemo)
print("被强转成tuple的list：", tuple(listDemo))
