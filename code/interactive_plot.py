import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets


def plot_interactive(data, health_descriptor, age_range):
    """
    Plot the distribution of records for selected health descriptor and age range.

    Args:
        data (DataFrame): The dataset containing "health", "age", and "Economic_Activity".
        health_descriptor (int): Selected health descriptor value.
        age_range (tuple): Tuple representing the min and max age range (inclusive).
    """
    age_min, age_max = age_range  # Unpack the age range tuple
    filtered_data = data[
        (data["health"] == health_descriptor) &
        (data["age"] >= age_min) &
        (data["age"] <= age_max)
        ]

    plt.figure(figsize=(10, 6))
    filtered_data["Economic_Activity"].value_counts().plot(kind="bar", color="skyblue", alpha=0.7)
    plt.title(f"Distribution of Economic Activity for Health {health_descriptor} and Age {age_min}-{age_max}")
    plt.xlabel("Economic Activity")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()


def create_interactive_plot(data):
    """
    Create interactive widgets to filter and visualize data.

    Args:
        data (DataFrame): The dataset containing "health", "age", and "Economic_Activity".
    """
    health_dropdown = widgets.Dropdown(
        options=sorted(data["health"].dropna().unique()),
        value=sorted(data["health"].dropna().unique())[0],  # Default to the first value
        description="Health:"
    )

    age_slider = widgets.IntRangeSlider(
        value=[data["age"].min(), data["age"].max()],
        min=data["age"].min(),
        max=data["age"].max(),
        step=1,
        description="Age Range:"
    )

    interact(lambda health_descriptor, age_range: plot_interactive(data, health_descriptor, age_range),
             health_descriptor=health_dropdown, age_range=age_slider)
