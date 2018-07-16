# check BMI
height = float(input("enter your height in inches:"))
H = height*0.0254 # height in metters
weight = float(input ("enter you weight in bounds:"))
W = weight*0.4536 # weight in kilograms

BMI = W/(H**2)
if BMI <18.5:
    print('Underweight')
elif BMI >= 18.55 and BMI <25:
    print('Normal')
elif BMI >=25 and BMI <30:
    print('Overweight')
elif BMI >=30:
    print('Obese')
