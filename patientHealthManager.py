#DATA COLLECTION
#Input Patient Details
#Prompt the user for the follwing inputs

first_name = input("Enter the patient's first name: ")
last_name = input("Enter the patient's last name: ")
year_of_birth = int(input("Enter the year of birth: "))
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))
cholesterol_level = int(input("Enter cholesterol level (mg/dL): "))

#CALCULATE AGE
#Use the current year to calculate the patients age

from datetime import datetime

current_year = datetime.now().year
age = current_year - year_of_birth

# DATA STORAGE
# Store data in a dictionary
# Store each patient's data in a dictionary

patient_data = {
    'first_name': first_name,
    'last_name': last_name,
    'year_of_birth': year_of_birth,
    'age': age,
    'weight': weight,
    'height': height,
    'cholesterol_level': cholesterol_level
}

# Append patient data to a list
# Maintain a collection of patient records by appending each dictionary to a list:

patients = []
patients.append(patient_data)

# HEALTH ANALYSIS FUNCTIONS
# Age Categorization
# Determine if the patient is a minor or an adult

def categorize_age(age):
    if age < 18:
        return 'Minor'
    else:
        return 'Adult'

# BMI calculation
#Calculate the BMI and categorize it:

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

# Cholesterol Level Analysis
# Categorize cholesterol levels

def categorize_cholesterol(cholesterol_level):
    if cholesterol_level < 200:
        return 'Normal'
    elif 200 <= cholesterol_level < 240:
        return 'Borderline High'
    else:
        return 'High'

# DISPLAY HEALTH SUMMARY
# Print the health summary
#Create a function to display the patient's health summary:

def display_health_summary(patient):
    age_category = categorize_age(patient['age'])
    bmi_category = calculate_bmi(patient['weight'], patient['height'])
    cholesterol_category = categorize_cholesterol(patient['cholesterol_level'])
    
    print(f"\nHealth Summary for {patient['first_name']} {patient['last_name']}")
    print(f"Age Category: {age_category}")
    print(f"BMI Category: {bmi_category}")
    print(f"Cholesterol Level: {cholesterol_category}\n")

# USER INTERACTION LOOP
# Main Menu
# Create a loop to interact with the user

while True:
    print("Patient Health Profile Manager & Analyzer")
    print("1. Add new patient")
    print("2. View patient health summary")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Collect data, store, and analyze
        # Use the above functions here
        # e.g., patients.append(patient_data)
        pass
    elif choice == '2':
        for patient in patients:
            display_health_summary(patient)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# Search for a patient by name
# Implement a search function to find a patient by their last name:

def search_patient(last_name, patients):
    for patient in patients:
        if patient['last_name'].lower() == last_name.lower():
            display_health_summary(patient)
            return
    print("Patient not found.")

 
