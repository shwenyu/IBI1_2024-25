class patients():
    # Define a class named 'patients' to represent patient information.
    def __init__(self, name, age, latest_admission, medical_history):
        # Initialize the patient object with name, age, latest admission date, and medical history.
        self.name = name  # Assign the patient's name to the 'name' attribute.
        self.age = age  # Assign the patient's age to the 'age' attribute.
        self.adm = latest_admission  # Assign the latest admission date to the 'adm' attribute.
        self.his = medical_history  # Assign the medical history to the 'his' attribute.
    
    def print_patient(self):
        # Define a method to print the patient's details.
        print(f"Name: {self.name} Age: {self.age} Lastest date of admission: {self.adm} Medical history: {self.his}")
        # Print the patient's name, age, latest admission date, and medical history.

name = input("What's the patient's name:")  # Prompt the user to input the patient's name.
age = input("What's the patient's age:")  # Prompt the user to input the patient's age.
last = input(" What's the lastest date for the patient to admit:")  # Prompt the user to input the latest admission date.
history = input("What's the patient's medical history:")  # Prompt the user to input the patient's medical history.
patient = patients(name, age, last, history)  # Create a new 'patients' object with the provided details.
patients.print_patient(patient)  # Call the 'print_patient' method to display the patient's details.