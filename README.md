# Student Assignment Tracker

## 1. Project Title

**Student Assignment Tracker Using Python**

## 2. Overview of the Project

The Student Assignment Tracker is a simple, menu-driven Python application designed to help students manage and keep track of their academic assignments. Students often have assignments from different subjects with different deadlines and priorities, making it difficult to keep track of all their pending work.

This project provides a simple solution by allowing users to add, view, search, complete, and delete assignments. Each assignment contains important information such as the assignment name, subject, deadline, priority, and completion status.

The project was developed as part of the **Python Essentials** course to apply basic Python programming concepts to a practical real-world problem.

## 3. Features

The project provides the following features:

* **Add Assignment:** Allows the user to enter the assignment name, subject, deadline, and priority.
* **View Assignments:** Displays all the assignments stored in the program.
* **Mark Assignment as Completed:** Changes the status of an assignment from Pending to Completed.
* **Delete Assignment:** Removes a selected assignment from the tracker.
* **Search Assignment:** Searches for an assignment using its name or subject.
* **View Pending Assignments:** Displays only assignments that have not yet been completed.
* **Exit:** Allows the user to safely exit the application.

## 4. Technologies/Tools Used

The following technologies and tools were used to develop this project:

* **Programming Language:** Python 3
* **Code Editor:** Visual Studio Code
* **Version Control:** Git and GitHub
* **Data Structures:** Lists and Dictionaries
* **Programming Concepts:** Functions, loops, conditional statements, string operations, user input, and exception handling.

No external Python libraries are required to run this project.

## 5. Steps to Install & Run the Project

### Step 1: Install Python

Download and install Python 3 on your computer.

### Step 2: Download the Project

Download this repository from GitHub or clone it using Git.

```bash
git clone https://github.com/your-username/student-assignment-tracker.git
```

### Step 3: Open the Project

Open the downloaded project folder in Visual Studio Code or another Python-supported code editor.

### Step 4: Run the Program

Open the terminal inside the project folder and run:

```bash
python assignment_tracker.py
```

The Assignment Tracker menu will appear in the terminal.

### Step 5: Use the Menu

Choose an option by entering its corresponding number and follow the instructions displayed by the program.

## 6. Instructions for Testing

The program can be tested by checking each available feature individually.

### Test 1: Add Assignment

Select option `1` and enter valid assignment details. The program should display:

```text
Assignment added successfully!
```

### Test 2: View Assignments

Select option `2`. The program should display all stored assignments with their name, subject, deadline, priority, and status.

### Test 3: Mark as Completed

Select option `3` and enter a valid assignment number. The status should change from **Pending** to **Completed**.

### Test 4: Delete Assignment

Select option `4` and enter a valid assignment number. The selected assignment should be removed.

### Test 5: Search Assignment

Select option `5` and enter an assignment name or subject. Matching assignments should be displayed.

### Test 6: View Pending Assignments

Select option `6`. Only assignments with **Pending** status should be displayed.

### Test 7: Invalid Input

Enter an invalid menu option or invalid assignment number. The program should display an appropriate error message without crashing.

