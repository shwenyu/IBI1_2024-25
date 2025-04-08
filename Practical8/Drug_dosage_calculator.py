def dos_calc(age, weight, strength):
    # Define a function to calculate the dosage volume based on age, weight, and strength
    if 0 < age < 18:
        # Check if the age is within the range of 0 to 18 (child)
        rec_dose = 15  # mg/kg
        # Set the recommended dose to 15 mg per kg
    else:
        return "You are not a child!"
        # Return an error message if the age is not within the child range

    if weight > 100 or weight < 10:  # kg
        # Check if the weight is outside the valid range of 10 to 100 kg
        return "Out of weight range!"
        # Return an error message if the weight is out of range

    rec_vol = rec_dose * weight / strength
    # Calculate the recommended volume based on dose, weight, and strength
    return rec_vol
    # Return the calculated recommended volume

try:
    # Start a try block to handle potential input errors
    age = int(input("What's your age: "))
    # Prompt the user to input their age and convert it to an integer
    weight = int(input("What's your weight: "))
    # Prompt the user to input their weight and convert it to an integer
    strength_mg = int(input("What's the mg of strength: "))
    # Prompt the user to input the strength in mg and convert it to an integer
    strength_ml = int(input("What's the ml of strength: "))
    # Prompt the user to input the strength in ml and convert it to an integer

    if strength_mg in [120, 250] and strength_ml == 5:
        # Check if the strength in mg is either 120 or 250 and the strength in ml is 5
        strength = strength_mg / strength_ml
        # Calculate the strength in mg/ml
        rec_vol = dos_calc(age, weight, strength)
        # Call the dos_calc function to calculate the recommended volume
        if isinstance(rec_vol, str):
            # Check if the returned value is a string (error message)
            print(rec_vol)  # Print error message from dos_calc
            # Print the error message
        else:
            print(f"The recommended volume is {rec_vol} ml")
            # Print the recommended volume in ml
    else:
        print("Wrong strength of dose!")
        # Print an error message if the strength values are invalid
except ValueError:
    # Handle cases where the input cannot be converted to an integer
    print("Invalid input! Please enter numeric values.")
    # Print an error message for invalid input