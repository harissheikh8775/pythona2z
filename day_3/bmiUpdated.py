weight =int(input("Enter your weight : "))
height =float(input("Enter your height : "))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5 :
    print("underweight")
elif bmi>=18.5 and bmi<25:
    print("normal weight")
else:
    print("overweight")