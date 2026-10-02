import pandas as pd

FILE_NAME = "students.csv"
PASS_MARKS = 50


def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= PASS_MARKS:
        return "D"
    else:
        return "F"


def load_data():
    df = pd.read_csv(FILE_NAME)
    df["Grade"] = df["Marks"].apply(get_grade)
    return df


def show_all_students(df):
    print("\n--- All Students ---")
    print(df[["Name", "RollNumber", "Subject", "Marks", "Grade"]].to_string(index=False))


def show_summary(df):
    print("\n--- Summary ---")
    total_students = len(df)
    average_marks = df["Marks"].mean()
    highest_marks = df["Marks"].max()
    lowest_marks = df["Marks"].min()
    passing = df[df["Marks"] >= PASS_MARKS]
    failing = df[df["Marks"] < PASS_MARKS]
    top_student = df.loc[df["Marks"].idxmax(), "Name"]

    print("Total Students:", total_students)
    print("Average Marks:", round(average_marks, 2))
    print("Highest Marks:", highest_marks)
    print("Lowest Marks:", lowest_marks)
    print("Passing Students:", len(passing))
    print("Failing Students:", len(failing))
    print("Top Student:", top_student)


def show_top_3(df):
    print("\n--- Top 3 Students ---")
    top3 = df.sort_values(by="Marks", ascending=False).head(3)
    print(top3[["Name", "Marks"]].to_string(index=False))


def search_by_name(df):
    name = input("Enter student name to search: ").strip().lower()
    result = df[df["Name"].str.lower() == name]
    if result.empty:
        print("Student not found.")
    else:
        print(result[["Name", "RollNumber", "Subject", "Marks", "Grade"]].to_string(index=False))


def filter_by_marks(df):
    try:
        minimum = float(input("Show students with marks above: "))
    except ValueError:
        print("Invalid number.")
        return
    result = df[df["Marks"] > minimum]
    if result.empty:
        print(f"No students scored above {minimum}.")
    else:
        print(f"\n--- Students Above {minimum} Marks ---")
        print(result[["Name", "Marks"]].to_string(index=False))


def average_by_subject(df):
    print("\n--- Average Marks by Subject ---")
    averages = df.groupby("Subject")["Marks"].mean().round(2)
    print(averages.to_string())


def main():
    df = load_data()

    while True:
        print("\n===== Student Performance Analysis =====")
        print("1. Show All Students")
        print("2. Show Summary (average, highest, lowest, pass/fail, top student)")
        print("3. Top 3 Students")
        print("4. Search Student by Name")
        print("5. Filter Students Above a Mark")
        print("6. Average Marks by Subject")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_students(df)
        elif choice == "2":
            show_summary(df)
        elif choice == "3":
            show_top_3(df)
        elif choice == "4":
            search_by_name(df)
        elif choice == "5":
            filter_by_marks(df)
        elif choice == "6":
            average_by_subject(df)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()