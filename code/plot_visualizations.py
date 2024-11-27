import matplotlib.pyplot as plt

def plot_bar_chart(data, column, title):
    """
    Plot a bar chart for a categorical variable.
    """
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar', alpha=0.7)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    import pandas as pd
    from load_data import load_data

    input_path = "../data/refined_data.csv"
    data = pd.read_csv(input_path)

    # 示例：绘制柱状图
    plot_bar_chart(data, "age", "Number of Records by Age Group")
    plot_bar_chart(data, "Occupation", "Number of Records by Occupation")
