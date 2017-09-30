# author: HR
# date: 2017/9/28

pcd = {
    "河北省": {"石家庄": ["一区", "二区"], "邯郸": ["汗一区", "汗二区"]},
    "江西省": {"大同": ["大一区", "大二区"], "抚州": ["州一区", "州二区"]}
}

# province = list(pcd.keys())
# print(list(province))

address = ''
while 1:
    print(list(pcd.keys()), "请选择:", end="")
    province = input()

    if province != "quit":
        address = province
        print(list(pcd.get(province).keys()), "请选择:", end="")
        city = input()

        address = "--".join([province, city])
        print(pcd.get(province).get(city), "请选择:", end="")

        district = input()

        while 1:
            if district in pcd.get(province).get(city):
                address = "--".join([province, city, district])
                break
            else:
                district = input("wrong input, please insert again:")
                print("district:", district)

        print("Address:", address)
        print("请重新选择：", end=" ")
    else:
        break
