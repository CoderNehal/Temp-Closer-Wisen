import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, pearsonr

# Sample data (replace this with your dataset)
data = pd.read_csv("data.csv")


# Create a tkinter window
window = tk.Tk()
window.title("Data Analysis Tool")

# Function to perform Chi-Square Test
def chi_square_test():
    attribute1 = combo_attribute1.get()
    attribute2 = combo_attribute2.get()
    contingency_table = pd.crosstab(data[attribute1], data[attribute2])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    result_label.config(text=f"Chi-Square Value: {chi2:.2f}")
    if p < 0.05:
        conclusion_label.config(text="Conclusion: Correlated")
    else:
        conclusion_label.config(text="Conclusion: Not Correlated")
    contingency_table_label.config(text="Contingency Table:\n" + str(contingency_table))

# Function to perform Correlation Analysis
def correlation_analysis():
    attribute1 = combo_attribute1.get()
    attribute2 = combo_attribute2.get()
    corr_coefficient, _ = pearsonr(data[attribute1], data[attribute2])
    result_label.config(text=f"Pearson Correlation Coefficient: {corr_coefficient:.2f}")
    if abs(corr_coefficient) >= 0.7:
        conclusion_label.config(text="Conclusion: Strong Correlation")
    elif abs(corr_coefficient) >= 0.3:
        conclusion_label.config(text="Conclusion: Moderate Correlation")
    else:
        conclusion_label.config(text="Conclusion: Weak Correlation")

# Function to perform Normalization
def normalize_data():
    attribute = combo_attribute1.get()
    normalization_type = combo_normalization.get()
    
    if normalization_type == "Min-Max":
        min_val = data[attribute].min()
        max_val = data[attribute].max()
        normalized_data = (data[attribute] - min_val) / (max_val - min_val)
    elif normalization_type == "Z-Score":
        mean_val = data[attribute].mean()
        std_dev = data[attribute].std()
        normalized_data = (data[attribute] - mean_val) / std_dev
    elif normalization_type == "Decimal Scaling":
        max_digit = len(str(int(data[attribute].max())))
        divisor = 10 ** max_digit
        normalized_data = data[attribute] / divisor
    
    normalized_table.config(text="Normalized Data:\n" + str(normalized_data))
    
    # Scatter plot
    import matplotlib.pyplot as plt
    plt.scatter(data[attribute], normalized_data)
    plt.xlabel(attribute)
    plt.ylabel(f"Normalized {attribute}")
    plt.title("Scatter Plot")
    plt.show()

# Create and place widgets on the window
label_attribute1 = ttk.Label(window, text="Select Attribute 1:")
label_attribute1.grid(column=0, row=0, padx=10, pady=10)

combo_attribute1 = ttk.Combobox(window, values=list(data.keys()))
combo_attribute1.grid(column=1, row=0, padx=10, pady=10)

label_attribute2 = ttk.Label(window, text="Select Attribute 2:")
label_attribute2.grid(column=0, row=1, padx=10, pady=10)

combo_attribute2 = ttk.Combobox(window, values=list(data.keys()))
combo_attribute2.grid(column=1, row=1, padx=10, pady=10)

btn_chi_square = ttk.Button(window, text="Chi-Square Test", command=chi_square_test)
btn_chi_square.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

btn_correlation = ttk.Button(window, text="Correlation Analysis", command=correlation_analysis)
btn_correlation.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

label_normalization = ttk.Label(window, text="Normalization Technique:")
label_normalization.grid(column=0, row=4, padx=10, pady=10)

combo_normalization = ttk.Combobox(window, values=["Min-Max", "Z-Score", "Decimal Scaling"])
combo_normalization.grid(column=1, row=4, padx=10, pady=10)

btn_normalize = ttk.Button(window, text="Normalize Data", command=normalize_data)
btn_normalize.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(window, text="")
result_label.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

conclusion_label = ttk.Label(window, text="")
conclusion_label.grid(column=0, row=7, columnspan=2, padx=10, pady=10)

contingency_table_label = ttk.Label(window, text="")
contingency_table_label.grid(column=0, row=8, columnspan=2, padx=10, pady=10)

normalized_table = ttk.Label(window, text="")
normalized_table.grid(column=0, row=9, columnspan=2, padx=10, pady=10)

# Start the tkinter main loop
window.mainloop()
