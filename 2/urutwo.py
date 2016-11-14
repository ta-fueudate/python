year=int(input("Anno Domini?"))

is_leap = (year % 400 == 0)or((year % 100 !=0) and (year % 4==0))

if is_leap:
    print("uru")
else:
    print("no uru")
