class StudentManagement:
    def __init__(self):
        # Data structure: {student_id: {'name': '...', 'attendance': {'date': 'status'}, 'marks': {'subject': score}}}
        self.students = {}

    def add_student(self, student_id, name):
        """Adds a new student to the system."""
        if student_id in self.students:
            print(f"Error: Student ID '{student_id}' already exists.")
        else:
            self.students[student_id] = {
                'name': name,
                'attendance': {},
                'marks': {}
            }
            print(f"Success: Student '{name}' (ID: {student_id}) added.")

    def mark_attendance(self, student_id, date, status):
        """Marks attendance (Present/Absent) for a specific date."""
        if student_id not in self.students:
            print("Error: Student ID not found.")
            return
        
        # Storing status securely (e.g., 'P' or 'A')
        self.students[student_id]['attendance'][date] = status.upper()
        print(f"Success: Attendance marked for {self.students[student_id]['name']} on {date}.")

    def add_marks(self, student_id, subject, marks):
        """Adds marks for a specific subject."""
        if student_id not in self.students:
            print("Error: Student ID not found.")
            return
        
        self.students[student_id]['marks'][subject] = marks
        print(f"Success: Marks added for {self.students[student_id]['name']} in {subject}.")

    def view_student(self, student_id):
        """Displays all details for a single student."""
        if student_id not in self.students:
            print("Error: Student ID not found.")
            return

        student = self.students[student_id]
        print("\n" + "="*30)
        print(f"Student Profile: {student['name']} (ID: {student_id})")
        print("-" * 30)
        
        print("--- Attendance ---")
        if not student['attendance']:
            print("No attendance records.")
        else:
            for date, status in student['attendance'].items():
                print(f"{date}: {'Present' if status == 'P' else 'Absent'}")
                
        print("\n--- Marks ---")
        if not student['marks']:
            print("No marks recorded.")
        else:
            for subject, score in student['marks'].items():
                print(f"{subject}: {score}")
        print("="*30 + "\n")

# --- Interactive CLI Menu ---
def main():
    sms = StudentManagement()
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Add Marks")
        print("4. View Student Details")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            s_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            sms.add_student(s_id, name)
            
        elif choice == '2':
            s_id = input("Enter Student ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            status = input("Enter Status (P/A): ")
            sms.mark_attendance(s_id, date, status)
            
        elif choice == '3':
            s_id = input("Enter Student ID: ")
            subject = input("Enter Subject: ")
            try:
                marks = float(input("Enter Marks: "))
                sms.add_marks(s_id, subject, marks)
            except ValueError:
                print("Error: Please enter a valid number for marks.")
                
        elif choice == '4':
            s_id = input("Enter Student ID: ")
            sms.view_student(s_id)
            
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()