from DrugDispensaryApp.drug_dispensary_management_class import DrugDispensarySystem


def main():
    system = DrugDispensarySystem()


    system.register_user("doc1", "pass123", "doctor")
    system.register_user("pharm1", "meds456", "pharmacist")

    print("\n Welcome to Drug Dispensary System ")
    username = input("Username: ")
    password = input("Password: ")

    user = system.login_user(username, password)
    if not user:
        return

    if user.role == "doctor":
        while True:
            print("\n️ Doctor Menu")
            print("1. Create Prescription")
            print("2. View Prescription History")
            print("3. Logout")
            choice = input("Choose: ")

            if choice == "1":
                patient = input("Patient Name: ")
                diagnosis = input("Diagnosis: ")
                drugs = input("Drugs (comma-separated): ").split(",")
                prescription = user.create_prescription(patient, diagnosis, drugs)
                system.prescriptions.append(prescription)
                print(f" Prescription created with code: {prescription.code}")
            elif choice == "2":
                for p in user.view_prescription_history():
                    print(p)
            elif choice == "3":
                break

    elif user.role == "pharmacist":
        while True:
            print("\n Pharmacist Menu")
            print("1. Verify Prescription")
            print("2. View Fulfilled Prescriptions")
            print("3. Logout")
            choice = input("Choose: ")

            if choice == "1":
                code = input("Enter Prescription Code: ")
                prescription = user.verify_prescription(code, system.prescriptions)
                if prescription:
                    print(prescription)
                    confirm = input("Dispense drugs? (yes/no): ")
                    if confirm.lower() == "yes":
                        user.dispense_drugs(prescription)
                        print(" Drugs dispensed.")
                else:
                    print(" Prescription not found.")
            elif choice == "2":
                for p in user.view_fulfilled_history():
                    print(p)
            elif choice == "3":
                break

if __name__ == "__main__":
    main()
