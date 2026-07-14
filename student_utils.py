def calculate_average(*marks):
    return sum(marks) / len(marks)


def get_grade(avg, pass_mark=40):
    if avg < pass_mark:
        return "Fail"
    if avg >= 80:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 40:
        return "C"
    return "Fail"
