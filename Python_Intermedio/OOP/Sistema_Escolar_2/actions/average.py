from models.student import Student
def calculate_average(student_list):

    average_list = []

    for student in student_list:

        student_name = student.full_name

        grade_average = (
            student.spanish_grade +
            student.english_grade +
            student.social_studies_grade +
            student.science_grade
        ) / 4

        average_list.append({
            "student_name": student_name,
            "grade_average": grade_average
        })

    return average_list