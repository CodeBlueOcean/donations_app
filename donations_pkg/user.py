def login(database, username, password):
    if username in database and database[username] == password:
        print("\nWelcome back", username + "!\n")
        return username
    if username in database and database[username] != password:
        print("\nIncorrect password for", username + ".\n")
        return ""
    else:
        print("\nUser not found. Please register.\n")
        return ""


def register(database, username):
    if username in database:
        print()
        print("Username already registered")
        return ""
    else:
        print()
        print("Username", username + " registered")
        return username
