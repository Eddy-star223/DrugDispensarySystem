from DrugDispensaryApp.services.login_service import register_user
from DrugDispensaryApp.services.doctor_services import create_prescription, view_prescriptions
from DrugDispensaryApp.services.pharmacist_service import verify_prescription, dispense_drugs, view_fulfilled
from DrugDispensaryApp.exceptions.custom_exception import (
    LoginError, PrescriptionNotFoundError, DispenseError, ValidationError
)

def doctor_menu(username):
    while True:
        print("\n--- Doctor Menu ---")
        print("1. Create Prescription\n2. View History\n3. Logout")
        choice = input("Choose: ")

        try:
            if choice == "1":
                name = input("Patient Name: ")
                diagnosis = input("Diagnosis: ")
                drugs = input("Drugs (comma-separated): ").split(",")
                code = create_prescription(username, name, diagnosis, drugs)
                print(f"Prescription Code: {code}")
            elif choice == "2":
                for p in view_prescriptions(username):
                    print(p)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")
        except ValidationError as ve:
            print(f"Validation Error: {ve}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

def pharmacist_menu(username):
    while True:
        print("\n--- Pharmacist Menu ---")
        print("1. Verify Prescription\n2. Dispense Drugs\n3. View Fulfilled\n4. Logout")
        choice = input("Choose: ")

        try:
            if choice == "1":
                code = input("Enter Code: ")
                p = verify_prescription(code)
                print(p)
            elif choice == "2":
                code = input("Enter Code: ")
                dispense_drugs(code)
                print("Dispensed")
            elif choice == "3":
                for p in view_fulfilled():
                    print(p)
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")
        except PrescriptionNotFoundError as pnfe:
            print(f"Not Found: {pnfe}")
        except DispenseError as de:
            print(f"Dispense Error: {de}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

def main():
    while True:
        print("\n=== Drug Dispensary System ===")
        print("1. Login\n2. Register\n3. Exit")
        choice = input("Choose: ")

        try:
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                role = input("Enter role (doctor/pharmacist): ")
                if role == "doctor":
                    doctor_menu(username)
                elif role == "pharmacist":
                    pharmacist_menu(username)
            elif choice == "2":
                register_user()
            elif choice == "3":
                print("Goodbye")
                break
            else:
                print("Invalid choice.")
        except LoginError as le:
            print(f"Login Error: {le}")
        except Exception as e:
            print(f" Unexpected Error: {e}")

if __name__ == "__main__":
    main()