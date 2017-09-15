first = 1
while first <= 9:
    sec = 1
    while sec <= first:
        print(sec, "*", first, "=", first * sec, end="\t")
        sec += 1
    print()
    first += 1
