weight=float(input("your body weight(in kg):")) 
height=float(input("your height(in m):"))
bmi = weight/height**2
if bmi > 30 :
    print("your BMI is:", bmi, "you are obese")
elif 18.5 <= bmi <= 30:
    print("your BMI is:", bmi, "you are normal")
else:
    print("your BMI is:", bmi, "you are too thin")