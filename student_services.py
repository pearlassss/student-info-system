
import json
from datetime import datetime
from student import Student

class StudentService:
    def __init__(self, filename='students.json'):
        self.filename = filename

    def _load_students(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_students(self, students):
        with open(self.filename, 'w') as file:
            json.dump(students, file, indent=4)

    def add_student(self, student_data):
        students = self._load_students()
        student = Student(**student_data)
        students.append(student.to_dict())
        self._save_students(students)
        return student.to_dict()

    def get_all_students(self):
        return self._load_students()

    def get_student(self, student_id):
        students = self._load_students()
        for student in students:
            if student['student_id'] == student_id:
                return student
        return None

    def update_student(self, student_id, update_data):
        students = self._load_students()
        for student in students:
            if student['student_id'] == student_id:
                student.update(update_data)
                student['updated_at'] = datetime.now().isoformat()
                self._save_students(students)
                return student
        return None

    def delete_student(self, student_id):
        students = self._load_students()
        new_students = [s for s in students if s['student_id'] != student_id]
        if len(new_students) != len(students):
            self._save_students(new_students)
            return True
        return False