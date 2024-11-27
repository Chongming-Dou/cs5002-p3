import subprocess
import os


def convert_notebook_to_html(notebook_path, output_path):
    """
    Convert a Jupyter Notebook file to an HTML file using `nbconvert`.

    Args:
        notebook_path (str): Path to the input Jupyter Notebook file.
        output_path (str): Path to save the converted HTML file.
    """
    try:
        result = subprocess.run([
            "jupyter", "nbconvert",
            "--to", "html",
            "--output", output_path,
            notebook_path
        ], check=True, capture_output=True, text=True)
        print(f"Conversion successful! HTML report saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion:\nCommand: {e.cmd}\nReturn Code: {e.returncode}")
        print(f"STDOUT:\n{e.stdout}")
        print(f"STDERR:\n{e.stderr}")
        raise


if __name__ == "__main__":
    # Input and output paths
    notebook_file = "../notebooks/census2011.ipynb"  # Replace with your notebook name
    output_file = "./data_analysis_report.html"  # Replace with your desired HTML output name

    # Convert the notebook to HTML
    convert_notebook_to_html(notebook_file, output_file)
