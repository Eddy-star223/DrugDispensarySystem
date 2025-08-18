from DrugDispensaryApp.users_class import Doctor, Pharmacist


class DrugDispensarySystem:
    def __init__(self):
        self.users = {}
        self.prescriptions = []

    def register_user(self, username, password, role):
        if username in self.users:
            print(" Username already exists.")
        else:
            if role == "doctor":
                self.users[username] = Doctor(username, password)
            elif role == "pharmacist":
                self.users[username] = Pharmacist(username, password)
            print(f" {role.capitalize()} registered successfully!")

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password):
            print(f" Welcome, {username} ({user.role})!")
            return user
        else:
            print("Invalid login.")
            return None

