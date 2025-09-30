# TODO: Add functions for data analysis here

import os


def load_data(filename):
    """Generic loader that checks file extension before loading"""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found.")

    if filename.endswith(".csv"):
        return load_csv(filename)
    else:
        raise ValueError("Unsupported file format. Only CSV is supported.")


def load_csv(filename):
    """Load CSV file into a list of student records (excluding header)"""
    with open(filename, "r") as f:
        lines = f.readlines()
    records = [line.strip().split(",") for line in lines[1:]]  # skip header
    return records


def analyze_data(students):
    """Return dictionary with multiple statistics including min/max and percentages"""
    total_students = len(students)
    grades = [float(s[2]) for s in students]

    # Basic stats
    avg_grade = sum(grades) / total_students if total_students > 0 else 0
    highest_grade = max(grades) if total_students > 0 else 0
    lowest_grade = min(grades) if total_students > 0 else 0

    # Count students per subject
    subject_counts = {}
    subject_totals = {}
    for s in students:
        subj = s[3].strip()
        grade = float(s[2])
        subject_counts[subj] = subject_counts.get(subj, 0) + 1
        subject_totals[subj] = subject_totals.get(subj, 0) + grade

    subject_avgs = {
        subj: subject_totals[subj] / subject_counts[subj] for subj in subject_counts
    }

    # Percentages per subject
    subject_percentages = {
        subj: (count / total_students) * 100 for subj, count in subject_counts.items()
    }

    # Grade distribution (A/B/C/D/F)
    grade_distribution = analyze_grade_distribution(grades, total_students)

    return {
        "total_students": total_students,
        "avg_grade": avg_grade,
        "highest_grade": highest_grade,
        "lowest_grade": lowest_grade,
        "subject_counts": subject_counts,
        "subject_avgs": subject_avgs,
        "subject_percentages": subject_percentages,
        "grade_distribution": grade_distribution,
    }


def analyze_grade_distribution(grades, total_students):
    """Count grades by letter grade ranges and percentages"""
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        if g >= 90:
            distribution["A"] += 1
        elif g >= 80:
            distribution["B"] += 1
        elif g >= 70:
            distribution["C"] += 1
        elif g >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    # Add percentages
    percentages = {k: (v / total_students) * 100 for k, v in distribution.items()}
    return {"counts": distribution, "percentages": percentages}


def save_results(results, filename="output/analysis_report.txt"):
    """Save analysis results to a formatted report file"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    report = "Project Analysis Report\n"
    report += "=" * 40 + "\n"
    report += f"Total Students: {results['total_students']}\n"
    report += f"Overall Average Grade: {results['avg_grade']:.1f}\n"
    report += f"Highest Grade: {results['highest_grade']:.1f}\n"
    report += f"Lowest Grade: {results['lowest_grade']:.1f}\n\n"

    report += "Average Grades by Subject:\n"
    for subj, avg in results["subject_avgs"].items():
        report += f"  {subj:<25} {avg:.1f}\n"

    report += "\nStudent Counts by Subject:\n"
    for subj, count in results["subject_counts"].items():
        report += (
            f"  {subj:<25} {count} ({results['subject_percentages'][subj]:.1f}%)\n"
        )

    report += "\nGrade Distribution:\n"
    for grade, count in results["grade_distribution"]["counts"].items():
        pct = results["grade_distribution"]["percentages"][grade]
        report += f"  {grade}: {count} ({pct:.1f}%)\n"

    with open(filename, "w") as f:
        f.write(report)


def main():
    """Orchestrate full analysis"""
    students = load_data("data/students.csv")
    results = analyze_data(students)
    save_results(results)
    print("Analysis complete. Report saved to output/analysis_report.txt")


if __name__ == "__main__":
    main()
