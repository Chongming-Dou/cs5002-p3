from load_data import load_data
from refine_data import refine_data
from descriptive_analysis import descriptive_analysis
from plot_visualizations import plot_bar_chart

if __name__ == "__main__":
    # File paths
    input_path = "../data/Scotland_teaching_file_1PCT.csv"
    output_path = "../data/refined_data.csv"

    # Load data
    data = load_data(input_path)

    # Define admissible values and ranges
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

    # Refine data
    refined_data = refine_data(data, admissible_values, ranges, output_path)

    # Descriptive analysis
    total_records, variable_types, unique_values = descriptive_analysis(refined_data)
    print("\nUnique Values and Counts:\n", unique_values)

    # Visualizations
    plot_bar_chart(refined_data, "age", "Number of Records by Age Group")
    plot_bar_chart(refined_data, "Occupation", "Number of Records by Occupation")

