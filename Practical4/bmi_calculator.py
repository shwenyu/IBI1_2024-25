weight = float(input("your body weight(in kg):"))  # PROMPT user to input their body weight (in kg) and STORE it in variable weight
height = float(input("your height(in m):"))  # PROMPT user to input their height (in m) and STORE it in variable height
bmi = weight / height**2  # CALCULATE bmi as weight divided by the square of height
if bmi > 30:  # IF bmi is greater than 30 THEN
    print("your BMI is:", bmi, "you are obese")  # PRINT "your BMI is:" followed by the value of bmi and "you are obese"
elif 18.5 <= bmi <= 30:  # ELSE IF bmi is between 18.5 and 30 (inclusive) THEN
    print("your BMI is:", bmi, "you are normal")  # PRINT "your BMI is:" followed by the value of bmi and "you are normal"
else:  # ELSE
    print("your BMI is:", bmi, "you are too thin")  # PRINT "your BMI is:" followed by the value of bmi and "you are too thin"
    
