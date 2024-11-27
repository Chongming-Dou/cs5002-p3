import pandas as pd

def refine_data(data, admissible_values, ranges, output_path):
    """
    Refine the dataset:
    1. Check variable formats and values.
    2. Remove duplicates.
    3. Save refined dataset to a new file.
    """
    refined_data = data.copy()

    # Check formats and admissible values
    for column, valid_values in admissible_values.items():
        refined_data[column] = refined_data[column].where(refined_data[column].isin(valid_values), pd.NA)

    # Check numerical ranges
    for column, (min_val, max_val) in ranges.items():
        refined_data[column] = refined_data[column].where(
            (refined_data[column] >= min_val) & (refined_data[column] <= max_val), pd.NA
        )

    # Remove duplicates
    refined_data = refined_data.drop_duplicates()

    # Save refined data
    refined_data.to_csv(output_path, index=False)
    print(f"Refined data saved to: {output_path}")

    return refined_data

if __name__ == "__main__":
    from load_data import load_data


    input_path = "../data/Scotland_teaching_file_1PCT.csv"
    output_path = "../data/refined_data.csv"
    data = load_data(input_path)

    admissible_values = {
        "RESIDENCE_TYPE": ["P", "C"],
        "Family_Composition": ["1", "0", "2", "3", "4", "5"],
        "Economic_Activity": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "Occupation": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "industry": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"],
        "Hours_Worked_Per_Week": ["1", "2", "3", "4"],
        "Approximate_Social_Grade": ["1", "2", "3", "4"]
    }

    ranges = {
        "age": (1, 8),
        "health": (1, 5),
        "student": (1, 2),
        "Ethnic_Group": (1, 6),
        "religion": (1, 9),
        "Country_Of_Birth": (1, 2),
    }

    refine_data(data, admissible_values, ranges, output_path)
