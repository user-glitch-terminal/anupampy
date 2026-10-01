def add_students(name):
    with open("students.txt", "a") as file:
        file.write(name + "\n")
 
def view_students():
    with open("students.txt", "r") as file:
        content = file.read()
        print(content)
 
def delete_student(name_to_delete):
    name_with_newline = name_to_delete + "\n"
 
    with open("students.txt", "r") as file:
        lines = file.readlines()
 
    with open("students.txt", "w") as file:
        for line in lines:
            if line!= name_with_newline:
                file.write(line)
 
 
 
while True:
    print("\n1. Add a student.")
    print("\n2. View students.")
    print("\n3. Delete a student.")
    print("\n4. Exit")
 
    choice = input("\nEnter the choice: ")
 
    if choice == "1":
        name = input("\nEnter the name of the student: ")
        add_students(name)
 
    elif choice == "2":
        view_students()
 
    elif choice == "3":
        name_to_delete = input("Enter the name you want to delete")
        delete_student(name_to_delete)
 
    elif choice == "4":
        break
 
 
 
# Student Name Manager
 
'''
Add a student name to a file.
View all student names stored in the file.
'''
 
 
 
def add_students(name):
    with open("students.txt", "a") as file:
        file.write(name + "\n")
 
def view_students():
    with open("students.txt", "r") as file:
        content = file.read()
        print(content)
 
def delete_student(name_to_delete):
    name_with_newline = name_to_delete + "\n"
 
    with open("students.txt", "r") as file:
        lines = file.readlines()
 
    with open("students.txt", "w") as file:
        for line in lines:
            if line!= name_with_newline:
                file.write(line)
 
 
 
while True:
    print("\n1. Add a student.")
    print("\n2. View students.")
    print("\n3. Delete a student.")
    print("\n4. Exit")
 
    choice = input("\nEnter the choice: ")
 
    if choice == "1":
        name = input("\nEnter the name of the student: ")
        add_students(name)
 
    elif choice == "2":
        view_students()
 
    elif choice == "3":
        name_to_delete = input("Enter the name you want to delete")
        delete_student(name_to_delete)
 
    elif choice == "4":
        break
 