import pandas as pd


def economically_active_by_age(data, active_codes):
    """
    Calculate the number of economically active people by age.

    Args:
        data (DataFrame): Dataset containing "Economic_Activity" and "age".
        active_codes (list): Codes representing economically active individuals.

    Returns:
        Series: Number of economically active people by age.
    """
    return data[data["Economic_Activity"].isin(active_codes)].groupby("age").size()


def economically_inactive_by_health(data, inactive_codes):
    """
    Calculate the number of economically inactive people by health.

    Args:
        data (DataFrame): Dataset containing "Economic_Activity" and "health".
        inactive_codes (list): Codes representing economically inactive individuals.

    Returns:
        Series: Number of economically inactive people by health.
    """
    return data[data["Economic_Activity"].isin(inactive_codes)].groupby("health").size()


def student_hours_worked(data, student_codes):
    """
    Calculate the total number of working hours per week for students.

    Args:
        data (DataFrame): Dataset containing "Economic_Activity" and "Hours_Worked_Per_Week".
        student_codes (list): Codes representing students in "Economic_Activity".

    Returns:
        Series: Total number of working hours per week for students.
    """
    return data[data["Economic_Activity"].isin(student_codes)].groupby("Hours_Worked_Per_Week").size()


if __name__ == "__main__":
    from load_data import load_data  # Assuming load_data.py exists for loading the data.

    # Load the dataset
    input_path = "../data//refined_data.csv"
    data = load_data(input_path)

    # Define codes for analysis
    economically_active_codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    economically_inactive_codes = ['X']  # Assuming 'X' represents inactive or missing data
    student_codes = ['4', '6']

    # Perform analyses
    active_by_age = economically_active_by_age(data, economically_active_codes)
    print("Economically Active People by Age:\n", active_by_age)

    inactive_by_health = economically_inactive_by_health(data, economically_inactive_codes)
    print("\nEconomically Inactive People by Health:\n", inactive_by_health)

    student_hours = student_hours_worked(data, student_codes)
    print("\nHours Worked Per Week by Students:\n", student_hours)
