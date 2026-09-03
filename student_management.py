students = []

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
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = float(input("Enter marks: "))

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        if marks >= 50:
            status = "PASS"
        else:
            status = "FAIL"

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks,
            "grade": grade,
            "status": status
        }

        students.append(student)

        print("\nStudent added successfully!")

    # View Students
    elif choice == "2":
        print("\n----- STUDENT DETAILS -----")

        if len(students) == 0:
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
        roll_no = input("Enter roll number to search: ")

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
        roll_no = input("Enter roll number to update: ")

        found = False

        for student in students:

            if student["roll_no"] == roll_no:

                student["name"] = input("Enter new name: ")
                student["marks"] = float(input("Enter new marks: "))

                marks = student["marks"]

                if marks >= 90:
                    student["grade"] = "A+"
                elif marks >= 80:
                    student["grade"] = "A"
                elif marks >= 70:
                    student["grade"] = "B"
                elif marks >= 60:
                    student["grade"] = "C"
                elif marks >= 50:
                    student["grade"] = "D"
                else:
                    student["grade"] = "F"

                if marks >= 50:
                    student["status"] = "PASS"
                else:
                    student["status"] = "FAIL"

                print("Student updated successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        roll_no = input("Enter roll number to delete: ")

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

    else:
        print("Invalid choice! Please try again.")
