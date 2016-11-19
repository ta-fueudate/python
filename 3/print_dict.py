fruits={
    "banana":300,
    "abogad":200,
    "apple":120,
    "orange":98
}

for name in fruits.keys():
    price=fruits[name]
    s="{0} is {1}yen".format(name,price)
    print(s)
