# CLI Attendance Manager – Statement

## Problem Statement

Students often find it difficult to monitor their attendance across multiple courses, especially when each subject has different class counts and specific attendance rules. Calculating percentages manually or keeping track using notes or spreadsheets is time–consuming and error-prone.  
There is a need for a simple tool that can:

- Record daily attendance,
- Track attendance percentage,
- Indicate debarment risk (below 75%),
- Show marks awarded based on attendance brackets (5–0 marks),
- Maintain all data locally without requiring internet or a GUI.

A command-line system provides a lightweight, fast, and distraction-free method for students to manage this information efficiently.

## Scope of the Project

The **CLI Attendance Manager** is a single-file Python application that allows students to:

- Add and remove courses
- Record attendance for each course on a given date
- Automatically calculate:
  - total classes,
  - presents and absents,
  - attendance percentage,
  - whether the student is debarred (<75%),
  - attendance-based marks (5/4/3/2/1/0)
- Store all class entries and course metadata in local CSV and JSON files

The project focuses on a terminal-driven experience and simple data storage using basic Python modules.  
It does *not* include:

- Online syncing or cloud backup
- Multi-user login
- Faculty-side attendance entry
- GUI or mobile application

The scope is intentionally kept focused on the core academic requirement of tracking attendance.

## Target Users

- **Primary Users:**  
  Students who want to track their attendance accurately for all their courses.

- **Secondary Users:**  
  - Student mentors or CRs maintaining attendance for classmates  
  - Anyone who follows a class/session schedule requiring attendance tracking

The tool is optimized for individual use and runs entirely on the user’s local machine.

## High-Level Features

The project provides the following major capabilities:

### **1. Course Management**
- Add new courses with default max attendance marks (5)
- Remove existing courses along with their recorded attendance
- List all current courses

### **2. Attendance Recording**
- Add attendance entry for any course
- Accepts date in `DDMM` format (defaults to today)
- Allows marking attendance as:
  - **P** – Present  
  - **A** – Absent  
- Updates existing records if the same date already exists

### **3. Analytics & Reporting**
- Computes for each course:
  - Total number of class sessions recorded
  - Total presents
  - Attendance percentage (accurate to 2 decimals)
  - Debarment status (<75%)
  - Marks awarded:
    - 95%+ → 5 marks  
    - 90–94% → 4 marks  
    - 85–89% → 3 marks  
    - 80–84% → 2 marks  
    - 75–79% → 1 mark  
    - <75% → 0 marks  

### **4. Data Storage (Local Persistence)**
- **courses.json** stores course metadata  
- **attendance.csv** stores attendance logs with fields:  
  `Course, Date, Status`
- Both are created automatically on first run

### **5. Command-line Based User Interface**
- Text-based menu with numeric shortcuts
- Commands include:
  - `add_course`
  - `remove_course`
  - `list`
  - `add_attendance`
  - `report`
  - `help`
  - `exit`

This design makes the project simple, modular, and fully operable through a terminal with no external libraries required.
