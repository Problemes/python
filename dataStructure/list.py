# author: HR
# date: 2018/1/9
# 可变序列

listTest1 = ['hello', 'world']
print(listTest1)
print(type(listTest1))

listTest2 = [1, 2, 3]
print(listTest2)

listTest3 = list("12343")  # 只能有一个参数
print(listTest3)

listTest3.append("hello")  # 只有一个参数，返回值为none
print("append 后的list", listTest3)

print("list参数个数：", len(listTest3))
print("list第一个参数：", listTest3[0])

# list遍历
for arg in listTest3:
    print("list:", arg)

listTest3[4] = 5  # 更新list 赋予它int的类型的值

for index, arg in enumerate(listTest3, start=0):
    print("index:", index, "---object:", arg, type(arg))

# list截取
print("截取listTest3:", listTest3[2:])  # 返回从第三个开始往后的所有元素list集合
print("截取listTest3:", listTest3[2:5])

# list函数
List = ["arg0", "arg1", "arg2", "arg3"]
print(List.count("arg2"))  # 统计obj出现次数

List.append('arg4')
List.append("arg5")
print(List)  # 添加到队尾

List.extend(["fuck1", "fuck2"])
print(List)  # append做不到的列表拓展，直接把另一个列表拓展到此列表中

print(List.index("fuck1"))  # 返回fuck1第一次出现的位置

List.insert(8, "fuck3")
print(List)  # list插入

print(List.pop(8))  # 删除并返回删除的元素，参数为下标
print(List)

print(List.remove("fuck1"))  # 删除某一个匹配的值
print(List)

List.reverse()  # list翻转
print(List)

List.sort()  # list排序
print(List)
