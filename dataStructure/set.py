# author: HR
# date: 2018/2/9

set1 = set(["fuck", "duck"])
print(set1)

# set集合重复元素自动忽略
setOne = set([1, 2, 3, 3, 4])
setTwo = set([0, 1, 3, 5, 5])
print(setOne)
print(setTwo)

# set集合顺序是随意的
setStr = set(["jack", "lose", "rose"])
print(setStr)

# set集合运算：
print(setOne.union(setTwo))
print("==", setOne | setTwo)

print("交集：", setOne & setTwo)
setThree = (setOne & setTwo).copy()
print(setThree)

setOne.add(10)
print("After Add:", setOne)

setOne.remove(10)
print("After Remove:", setOne)

# print(setOne.add(setTwo)) 错误 TypeError: unhashable type: 'set' 由于集合本身的元素是不可变元素而集合是可变元素
setOne.add(frozenset(setTwo))
print(setOne)

