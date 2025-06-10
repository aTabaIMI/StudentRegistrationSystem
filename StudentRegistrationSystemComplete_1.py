#!/usr/bin/env python3
"""
Mini-project of University Registration System:
  Demonstrates OOP concepts, CSV persistence, logging,
  a simple console-based menu,
  and a basic Flask web app (running on localhost).

Usage:
  • Console: python scriptname.py
  • Web:     python scriptname.py web
"""

import csv
import logging
import os
import sys
from abc import ABC, abstractmethod

# --- Set up logging (will write to registration.log file stored in the current directory) ---
logging.basicConfig(
    filename="registration.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ===============================
# Base and Derived Classes
# ===============================

class Person(ABC):
    def __init__(self, fname, lname, ID, DoB):
        self.fname = fname
        self.lname = lname
        self.ID = ID
        self.DoB = DoB

    @abstractmethod
    def __str__(self):
        pass

class Student(Person):
    def __init__(self, fname, lname, ID, DoB, major):
        super().__init__(fname, lname, ID, DoB)
        self.major = major

    def __str__(self):
        return f"Student [ID: {self.ID}] - {self.lname}, DoB: {self.DoB}, Major: {self.major}"

class Teacher(Person):
    def __init__(self, fname, lname, ID, DoB, subject):
        super().__init__(fname, lname, ID, DoB)
        self.subject = subject

    def __str__(self):
        return f"Teacher [ID: {self.ID}] - {self.lname}, DoB: {self.DoB}, Subject: {self.subject}"

class Employee(Person):
    def __init__(self, fname, lname, ID, DoB, section):
        super().__init__(fname, lname, ID, DoB)
        self.section = section

    def __str__(self):
        return f"Employee [ID: {self.ID}] - {self.lname}, DoB: {self.DoB}, Section: {self.section}"


# ===============================
# Main School Registration System Class
# ===============================
class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.employees = []
        # Load data from CSV (if exists)
        self.load_data()

    # ----- Adding Methods -----
    def add_student(self):
        print("\n--- Adding a Student ---")
        fname = input("Enter student first name: ").strip()
        lname = input("Enter student last name: ").strip()
        DoB = input("Enter student DoB (YYYY-MM-DD): ").strip()
        ID = input("Enter student ID: ").strip()
        major = input("Enter student major: ").strip()
        student = Student(fname, lname, ID, DoB, major)
        if any(s.ID == student.ID for s in self.students):
            print("The student is already registered.")
        else:
            self.students.append(student)
            print("Student registered successfully!")
            logging.info(f"Added student: {student}")
            self.save_data()

    def add_teacher(self):
        print("\n--- Adding a Teacher ---")
        fname = input("Enter teacher first name: ").strip()
        lname = input("Enter teacher last name: ").strip()
        DoB = input("Enter teacher DoB (YYYY-MM-DD): ").strip()
        ID = input("Enter teacher ID: ").strip()
        subject = input("Enter teacher subject: ").strip()
        teacher = Teacher(fname, lname, ID, DoB, subject)
        if any(t.ID == teacher.ID for t in self.teachers):
            print("The teacher is already registered.")
        else:
            self.teachers.append(teacher)
            print("Teacher registered successfully!")
            logging.info(f"Added teacher: {teacher}")
            self.save_data()

    def add_employee(self):
        print("\n--- Adding an Employee ---")
        fname = input("Enter employee first name: ").strip()
        lname = input("Enter employee last name: ").strip()
        DoB = input("Enter employee DoB (YYYY-MM-DD): ").strip()
        ID = input("Enter employee ID: ").strip()
        section = input("Enter employee section: ").strip()
        employee = Employee(fname, lname, ID, DoB, section)
        if any(e.ID == employee.ID for e in self.employees):
            print("The employee is already registered.")
        else:
            self.employees.append(employee)
            print("Employee registered successfully!")
            logging.info(f"Added employee: {employee}")
            self.save_data()

    # ----- Deregistration Methods -----
    def deregister_student(self):
        print("\n--- Deregister Student ---")
        ID = input("Enter student ID to remove: ").strip()
        for student in self.students:
            if student.ID == ID:
                self.students.remove(student)
                print(f"Student with ID {ID} deregistered.")
                logging.info(f"Removed student: {student}")
                self.save_data()
                return
        print("Student not found.")

    def deregister_teacher(self):
        print("\n--- Deregister Teacher ---")
        ID = input("Enter teacher ID to remove: ").strip()
        for teacher in self.teachers:
            if teacher.ID == ID:
                self.teachers.remove(teacher)
                print(f"Teacher with ID {ID} deregistered.")
                logging.info(f"Removed teacher: {teacher}")
                self.save_data()
                return
        print("Teacher not found.")

    def deregister_employee(self):
        print("\n--- Deregister Employee ---")
        ID = input("Enter employee ID to remove: ").strip()
        for employee in self.employees:
            if employee.ID == ID:
                self.employees.remove(employee)
                print(f"Employee with ID {ID} deregistered.")
                logging.info(f"Removed employee: {employee}")
                self.save_data()
                return
        print("Employee not found.")

    # ----- Search Methods -----
    def search_student(self):
        print("\n--- Search Student ---")
        print("1. Search by ID")
        print("2. Search by Last Name")
        print("3. Search by DoB")
        choice = input("Enter your choice: ").strip()
        found = False
        if choice == '1':
            search_id = input("Enter student ID: ").strip()
            for s in self.students:
                if s.ID == search_id:
                    print(s)
                    found = True
        elif choice == '2':
            keyword = input("Enter last name: ").strip().lower()
            for s in self.students:
                if s.lname.lower() == keyword:
                    print(s)
                    found = True
        elif choice == '3':
            dob = input("Enter DoB (YYYY-MM-DD): ").strip()
            for s in self.students:
                if s.DoB == dob:
                    print(s)
                    found = True
        else:
            print("Invalid choice.")
        if not found:
            print("No matching student found.")

    def search_teacher(self):
        print("\n--- Search Teacher ---")
        print("1. Search by ID")
        print("2. Search by Last Name")
        print("3. Search by DoB")
        choice = input("Enter your choice: ").strip()
        found = False
        if choice == '1':
            search_id = input("Enter teacher ID: ").strip()
            for t in self.teachers:
                if t.ID == search_id:
                    print(t)
                    found = True
        elif choice == '2':
            keyword = input("Enter last name: ").strip().lower()
            for t in self.teachers:
                if t.lname.lower() == keyword:
                    print(t)
                    found = True
        elif choice == '3':
            dob = input("Enter DoB (YYYY-MM-DD): ").strip()
            for t in self.teachers:
                if t.DoB == dob:
                    print(t)
                    found = True
        else:
            print("Invalid choice.")
        if not found:
            print("No matching teacher found.")

    def search_employee(self):
        print("\n--- Search Employee ---")
        print("1. Search by ID")
        print("2. Search by Last Name")
        print("3. Search by DoB")
        choice = input("Enter your choice: ").strip()
        found = False
        if choice == '1':
            search_id = input("Enter employee ID: ").strip()
            for e in self.employees:
                if e.ID == search_id:
                    print(e)
                    found = True
        elif choice == '2':
            keyword = input("Enter last name: ").strip().lower()
            for e in self.employees:
                if e.lname.lower() == keyword:
                    print(e)
                    found = True
        elif choice == '3':
            dob = input("Enter DoB (YYYY-MM-DD): ").strip()
            for e in self.employees:
                if e.DoB == dob:
                    print(e)
                    found = True
        else:
            print("Invalid choice.")
        if not found:
            print("No matching employee found.")

    def list_all(self):
        print("\n--- Students ---")
        for s in self.students:
            print(s)
        print("\n--- Teachers ---")
        for t in self.teachers:
            print(t)
        print("\n--- Employees ---")
        for e in self.employees:
            print(e)

    # ----- CSV Persistence Methods -----
    def save_data(self):
        self._save_csv("students.csv", self.students, ["fname", "lname", "ID", "DoB", "major"])
        self._save_csv("teachers.csv", self.teachers, ["fname", "lname", "ID", "DoB", "subject"])
        self._save_csv("employees.csv", self.employees, ["fname", "lname", "ID", "DoB", "section"])

    def _save_csv(self, filename, data_list, fieldnames):
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for obj in data_list:
                writer.writerow(obj.__dict__)

    def load_data(self):
        self.students = self._load_csv("students.csv", Student, ["fname", "lname", "ID", "DoB", "major"])
        self.teachers = self._load_csv("teachers.csv", Teacher, ["fname", "lname", "ID", "DoB", "subject"])
        self.employees = self._load_csv("employees.csv", Employee, ["fname", "lname", "ID", "DoB", "section"])

    def _load_csv(self, filename, cls, fieldnames):
        data_list = []
        if os.path.exists(filename):
            with open(filename, mode="r", newline="") as file:
                reader = csv.DictReader(file, fieldnames=fieldnames)
                next(reader)  # skip header
                for row in reader:
                    data_list.append(cls(**row))
        return data_list

    # ----- Console-Based Menu -----
    def user_menu(self):
        while True:
            print("\n=== University Registration System ===")
            print("1. Add Student")
            print("2. Add Teacher")
            print("3. Add Employee")
            print("4. Deregister Student")
            print("5. Deregister Teacher")
            print("6. Deregister Employee")
            print("7. Search Student")
            print("8. Search Teacher")
            print("9. Search Employee")
            print("10. List All Registrations")
            print("11. Save Data")
            print("12. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_teacher()
            elif choice == '3':
                self.add_employee()
            elif choice == '4':
                self.deregister_student()
            elif choice == '5':
                self.deregister_teacher()
            elif choice == '6':
                self.deregister_employee()
            elif choice == '7':
                self.search_student()
            elif choice == '8':
                self.search_teacher()
            elif choice == '9':
                self.search_employee()
            elif choice == '10':
                self.list_all()
            elif choice == '11':
                self.save_data()
                print("Data saved successfully.")
            elif choice == '12':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


# ===============================
# Console Run Function
# ===============================
def run_console():
    school = School()
    school.user_menu()


# ===============================
# Flask Web Application
# ===============================
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
web_school = School()  # Global instance for the web app

# A basic base template to be used by our routes
BASE_HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>University Registration System</title>
  </head>
  <body>
    <h1>University Registration System</h1>
    <nav>
      <a href="{{ url_for('home') }}">Home</a> |
      <a href="{{ url_for('list_people') }}">List Registrations</a> |
      <a href="{{ url_for('add_person') }}">Add Person</a> |
      <a href="{{ url_for('deregister_person') }}">Deregister</a>
    </nav>
    <hr>
    {% block content %}{% endblock %}
  </body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        "{% extends 'base.html' %}{% block content %}<p>Welcome to the University Registration System!</p>{% endblock %}",
        )

@app.route("/list")
def list_people():
    all_people = {
        "Students": web_school.students,
        "Teachers": web_school.teachers,
        "Employees": web_school.employees
    }
    content = "<h2>All Registrations</h2>"
    for category, people in all_people.items():
        content += f"<h3>{category}</h3><ul>"
        for person in people:
            content += f"<li>{person}</li>"
        content += "</ul>"
    return render_template_string(
        "{% extends 'base.html' %}{% block content %}" + content + "{% endblock %}"
    )

@app.route("/add", methods=["GET", "POST"])
def add_person():
    if request.method == "POST":
        type_ = request.form.get("type")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        DoB = request.form.get("DoB")
        ID = request.form.get("ID")
        extra = request.form.get("extra")
        if type_ == "student":
            web_school.students.append(Student(fname, lname, ID, DoB, extra))
            logging.info(f"Added student via web: {fname} {lname}")
        elif type_ == "teacher":
            web_school.teachers.append(Teacher(fname, lname, ID, DoB, extra))
            logging.info(f"Added teacher via web: {fname} {lname}")
        elif type_ == "employee":
            web_school.employees.append(Employee(fname, lname, ID, DoB, extra))
            logging.info(f"Added employee via web: {fname} {lname}")
        web_school.save_data()
        return redirect(url_for("list_people"))
    form_html = """
    {% extends 'base.html' %}
    {% block content %}
    <h2>Add Person</h2>
    <form method="post">
      Type:
      <select name="type">
         <option value="student">Student</option>
         <option value="teacher">Teacher</option>
         <option value="employee">Employee</option>
      </select><br>
      First Name: <input type="text" name="fname"><br>
      Last Name: <input type="text" name="lname"><br>
      DoB (YYYY-MM-DD): <input type="text" name="DoB"><br>
      ID: <input type="text" name="ID"><br>
      Extra (Major/Subject/Section): <input type="text" name="extra"><br>
      <input type="submit" value="Add">
    </form>
    {% endblock %}
    """
    return render_template_string(form_html)

@app.route("/deregister", methods=["GET", "POST"])
def deregister_person():
    if request.method == "POST":
        type_ = request.form.get("type")
        ID = request.form.get("ID")
        removed = False
        if type_ == "student":
            for s in web_school.students:
                if s.ID == ID:
                    web_school.students.remove(s)
                    removed = True
                    logging.info(f"Removed student via web: {s}")
                    break
        elif type_ == "teacher":
            for t in web_school.teachers:
                if t.ID == ID:
                    web_school.teachers.remove(t)
                    removed = True
                    logging.info(f"Removed teacher via web: {t}")
                    break
        elif type_ == "employee":
            for e in web_school.employees:
                if e.ID == ID:
                    web_school.employees.remove(e)
                    removed = True
                    logging.info(f"Removed employee via web: {e}")
                    break
        web_school.save_data()
        msg = "Removed successfully." if removed else "ID not found. No removal occurred."
        return render_template_string(
            "{% extends 'base.html' %}{% block content %}<p>" + msg +
            "</p><p><a href='{{ url_for('home') }}'>Home</a></p>{% endblock %}"
        )
    form_html = """
    {% extends 'base.html' %}
    {% block content %}
    <h2>Deregister Person</h2>
    <form method="post">
      Type:
      <select name="type">
         <option value="student">Student</option>
         <option value="teacher">Teacher</option>
         <option value="employee">Employee</option>
      </select><br>
      ID: <input type="text" name="ID"><br>
      <input type="submit" value="Remove">
    </form>
    {% endblock %}
    """
    return render_template_string(form_html)

# Write the base template to the "templates" folder so that our "extends" works.
if not os.path.exists("templates"):
    os.makedirs("templates", exist_ok=True)
with open("templates/base.html", "w", encoding="utf-8") as f:
    f.write(BASE_HTML)

# ===============================
# Main Runner
# ===============================
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'web':
        print("Starting Flask web server on http://127.0.0.1:5000 ...")
        app.run(debug=True)
    else:
        run_console()
