# AttendTrack - file handling
FILE_NAME = "attendance.txt"

def mark_attendance():
    name = input("Employee name: ")
    status = input("Present or Absent (P/A): ").upper()
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(name + "," + status + "\n")
    print("Attendance saved.")

def view_attendance():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            print("\nAttendance records")
            print(file.read())
    except FileNotFoundError:
        print("No attendance records yet.")

while True:
    print("\n1. Mark attendance  2. View records  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
