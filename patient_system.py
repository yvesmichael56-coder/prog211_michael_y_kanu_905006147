class Patient:
    def __init__(self, patient_id, name, age, symp4tom):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.symptom = symptom

    # Instance Method to display info
    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Symptom: {self.symptom}")

    # Instance Method to update the symptom
    def update_symptom(self, new_symptom):
        self.symptom = new_symptom
        print("Success: Record updated.")


# Task 1: Second Class (The System)
class HospitalSystem:
    def __init__(self):
        # Task 2: Data Structure (List)
        self.patients = []

    # Function to add records
    def add_patient(self):
        new_id = "P" + str(len(self.patients) + 1)
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        symptom = input("Enter patient symptom: ")

        new_patient = Patient(new_id, name, age, symptom)
        self.patients.append(new_patient)
        print("Success: Patient added to the system.")

    # Function to view ALL records
    def view_all_patients(self):
        print("\n--- All Patient Records ---")
        if len(self.patients) == 0:
            print("No records found.")
        else:
            for p in self.patients:
                p.display_info()

    # Function to SEARCH and view a specific record
    def search_patient(self):
        search_id = input("Enter the Patient ID to search (e.g., P1): ")
        found = False
        for p in self.patients:
            if p.patient_id == search_id:
                print("\n--- Patient Found ---")
                p.display_info()
                found = True
                break  # Stop searching once found
        if found == False:
            print("Error: Patient ID not found.")

    # Function to UPDATE a record
    def update_record(self):
        search_id = input("Enter the Patient ID to update: ")
        found = False
        for p in self.patients:
            if p.patient_id == search_id:
                print("Current symptom:", p.symptom)
                new_symp = input("Enter the new symptom: ")
                p.update_symptom(new_symp)  # Calling the instance method
                found = True
                break
        if found == False:
            print("Error: Patient ID not found.")

    # Task 3: Class Method
    @classmethod
    def system_rules(cls):
        print("\n[SYSTEM NOTICE]: Data is kept private according to DPG standards.")


# --- MAIN PROGRAM (The Menu) ---

clinic = HospitalSystem()
print("Welcome to the Clinic Patient Record System")

# While loop to keep the menu running
while True:
    print("\n--- MAIN MENU ---")
    print("1. Add a New Patient")
    print("2. View All Patients")
    print("3. View a Specific Patient Record")
    print("4. Update a Patient's Record")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        clinic.add_patient()
    elif choice == "2":
        clinic.view_all_patients()
    elif choice == "3":
        clinic.search_patient()
    elif choice == "4":
        clinic.update_record()
    elif choice == "5":
        print("Exiting system. Have a nice day!")
        clinic.system_rules()  # Call class method
        break  # Stops the loop
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
