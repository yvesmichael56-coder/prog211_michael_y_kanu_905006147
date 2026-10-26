# prog211_michael_y_kanu_905006147
Patient Record System
*Domain:* Health
*Student Name:* Michael Y. Kanu
*Student ID:* 905006147

## How the System Works
This Python program is a fully menu-driven Patient Record System. When you run it, it asks the user to choose an option from a menu, making it act like a real clinic receptionist's software.

### Main Features:
1. *Add a New Patient:* Prompts the user to type the patient's name, age, and symptom. It automatically generates a unique ID (P1, P2, etc.) and stores the record.
2. *View All Patients:* Loops through the system's list and prints the full record for every patient.
3. *View Specific Patient Record:* Asks for a Patient ID (like "P1"), searches the list, and displays only that one specific patient's details.
4. *Update Patient Record:* Asks for a Patient ID, finds the patient, and allows the user to change their symptom.
5. *Exit:* Closes the program and displays a class method warning about data privacy.

### OOP Structure:
*   **Patient Class:** Holds attributes (id, name, age, symptom) and has instance methods to display info and update the symptom.
*   **HospitalSystem Class:** Manages the list of patients (self.patients). It contains the functions for adding, searching, and updating. It also has a @classmethod for system rules.

## Digital Public Goods (DPG) Alignment
*   *Privacy-respecting:* The program is designed to be safe. It only asks for basic health info and a name. It does not ask for sensitive personal data like home addresses or phone numbers.
*   *Open-source:* The code is uploaded to GitHub.
*   *Inclusive:* Uses simple text menus.
*   *Modular:* The Patient and HospitalSystem classes are separate, making the code clean and reusable.
