from domain.entities import User

def run_interface(usecase):
    while True:
        print("1. Add\n2. Browse\n3. Read\n4. Edit\n5. Delete\n0. Exit")
        choice = input("Choose: ")
        if choice == "1":
            uid = int(input("ID: "))
            name = input("Name: ")
            email = input("Email: ")
            usecase.create_user(User(uid, name, email))
        elif choice == "2":
            for u in usecase.browse_users():
                print(f"{u.user_id} - {u.name} - {u.email}")
        elif choice == "3":
            uid = int(input("ID: "))
            u = usecase.read_user(uid)
            print(f"{u.user_id} - {u.name} - {u.email}" if u else "Not found")
        elif choice == "4":
            uid = int(input("ID: "))
            name = input("New name: ")
            email = input("New email: ")
            print("Updated" if usecase.edit_user(uid, name, email) else "Failed")
        elif choice == "5":
            uid = int(input("ID: "))
            print("Deleted" if usecase.delete_user(uid) else "Not found")
        elif choice == "0":
            break
