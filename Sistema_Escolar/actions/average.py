def calculate_average(student_list):

    average_list = []

    for student in student_list:

        student_name = student["Full_name"]

        grade_average = (
            int(student["Spanish_grade"]) +
            int(student["English_grade"]) +
            int(student["Social_studies_grade"]) +
            int(student["Science_grade"])
        ) / 4

        average_list.append({
            "student_name": student_name,
            "grade_average": grade_average
        })

    return average_list