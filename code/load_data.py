import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the specified file path.
    """
    return pd.read_csv(file_path)

if __name__ == "__main__":
    input_path = "../data/Scotland_teaching_file_1PCT.csv"
    data = load_data(input_path)
    print("Data loaded successfully.")
