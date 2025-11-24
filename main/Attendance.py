import csv
import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "attendance.csv")
COURSES_PATH = os.path.join(BASE_DIR, "courses.json")
DATE_FMT = "%d%m"


def ensure_files():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Course", "Date", "Status"])
    if not os.path.exists(COURSES_PATH):
        with open(COURSES_PATH, "w", encoding="utf-8") as f:
            json.dump({}, f)


def load_courses():
    with open(COURSES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_courses(courses):
    with open(COURSES_PATH, "w", encoding="utf-8") as f:
        json.dump(courses, f, indent=2)


def add_course():
    courses = load_courses()
    name = input("Course name (unique): ").strip()
    if not name:
        print("Empty name; cancelled.")
        return
    if name in courses:
        print("Course already exists.")
        return
    
    max_marks = 5.0
    courses[name] = {"max_marks": max_marks}
    save_courses(courses)
    print(f"Added course '{name}' with max marks {max_marks}.")


def remove_course():
    courses = load_courses()
    if not courses:
        print("No courses to remove.")
        return
    print("Courses:")
    for i, c in enumerate(courses.keys(), 1):
        print(f"{i}. {c}")
    name = input("Course name to remove (exact): ").strip()
    if name not in courses:
        print("Course not found.")
        return
    confirm = input(f"Delete course '{name}' and its attendance rows? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return
    del courses[name]
    save_courses(courses)
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r["Course"] != name:
                rows.append(r)
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Course", "Date", "Status"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Course '{name}' and its attendance removed.")


def list_courses():
    courses = load_courses()
    if not courses:
        print("No courses added yet.")
        return
    print("Courses:")
    for name, meta in courses.items():
        print(f"- {name}  (max_marks: {meta.get('max_marks', 5)})")


def append_attendance_row(course, date_str, status):
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([course, date_str, status])


def add_attendance():
    courses = load_courses()
    if not courses:
        print("Add a course first.")
        return
    print("Select course:")
    for i, c in enumerate(courses.keys(), 1):
        print(f"{i}. {c}")
    sel = input("Course name (exact) or number: ").strip()
    if sel.isdigit():
        idx = int(sel) - 1
        try:
            course = list(courses.keys())[idx]
        except IndexError:
            print("Invalid number.")
            return
    else:
        course = sel
    if course not in courses:
        print("Course not found.")
        return
    date_inp = input(f"Date (DDMM) [default today {datetime.today().strftime(DATE_FMT)}]: ").strip()
    if not date_inp:
        date_str = datetime.today().strftime(DATE_FMT)
    else:
        try:
            _ = datetime.strptime(date_inp, DATE_FMT)
            date_str = date_inp
        except ValueError:
            print("Invalid date format.")
            return
    st = input("Status - present (p) or absent (a): ").strip().lower()
    if st not in ("p", "a", "present", "absent"):
        print("Invalid status.")
        return
    status = "P" if st[0] == "p" else "A"
    updated = False
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r["Course"] == course and r["Date"] == date_str:
                rows.append({"Course": course, "Date": date_str, "Status": status})
                updated = True
            else:
                rows.append(r)
    if updated:
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Course", "Date", "Status"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Updated attendance for {course} on {date_str} -> {status}")
    else:
        append_attendance_row(course, date_str, status)
        print(f"Recorded attendance for {course} on {date_str} -> {status}")


def compute_stats_for_course(course):
    total = 0
    present = 0
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r["Course"] == course:
                total += 1
                if r["Status"].upper() == "P":
                    present += 1
    percent = (present / total * 100) if total > 0 else 0.0
    return total, present, round(percent, 2)


def show_report():
    courses = load_courses()
    if not courses:
        print("No courses.")
        return
    print("Select course for report:")
    for i, c in enumerate(courses.keys(), 1):
        print(f"{i}. {c}")
    sel = input("Course name or number: ").strip()
    if sel.isdigit():
        idx = int(sel) - 1
        try:
            course = list(courses.keys())[idx]
        except IndexError:
            print("Invalid number.")
            return
    else:
        course = sel
    if course not in courses:
        print("Course not found.")
        return
    total, present, percent = compute_stats_for_course(course)
    max_marks = 5.0
    debarred = percent < 75.0
    if percent >= 95:
        marks_obtained = 5
    elif percent >= 90:
        marks_obtained = 4
    elif percent >= 85:
        marks_obtained = 3
    elif percent >= 80:
        marks_obtained = 2
    elif percent >= 75:
        marks_obtained = 1
    else:
        marks_obtained = 0
    print(f"Report for '{course}':")
    print(f"- Sessions recorded: {total}")
    print(f"- Presents: {present}")
    print(f"- Attendance %: {percent}%")
    print(f"- Debarred (<75%): {'YES :(' if debarred else 'NO :)'}")
    if not debarred:
        print(f"- Attendance marks (out of {max_marks}): {marks_obtained}")
    else:
        print("- No marks awarded due to debarment.")


def show_help():
    print(
        "\nCommands (you can enter the number shown):\n"
        "  1) add_course     - Add a new course (max marks fixed at 5)\n"
        "  2) remove_course  - Remove a course and its attendance rows\n"
        "  3) list           - List courses\n"
        "  4) add_attendance - Record attendance for a course (DDMM)\n"
        "  5) report         - Show attendance %, debarred status, and marks\n"
        "  6) help           - Show this help\n"
        "  7) exit           - Save & exit\n"
    )


def main_loop():
    ensure_files()
    print("Attendance CLI. Type 'help' or enter a number for commands.")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "1":
            cmd = "add_course"
        elif cmd == "2":
            cmd = "remove_course"
        elif cmd == "3":
            cmd = "list"
        elif cmd == "4":
            cmd = "add_attendance"
        elif cmd == "5":
            cmd = "report"
        elif cmd == "6":
            cmd = "help"
        elif cmd == "7":
            cmd = "exit"
        if cmd in ("add_course", "ac"):
            add_course()
        elif cmd in ("remove_course", "rc"):
            remove_course()
        elif cmd in ("list", "ls"):
            list_courses()
        elif cmd in ("add_attendance", "aa"):
            add_attendance()
        elif cmd in ("report", "rep"):
            show_report()
        elif cmd in ("help", "h", "?"):
            show_help()
        elif cmd in ("exit", "quit", "q"):
            print("Exiting.")
            break
        elif cmd == "":
            continue
        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main_loop()
