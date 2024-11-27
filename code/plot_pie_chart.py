import matplotlib.pyplot as plt

def plot_pie_chart_with_legend(data, column, title):
    """
    Generate a pie chart with percentages displayed in the legend.

    Args:
        data (DataFrame): Dataset containing the column.
        column (str): Column name for pie chart.
        title (str): Title for the pie chart.
    """
    values = data[column].value_counts()
    labels = values.index
    sizes = values.values

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    wedges, _ = plt.pie(sizes, startangle=140, colors=plt.cm.tab20.colors[:len(labels)])

    # Create the legend with percentages
    legend_labels = [f"{label} - {size / sum(sizes) * 100:.1f}%" for label, size in zip(labels, sizes)]
    plt.legend(wedges, legend_labels, title="Legend", loc="best")
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    import pandas as pd
    from load_data import load_data

    input_path = "../data/refined_data.csv"
    data = load_data(input_path)

    # Generate pie chart for "health" (general health descriptor)
    plot_pie_chart_with_legend(data, "health", "Percentage of Records for Each General Health Descriptor")

    # Generate pie chart for "Ethnic_Group"
    plot_pie_chart_with_legend(data, "Ethnic_Group", "Percentage of Records for Each Ethnic Group")
