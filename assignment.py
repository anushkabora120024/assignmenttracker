from assignment import (
    add_assignment,
    view_assignments,
    mark_completed,
    delete_assignment,
    search_assignment,
    pending_assignments
)

from utils import show_menu


while True:

    show_menu()

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
        print("\nThank you for using Assignment Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")