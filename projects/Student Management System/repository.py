from database import students


def get_all_students():
    return students


def get_student(id):
    for student in students:
        if student["id"] == id:
            return student
    return None


def insert_student(student):
    students.append(student)


def remove_student(student):
    students.remove(student)


def next_student_id():
    if not students:
        return 1
    highest = max(student["id"] for student in students)
    return highest + 1