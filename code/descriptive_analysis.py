def descriptive_analysis(data):
    """
    Perform descriptive analysis on the dataset.
    """
    # Total number of records
    total_records = len(data)
    print(f"Total records: {total_records}")

    # Variable types
    variable_types = data.dtypes
    print("\nVariable Types:\n", variable_types)

    # Unique values and occurrences for each variable
    unique_values = {}
    for col in data.columns:
        if col not in ["Record_Number", "Region"]:
            unique_values[col] = data[col].value_counts()
    return total_records, variable_types, unique_values

if __name__ == "__main__":
    import pandas as pd
    from load_data import load_data
    from refine_data import refine_data

    input_path = "../data/refined_data.csv"
    data = load_data(input_path)

    total_records, variable_types, unique_values = descriptive_analysis(data)
    print("\nUnique Values and Counts:\n", unique_values)
