print("hello,boy!")

count = 0
beforePass = "123"

name = input("please input your name:")
while count < 3:
    password = input("please input your password:")
    if password != beforePass:
        count += 1
    else:
        print("success")
        break
else:
    print("failure")

print(name, password, count)
