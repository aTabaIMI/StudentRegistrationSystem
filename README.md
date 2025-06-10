# University Registration System

A mini-scale student registration system developed as an educational project for a university Advanced Programming course. This project demonstrates advanced object-oriented programming (OOP) concepts in Python—including inheritance, polymorphism, and abstraction—as well as practical features such as CSV persistence, logging, a simple console menu, and a basic full-stack web application using Flask. 
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Console Mode](#console-mode)
  - [Web Mode](#web-mode)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This project provides a toy registration system to help computer science students learn and practice real-world software development topics. The system allows the addition and deregistration of students, teachers, and employees. It supports data persistence using CSV and logs all registration activities. The project is designed with both a simple command-line interface and a basic Flask web application.

## Features

- **OOP Concepts:** Utilizes inheritance and abstraction through a common `Person` class for students, teachers, and employees.
- **CRUD Operations:** 
  - Add and deregister users (students, teachers, and employees).
  - Search and list registered entities.
- **Data Persistence:** Automatically saves and loads data using CSV files.
- **Logging:** Maintains a log (`registration.log`) of all registration activities.
- **Console Menu:** A user-friendly console interface to interact with the system.
- **Web Application:** 
  - A full-stack web interface built with Flask.
  - Every page includes a dynamically generated logo.
  - Basic routes for listing, adding, and deregistering users.
- **Professional Workflow:** The project is structured to mimic real-world projects, ideal for teaching version control and project management.

## Requirements

- **Python 3.6+**
- **Flask  (for Web Mode):** Install via `pip install flask`
- **Matplotlib (for dynamic logo generation in Web Mode):** Install via `pip install matplotlib`

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/UniversityRegistrationSystem.git
   cd UniversityRegistrationSystem
##usage
Console mode:

Run the project in console mode by executing:
python registration_system.py

Run the project in web mode by executing:
python registration_system.py web
 and then open your browser and navigate the local host: http://127.0.0.1:5000


##License:

None

##Acknowledgements
Students of Department of Computer Science, Faculty of Mathematical Sciences at University of Guilan





