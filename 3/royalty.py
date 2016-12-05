def calc_royality(price,sales,per):
    rate = per / 100
    ro = int(price * sales * rate)
    return ro

i = input("price?")
price = int(i)

i = input("sales?")
sales = int(i)

i = input("per?")
per = int(i)

v = calc_royality(price,sales,per)
print("royality is ", v ,"yen")
