# Module 4 Homework: Exercise 1
# The function takes a file path as input. The file is expected to have a name and salary separated by commas on each
# row. The function calculates the total and average of salaries and outputs them as a tuple.
# The function returns 0.0, 0.0 if there are no valid entries in the file or if the file is not found or inaccessible.

from pathlib import Path


def total_salary(path) -> tuple:
    file_path = Path(path)  # create Path object for file

    try:  # check for errors with path/file
        with open(file_path, 'r', encoding='utf-8') as file:
            tot_salaries = 0.0
            num_salaries = 0
            for line in file:  # process each line in the file
                try:  # check for errors with entries in the file
                    name, salary = line.split(',')
                    tot_salaries += float(salary)
                    num_salaries += 1

                except ValueError:  # skip lines where there are no valid entries
                    continue

        if num_salaries > 0:
            avg = tot_salaries / num_salaries  # calculate average salary if number of salaries > 0
            return round(tot_salaries, 2), round(avg, 2)  # return total and average of salaries

        else:  # return 0.0, 0.0 if no valid entries in the file
            print('There are no valid entries in the file.')
            return 0.0, 0.0

    except Exception as expt:  # output exception with file access and return 0.0, 0.0
        print('Exception: ', expt)
        return 0.0, 0.0


total, average = total_salary("01/salary_file.txt")
print(f"Sum of salaries: {total}\nAverage salary: {average}")
