from DrugDispensaryApp.exceptions.custom_exception import LoginError

USERS = {}

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (doctor/pharmacist): ")

    if username in USERS:
        raise LoginError("Username already exists")
    elif not username:
        raise LoginError("Username cannot be blank")
    elif not password:
        raise LoginError("Password cannot be blank")

    USERS[username] = {"password": password, "role": role}
    print("User registered successfully!")
    return role

def show_users():
    for username, info in USERS.items():
        print(f"{username}: {info}")




