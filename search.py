# Search and pending assignment functions


def search_assignment(assignments):
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

    if not found:
        print("No matching assignment found.")


def pending_assignments(assignments):
    print("\n--- Pending Assignments ---")

    found = False

    for i in range(len(assignments)):
        a = assignments[i]

        if a["status"] == "Pending":
            print("\nAssignment", i + 1)
            print("Name     :", a["name"])
            print("Subject  :", a["subject"])
            print("Deadline :", a["deadline"])
            print("Priority :", a["priority"])

            found = True

    if not found:
        print("No pending assignments.")