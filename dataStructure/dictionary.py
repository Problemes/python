# author: HR
# date: 2018/1/24

# 字典定义
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print("dictionary定义：", dict)

# 访问字典内的值
print("Alice:", dict['Alice'])

# 字典的删除操作
del dict['Alice']  # delete dict的一个条目
print(dict)
dict.clear()  # 清空dict所有条目
print(dict)
del dict  # 删除整个dict
print(dict)

# 字典内置的函数和方法
dict1 = {"A": 'a', "B": 'b', "C": 'c'}
dict2 = {"1": 1, "2": 2, "3": 3}
print(dict1)
print(dict2)

print("calculate dictionary length:", len(dict2))
print("toString", str(dict2))
print("Type of param:", type(dict2))
print("return Dict copy:", dict1.copy())
print("创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值:", dict1.fromkeys(["X", "Y", "Z"], ["xy", "z"]))
# print("dict get:", dict1.get("A", default="啥也没有"))
print("dict get:", dict1.get("s"))
print("iterator:", dict1.items())
print("keys:", dict1.keys())
print("setDefault 如果没有就加新的:", dict1.setdefault("A", "s"))
print(dict1)
print("把dict2注入到dict1中：", dict1.update(dict2))
print(dict1)
print("字典所有的值：", dict1.values())
