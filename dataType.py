# author: HR
# date: 2017/9/15

'''
name = input("姓名：")
salary = input("薪水：")
job = input("职位：")

if salary.isdigit():
    salary = int(salary)
else:
    print("salary must be a number!")

msg = ''' '''
    ----------info of %s --------------
    Name:%s
    Salary:%d
    job:%s
    
    you are less than average salary : $ %s 
''' ''' % (name, name, salary, job, 30000 - int(salary))

print(msg) '''


''' ---------- info of list -------------- '''

a = ["xm", "xl", "xh", "xz", "xa", "xz"]
#增删改查 切片[]
## 查 a[%a: %b: %c]  %a:从a开始，取到b b为负值时候是指倒数第x个索引； 间隔c个，默认1 ，为负值时，表示从右往左取；
''' print("query: ", a[1:-1:1])

#增 append("xx") 默认插入最后一个，append(index,"xxx") 添加到指定的索引位置
print("before append", a)
a.append("xa")
print("after append", a)

print("before insert", a)
a.insert(2, "xz")
print("after insert", a)


#修改 a[index] = xxx ;  用切片：a[1:3]=["xxx","xxx"] 表示修改从1开始到下表3之前的所有元素被替换
print("before change", a)
a[2] = "xc"
print("after change", a)
a[0:2] = ["xa", "xz"]
print("after changeDouble", a)
print()

#删除
a.remove("xa") #删除第一个参数中的元素
print("after remove", a)
pop = a.pop(1)
print("pop", pop)
print("after pop", a)
del a[0]
print("after del", a)
del a
print("after del all", a)#报错，删除这个a变量的内存 '''


''' ---------- info of list method -------------- '''
print(a.count("xz")) #计算出现几次参数
x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y) # 组装
print(x)

index = a.index("xz") #找参数在列表中的索引,取第一个位置，想取后面的参数索引值，用切片造小列表
print(index)
second_index = a[index + 1:].index("xz")
print(second_index)

a.reverse() # 倒序
print("reverse: ", a)

from audioop import reverse

num = [2, 4, 6, 2, 7, 4, 8, 0]
num.sort(reverse=True)
print(num)
num.sort() #按照ASCII码顺序排
print(num)
if type(num) is list:
    print("is list")
else:
    print("is not list")

