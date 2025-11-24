# CLI Attendance Manager

A simple and lightweight **command-line attendance tracking system** that allows students to add courses, record attendance, compute attendance percentage, check debarment status, and view marks awarded based on attendance brackets.  
All data is stored locally using CSV and JSON files—no database or internet connection required.

---

## Features

### Course Management
- Add new courses (default max marks = 5)
- Remove existing courses along with all attendance records
- List all courses with their metadata
<img width="425" height="448" alt="image" src="https://github.com/user-attachments/assets/9f356dae-04c2-487d-a7ac-97cb7cd67ae6" />


### Attendance Tracking
- Record attendance for any course for any date  
- Supports:
  - **P** → Present  
  - **A** → Absent  
- Automatically updates existing entry if same date is recorded again
- Dates follow format **DDMM** (defaults to today's date)
<img width="389" height="406" alt="image" src="https://github.com/user-attachments/assets/8dba93c6-0861-4c2d-885b-22f1e1e0aee8" />


### Reporting & Analytics
- Total classes recorded
- Total presents
- Attendance percentage (with 2 decimal precision)
- Debarment check (<75% attendance)
- Attendance-based mark calculation:
  - ≥ 95% → 5 marks  
  - ≥ 90% → 4 marks  
  - ≥ 85% → 3 marks  
  - ≥ 80% → 2 marks  
  - ≥ 75% → 1 mark  
  - < 75% → 0 marks (debarred)
<img width="311" height="193" alt="image" src="https://github.com/user-attachments/assets/ab6aff33-e2c7-453c-baff-de4290376c7f" />


### File-Based Storage
- `courses.json` → stores all course names + metadata  
- `attendance.csv` → stores all attendance rows  
- Files are auto-created on first run
<img width="212" height="100" alt="image" src="https://github.com/user-attachments/assets/78225d9b-de89-49fc-bc35-85dc16638f78" />


### CLI-Based Interface
Simple commands like:
- add_course
- remove_course
- list
- add_attendance
- report
- help
- exit

Supports numeric shortcuts (1–7) for convenience.
<img width="598" height="164" alt="image" src="https://github.com/user-attachments/assets/513be408-05ec-4281-882f-7db444a12542" />


---

## Technologies Used

- **Python 3** (Core language)
- **CSV module** (attendance storage)
- **JSON module** (course storage)
- **Datetime** (date validation)
- **OS module** (file handling)

No external libraries required.

---

## Project Structure

/attendance_manager
│
├── attendance.csv # Auto-created for attendance logs
├── courses.json # Auto-created for course data
└── attendance.py # Main Python script (your project file)

> Note: Your actual Python filename can be anything (e.g., `main.py` or `attendance.py`).

---

## How to Run the Project

### **1. Install Python**
Ensure Python 3.x is installed on your system.  
Check with:
python --version

### **2. Clone or Download the Repository**
git clone https://github.com/your-username/cli-attendance-manager.git
cd cli-attendance-manager

### **3. Run the Program**
python attendance.py

---

## How to Use (Examples)

### **Add a course**
add_course
Course name (unique): Math
Added course 'Math' with max marks 5.

### **Record attendance**
add_attendance
Select course:

Math
Date (DDMM) [default today]:
Status - present (p) or absent (a): p
Recorded attendance for Math -> P

### **View report**
report
Select course:

Math
Report for 'Math':

Sessions recorded: 5

Presents: 4

Attendance %: 80.0%

Debarred: NO

Attendance marks: 2

---

## Future Enhancements

- Add support for skipping classes (how many can be missed before marks drop)
- Add prediction tools (how many classes needed to reach target %)
- Export attendance summary to PDF
- Provide color-coded CLI output
- Add custom attendance rules per university

---

## License

This project is created for academic coursework and educational use.

---

## Author

**Shivraj Mulik**  
CLI Attendance Manager

---




