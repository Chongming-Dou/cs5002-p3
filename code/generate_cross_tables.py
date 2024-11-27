import pandas as pd


def generate_cross_table(data, row_variable, column_variable, output_path):
    """
    Generate a cross table (pivot table) based on the provided variables and save it as a CSV file.

    Args:
        data (DataFrame): Dataset for generating the table.
        row_variable (str): Variable to use for rows.
        column_variable (str): Variable to use for columns.
        output_path (str): Path to save the resulting table as a CSV file.
    """
    # Create cross table
    cross_table = data.groupby([row_variable, column_variable]).size().unstack(fill_value=0)

    # Save table to CSV
    cross_table.to_csv(output_path, index=True)
    print(f"Cross table saved to '{output_path}'")
    return cross_table


if __name__ == "__main__":
    from load_data import load_data

    # Load the dataset
    input_path = "../data/refined_data.csv"
    data = load_data(input_path)

    # Generate and save cross tables
    hours_worked_industry = generate_cross_table(
        data,
        row_variable="Hours_Worked_Per_Week",
        column_variable="industry",
        output_path="hours_worked_industry.csv"
    )

    occupation_social_grade = generate_cross_table(
        data,
        row_variable="Occupation",
        column_variable="Approximate_Social_Grade",
        output_path="occupation_social_grade.csv"
    )
