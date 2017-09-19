# author: HR
# date: 2017/9/16

salary = 5000
goods = ["apple", "banana", "orange", "watermelon", "lemon", "strawberry"]
price = [8000, 1000, 3000, 500, 2000, 6000]

left_money = 5000
cart = []

i = 0
print("Goods Map:")

while i < len(goods):

    print(i, ".", goods[i], ":", price[i])
    i += 1

while 1:
    print("请输入购买的商品编号：")
    index = input(">>> ")
    if index.isdigit():
        if price[int(index)] > left_money:
            print("余额不足！")
        elif price[int(index)] <= left_money:
            cart.append(goods[int(index)])
            print("您已经购买了:", cart[0])
            left_money = left_money - price[int(index)]
            print("您的余额为：", left_money)
    elif index == "quit":
        break
