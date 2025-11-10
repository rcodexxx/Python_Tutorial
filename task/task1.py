def analyze_grades(students):
    result = {}

    for name, scores in students.items():
        average = round(sum(scores) / len(scores), 1)

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        pass_status = average >= 60

        result[name] = {
            "average": average,
            "grade": grade,
            "pass": pass_status
        }

    return result

students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [55, 60, 58]
}
result = analyze_grades(students)