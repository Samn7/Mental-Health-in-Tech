# Mental Health in Tech Survey Analysis
# -------------------------------------
# This program analyzes a mental health survey dataset using Python.

# Importing the necessary libraries
import pandas as pd       # For handling datasets (loading, cleaning, exploring)
import matplotlib.pyplot as plt  # For plotting graphs
import seaborn as sns     # For advanced visualizations

# Optional: Configure visual style for seaborn
sns.set(style="whitegrid")

# 1. Load the dataset
file_path = "survey.csv"   # Make sure your CSV is in the same folder
df = pd.read_csv(file_path)

# 2. Print a welcome message
print("🔍 Welcome to the Mental Health in Tech Survey Analysis!")
print("📁 Dataset loaded successfully.\n")

# 3. Display basic information about the dataset
print("📊 Dataset Information:")
print(df.info())

# 4. Show the first 5 rows to preview data
print("\n👀 Here's a preview of the dataset:")
print(df.head())
