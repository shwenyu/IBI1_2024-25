weight=float(input("your body weight(in kg):")) 
height=float(input("your height(in m):"))
bmi = weight/height**2
if bmi > 30 :
    print("your BMI is:", bmi, "you are obese")
elif 18.5 <= bmi <= 30:
    print("your BMI is:", bmi, "you are normal")
else:
    print("your BMI is:", bmi, "you are too thin")
    
#pseudocode:
#BEGIN
#    PROMPT user to input their body weight (in kg) and STORE it in variable weight
#    PROMPT user to input their height (in m) and STORE it in variable height
#
#    CALCULATE bmi as weight divided by the square of height
#
#   IF bmi is greater than 30 THEN
#        PRINT "your BMI is:" followed by the value of bmi and "you are obese"
#    ELSE IF bmi is between 18.5 and 30 (inclusive) THEN
#        PRINT "your BMI is:" followed by the value of bmi and "you are normal"
#    ELSE
#        PRINT "your BMI is:" followed by the value of bmi and "you are too thin"
#    END IF
#END