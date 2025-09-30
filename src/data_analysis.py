# TODO: Implement analysis here
# Read the CSV file line by line using open() and readlines()
# Split each line by commas to extract fields
# Calculate basic statistics (total students, average grade)
# Count students by subject
# Write results to output/analysis_report.txt
# Use f-strings with .1f formatting for decimal numbers

import os


def load_students():
    """Read CSV and return list of student data using open() and readlines()"""
    with open("data/students.csv") as file:
        lines = file.readlines()
        records = [line.strip().split(",") for line in lines[1:]]  # Skip header
    return records


def avg_grade(students):
    """calculate_average_grade(students): Calculate and return average"""
    total_students = len(students)
    grades = [float(s[2]) for s in students]
    avg_grade = sum(grades) / total_students if total_students > 0 else 0
    return total_students, avg_grade


def count_math_students(students):
    """Count students in Math"""
    return sum(1 for s in students if s[3].strip() == "Math")


def generate_report(students):
    """Generate formatted report string"""
    total_students, avg_grade = avg_grade(students)
    math_students = count_math_students(students)

    subject_counts = {}
    subject_grades = {}
    for s in students:
        subject = s[3].strip()
        grade = float(s[2])
        subject_counts[subject] = subject_counts.get(subject, 0) + 1
        subject_grades[subject] = subject_grades.get(subject, []) + [grade]
    # average grade per subject
    subject_avg = {
        subj: sum(subject_grades[subj]) / len(subject_grades[subj])
        for subj in subject_counts
    }

    # Build report string
    report = f"Project Analysis Report\n"
    report += "-" * 30 + "\n"
    report += f"Total Students: {total_students}\n"
    report += f"Average Grade: {avg_grade:.1f}\n"
    report += f"Math Students: {math_students}\n"

    report += "\nStudents by Subject:\n"
    for subj, count in subject_counts.items():
        report += f" {subj:<25} {count}\n"

    report += "Average Grade by Subject:\n"
    for subj, avg in subject_avg.items():
        report += f" {subj:<25} {avg:.1f}\n"

    return report


def save_report(report, filename="output/analysis_report.txt"):
    """Write report string to file"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write(report)


def main():
    """Orchestrate the analysis"""
    students = load_students()
    report = generate_report(students)
    save_report(report)
    print("Analysis complete. Report saved to output/analysis_report.txt")
    print("Analysis complete. Report saved to output/analysis_report.txt")
