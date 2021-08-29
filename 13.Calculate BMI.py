import math
def bmi(weight,height):
   BMI=(weight)/(pow(height,2))
   return BMI;

weight=float(input("Enter weight"))
height=float(input("Enter height"))

result=bmi(weight,height)
print(result)

