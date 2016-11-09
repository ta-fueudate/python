print("i am rich trader","no'")
print('i can\'t do everythings')
print("i like \"yuri suzuki\"")

wea="""
today nice weather
tomorow nice weather
but day after tomorow rain
"""
print(wea)

strs="""\
today nice weather
tomorow nice weather
but day after tomorow rain\
"""

print(strs)

strtwo = wea + strs
print(strtwo)


temperature=12
name="yuri"
print(name + str(temperature))

per_inch=2.54
inch=24
cm=inch*per_inch
desc="{0}インチ={1}センチ".format(inch,cm)
print(desc)


print("I love {name}".format(name="yuri"))
fmt ="yuri {motion} me"
s=fmt.format(motion="Love")
print(s)
