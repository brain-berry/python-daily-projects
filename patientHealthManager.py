from datetime import datetime

# ──────────────────────────────────────────────
#  PATIENT DATA STORE
# ──────────────────────────────────────────────
patients = []


# ──────────────────────────────────────────────
#  INPUT / DATA COLLECTION
# ──────────────────────────────────────────────
def get_valid_input(prompt, cast_type, validation_fn=None, error_msg="Invalid input."):
    """Generic input helper with type casting and optional validation."""
    while True:
        try:
            value = cast_type(input(prompt))
            if validation_fn and not validation_fn(value):
                print(error_msg)
                continue
            return value
        except ValueError:
            print(error_msg)


def collect_patient_data():
    """Prompt the user for patient details and return a patient dictionary."""
    print("\n--- Enter Patient Details ---")

    first_name = input("  First name: ").strip()
    while not first_name.isalpha():
        print("  Name must contain only letters.")
        first_name = input("  First name: ").strip()

    last_name = input("  Last name: ").strip()
    while not last_name.isalpha():
        print("  Name must contain only letters.")
        last_name = input("  Last name: ").strip()

    current_year = datetime.now().year

    year_of_birth = get_valid_input(
        "  Year of birth: ",
        int,
        lambda y: 1900 <= y <= current_year,
        f"  Enter a valid year (1900–{current_year})."
    )

    weight = get_valid_input(
        "  Weight (kg): ",
        float,
        lambda w: w > 0,
        "  Weight must be a positive number."
    )

    height = get_valid_input(
        "  Height (m): ",
        float,
        lambda h: 0.3 <= h <= 2.8,
        "  Enter a realistic height in meters (0.3–2.8)."
    )

    cholesterol_level = get_valid_input(
        "  Cholesterol level (mg/dL): ",
        int,
        lambda c: c > 0,
        "  Cholesterol must be a positive number."
    )

    age = current_year - year_of_birth

    return {
        "first_name":       first_name.title(),
        "last_name":        last_name.title(),
        "year_of_birth":    year_of_birth,
        "age":              age,
        "weight":           weight,
        "height":           height,
        "cholesterol_level": cholesterol_level,
    }


# ──────────────────────────────────────────────
#  HEALTH ANALYSIS FUNCTIONS
# ──────────────────────────────────────────────
def categorize_age(age):
    """Return age‑group label."""
    if age < 13:
        return "Child"
    if age < 18:
        return "Adolescent"
    if age < 65:
        return "Adult"
    return "Senior"


def calculate_bmi(weight, height):
    """Return (numeric BMI, category string)."""
    bmi = round(weight / (height ** 2), 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


def categorize_cholesterol(level):
    """Return cholesterol risk category."""
    if level < 200:
        return "Normal"
    if level < 240:
        return "Borderline High"
    return "High"


# ──────────────────────────────────────────────
#  DISPLAY
# ──────────────────────────────────────────────
def display_health_summary(patient):
    """Print a formatted health summary for one patient."""
    age_cat              = categorize_age(patient["age"])
    bmi_value, bmi_cat   = calculate_bmi(patient["weight"], patient["height"])
    chol_cat             = categorize_cholesterol(patient["cholesterol_level"])

    print("┌──────────────────────────────────────────┐")
    print(f"  Patient : {patient['first_name']} {patient['last_name']}")
    print(f"  Age     : {patient['age']} ({age_cat})")
    print(f"  BMI     : {bmi_value} ({bmi_cat})")
    print(f"  Chol.   : {patient['cholesterol_level']} mg/dL ({chol_cat})")
    print("└──────────────────────────────────────────┘")


def display_all_patients():
    """Show summaries for every patient on file."""
    if not patients:
        print("\n  No patient records found.\n")
        return
    print(f"\n--- All Patients ({len(patients)}) ---")
    for patient in patients:
        display_health_summary(patient)


# ──────────────────────────────────────────────
#  SEARCH
# ──────────────────────────────────────────────
def search_patient():
    """Find and display patients matching a last‑name query."""
    if not patients:
        print("\n  No patient records to search.\n")
        return

    query   = input("  Enter last name to search: ").strip().lower()
    results = [p for p in patients if p["last_name"].lower() == query]

    if results:
        print(f"\n  Found {len(results)} match(es):")
        for patient in results:
            display_health_summary(patient)
    else:
        print("  No patient found with that last name.\n")


# ──────────────────────────────────────────────
#  MAIN MENU LOOP
# ──────────────────────────────────────────────
def main():
    print("\n╔══════════════════════════════════════════╗")
    print("║  Patient Health Profile Manager          ║")
    print("╚══════════════════════════════════════════╝")

    while True:
        print("\n  1. Add new patient")
        print("  2. View all patient summaries")
        print("  3. Search patient by last name")
        print("  4. Exit")

        choice = input("\n  Enter your choice (1-4): ").strip()

        if choice == "1":
            patient_data = collect_patient_data()
            patients.append(patient_data)
            print(f"\n  ✓ Patient '{patient_data['first_name']} "
                  f"{patient_data['last_name']}' added successfully!")
            display_health_summary(patient_data)

        elif choice == "2":
            display_all_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            print("\n  Goodbye!\n")
            break

        else:
            print("  Invalid choice — please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
