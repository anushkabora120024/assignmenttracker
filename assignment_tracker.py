# Student Assignment Tracker
assignments = []
def add_assignment():
    print("\n--- Add Assignment ---")
    name = input("Enter assignment name: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline (DD-MM-YYYY): ")
    priority = input("Enter priority (High/Medium/Low): ")

    new_assignment = {"name": name,
                      "subject": subject,
                      "deadline": deadline,
                      "priority": priority,
                      "status": "Pending"}

    assignments.append(new_assignment)
    print("Assignment added ")


def view_assignments():
    print("\n--- All Assignments ---")

    if not assignments:
        print("No assignments found.")
        return

    for i in range(len(assignments)):
        a = assignments[i]

        print("\nAssignment", i + 1)
        print("Name:", a["name"])
        print("Subject:", a["subject"])
        print("Deadline:", a["deadline"])
        print("Priority:", a["priority"])
        print("Status:", a["status"])


def mark_completed():
    print("\n--- Mark Assignment as Completed ---")

    if not assignments:
        print("No assignments available.")
        return

    view_assignments()
    try:
        num = int(input("\nEnter assignment number: "))

        if num >= 1 and num <= len(assignments):
            assignments[num - 1]["status"] = "Completed"
            print("Assignment marked as completed.")
        else:
            print("Invalid assignment number.")

    except ValueError:
        print("Please enter a number.")


def delete_assignment():
    print("\n--- Delete Assignment ---")

    if not assignments:
        print("No assignments available.")
        return

    view_assignments()
    try:
        num = int(input("\nEnter assignment number to delete: "))

        if num >= 1 and num <= len(assignments):
            removed = assignments.pop(num - 1)
            print(removed["name"], "deleted successfully.")
        else:
            print("Invalid assignment number.")

    except ValueError:
        print("Please enter a number.")


def search_assignment():
    print("\n--- Search Assignment ---")

    if not assignments:
        print("No assignments available.")
        return

    keyword = input("Enter assignment name or subject: ").lower()
    found = False

    for i in range(len(assignments)):
        a = assignments[i]

        if keyword in a["name"].lower() or keyword in a["subject"].lower():
            print("\nAssignment", i + 1)
            print("Name     :", a["name"])
            print("Subject  :", a["subject"])
            print("Deadline :", a["deadline"])
            print("Priority :", a["priority"])
            print("Status   :", a["status"])

            found = True

    if found == False:
        print("No matching assignment found.")


def pending_assignments():
    print("\n--- Pending Assignments ---")

    found = False

    for i in range(len(assignments)):
        a = assignments[i]

        if a["status"] == "Pending":
            print("\nAssignment", i + 1)
            print("Name:", a["name"])
            print("Subject:", a["subject"])
            print("Deadline:", a["deadline"])
            print("Priority:", a["priority"])

            found = True

    if found == False:
        print("No pending assignments.")
# program menu
while True:
    print("\n================================")
    print("     STUDENT ASSIGNMENT TRACKER")
    print("================================")

    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Mark Assignment as Completed")
    print("4. Delete Assignment")
    print("5. Search Assignment")
    print("6. View Pending Assignments")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_assignment()

    elif choice == "2":
        view_assignments()

    elif choice == "3":
        mark_completed()

    elif choice == "4":
        delete_assignment()

    elif choice == "5":
        search_assignment()

    elif choice == "6":
        pending_assignments()

    elif choice == "7":
        print("\nThank you for using Assignment Tracker")
        break

    else:
        print("Invalid choice. Please try again.")
