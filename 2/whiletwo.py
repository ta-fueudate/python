while True:
    user=input("Floor space?")
    if user == "" or user =="q":break
    space = int(user)
    m2 = space * 3.31
    s="{0} space is {1} Square meter".format(space,m2)
    print(s)
