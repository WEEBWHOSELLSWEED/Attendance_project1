# Attendance CLI - Technical Documentation

A CLI tool to manage course attendance, generate simple reports, and compute attendance marks.

**Setup:**
- No external dependencies. Place files in a folder and run:

**Files used:**
- `attendance.csv` — CSV with header `Course,Date,Status`. Status is `P` or `A`.
- `courses.json` — JSON storing course metadata (new courses include `max_marks: 5.0`).

Date format and compatibility:
- Entries use `DDMM` (e.g., `2411` for 24 Nov).

Commands / Usage (interactive):
- The CLI shows a numbered help menu. You can type the command name or its number (e.g., `4` for `add_attendance`).
- Typical flow:
  - `1` / `add_course` — add a course (max marks fixed at 5).
  - `4` / `add_attendance` — record a session: select course, enter date or press Enter for today, status `p`/`a`.
  - `5` / `report` — show totals, percent, debarred status, and computed attendance marks.

Scoring rules (attendance → marks):
- Max marks: 5 (fixed)
- Mapping by percentage (inclusive lower bounds):
  - 95% and above → 5
  - 90–94.99% → 4
  - 85–89.99% → 3
  - 80–84.99% → 2
  - 75–79.99% → 1
  - Below 75% → debarred (no marks)
