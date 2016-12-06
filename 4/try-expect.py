while True:
    try:
        weight = float(input("weight?"))
        height = float(input("height?"))
        height = height / 100
        bmi = weight / (height * height)
        break;
    except:
        print("input error please retry input")

result = ""
if bmi < 18.5: result="small"
elif bmi < 25: result ="average"
elif bmi < 30: result ="fat"
else: result ="heavy"

print("BMI :" ,bmi)
print("judge :", result)
