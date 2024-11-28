import pandas as pd
import argparse


def load_data(file_path):
    """
    Load the dataset from the specified file path.
    """
    return pd.read_csv(file_path)


def refine_data(data, admissible_values, ranges, output_path):
    """
    Refine the dataset:
    1. Check variable formats and values.
    2. Remove duplicates.
    3. Save refined dataset to a new file.

    Args:
        data (DataFrame): Original dataset.
        admissible_values (dict): Expected admissible values for categorical variables.
        ranges (dict): Expected ranges for numerical variables.
        output_path (str): Path to save the refined dataset.
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
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Refine a dataset based on specified rules.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_file", help="Path to save the refined CSV file.")
    parser.add_argument("--admissible_values", required=True,
                        help="JSON file specifying admissible values for categorical columns.")
    parser.add_argument("--ranges", required=True, help="JSON file specifying ranges for numerical columns.")

    args = parser.parse_args()

    # Load dataset
    data = load_data(args.input_file)

    # Load admissible values and ranges from JSON files
    admissible_values = pd.read_json(args.admissible_values, typ='dictionary')
    ranges = pd.read_json(args.ranges, typ='dictionary')

    # Refine dataset
    refine_data(data, admissible_values, ranges, args.output_file)
