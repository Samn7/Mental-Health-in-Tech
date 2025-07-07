# Part 4: Exploring Data Relationships using Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path = "survey.csv"
df = pd.read_csv(file_path)

# Clean Gender and Age
def clean_gender(g):
    g = str(g).strip().lower()
    if g in ['male', 'm', 'man', 'cis male']:
        return 'Male'
    elif g in ['female', 'f', 'woman', 'cis female']:
        return 'Female'
    else:
        return 'Other'

df['Gender'] = df['Gender'].apply(clean_gender)
df = df[(df['Age'] >= 18) & (df['Age'] <= 65)]

sns.set(style="darkgrid")

# 📌 1. Countplot: Treatment count by Gender
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Gender', hue='treatment')
plt.title("Treatment by Gender")
plt.tight_layout()
plt.show()

# 📌 2. Boxplot: Age vs. Treatment
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='treatment', y='Age', palette='Set2')
plt.title("Age Distribution by Treatment")
plt.tight_layout()
plt.show()

# 📌 3. Heatmap: Correlation matrix (numeric only)
plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# 📌 4. Catplot: Work interfere vs. Treatment
sns.catplot(data=df, x='work_interfere', hue='treatment', kind='count', height=4, aspect=2)
plt.title("Work Interference vs. Mental Health Treatment")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
