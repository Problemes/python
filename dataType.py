# author: HR
# date: 2017/9/15

name = input("姓名：")
salary = input("薪水：")
job = input("职位：")

if salary.isdigit():
    salary = int(salary)
else:
    print("salary must be a number!")

msg = '''
    ----------info of %s --------------
    Name:%s
    Salary:%d
    job:%s
    
    you are less than average salary : $ %s 
''' % (name, name, salary, job, 10000 - int(salary))

print(msg)
