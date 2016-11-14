year=int(input("Anno Domini?"))

is_leap= False

if year % 4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap =True
else:
    is_leap=True

if is_leap:
    print("True")
else:
    print("False")
