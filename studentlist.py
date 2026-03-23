
students = []

def add_student():
    try:
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        students.append({"id": id, "name": name, "age": age, "grade": grade})
        print("Student added!")

    except:
        print("Invalid input!")

def view_students():
    if not students:
        print("No students found.")
        return

    for s in students:
        print(s["id"], s["name"], s["age"], s["grade"])

def search_student():
    id = input("Enter ID to search: ")

    for s in students:
        if s["id"] == id:
            print(s)
            return

    print("Not found.")

def delete_student():
    id = input("Enter ID to delete: ")

    for s in students:
        if s["id"] == id:
            students.remove(s)
            print("Deleted.")
            return

    print("Not found.")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
