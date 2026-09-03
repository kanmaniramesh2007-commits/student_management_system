students = []


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def calculate_status(marks):
    return "PASS" if marks >= 50 else "FAIL"


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ").strip()
        roll_no = input("Enter roll number: ").strip()

        if not name or not roll_no:
            print("Name and roll number cannot be empty.")
            continue

        duplicate = False

        for student in students:
            if student["roll_no"] == roll_no:
                duplicate = True
                break

        if duplicate:
            print("Roll number already exists!")
            continue

        try:
            marks = float(input("Enter marks (0-100): "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue

        except ValueError:
            print("Please enter valid marks.")
            continue

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks,
            "grade": calculate_grade(marks),
            "status": calculate_status(marks)
        }

        students.append(student)

        print("Student added successfully!")


    # View Students
    elif choice == "2":
        print("\n----- STUDENT DETAILS -----")

        if not students:
            print("No students found.")

        else:
            total = 0

            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Marks:", student["marks"])
                print("Grade:", student["grade"])
                print("Status:", student["status"])
                print("---------------------------")

                total += student["marks"]

            average = total / len(students)

            print("Class Average:", round(average, 2))


    # Search Student
    elif choice == "3":
        roll_no = input("Enter roll number to search: ").strip()

        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                print("\n----- STUDENT FOUND -----")
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Marks:", student["marks"])
                print("Grade:", student["grade"])
                print("Status:", student["status"])

                found = True
                break

        if not found:
            print("Student not found.")


    # Update Student
    elif choice == "4":
        roll_no = input("Enter roll number to update: ").strip()

        found = False

        for student in students:
            if student["roll_no"] == roll_no:

                new_name = input("Enter new name: ").strip()

                if not new_name:
                    print("Name cannot be empty.")
                    found = True
                    break

                try:
                    new_marks = float(input("Enter new marks (0-100): "))

                    if new_marks < 0 or new_marks > 100:
                        print("Marks must be between 0 and 100.")
                        found = True
                        break

                except ValueError:
                    print("Please enter valid marks.")
                    found = True
                    break

                student["name"] = new_name
                student["marks"] = new_marks
                student["grade"] = calculate_grade(new_marks)
                student["status"] = calculate_status(new_marks)

                print("Student updated successfully!")

                found = True
                break

        if not found:
            print("Student not found.")


    # Delete Student
    elif choice == "5":
        roll_no = input("Enter roll number to delete: ").strip()

        found = False

        for student in students:
            if student["roll_no"] == roll_no:

                students.remove(student)

                print("Student deleted successfully!")

                found = True
                break

        if not found:
            print("Student not found.")


    # Exit
    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break


    # Invalid Choice
    else:
        print("Invalid choice! Please try again.")


