# Part 3: Data Visualization using Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path = "survey.csv"
df = pd.read_csv(file_path)

# Clean Gender
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

# 📊 1. Gender Distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6, 4))
gender_counts.plot(kind='bar', color=['skyblue', 'pink', 'gray'])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Respondents")
plt.tight_layout()
plt.show()

# 📊 2. Age Distribution
plt.figure(figsize=(6, 4))
plt.hist(df['Age'], bins=15, color='purple', edgecolor='white')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Respondents")
plt.tight_layout()
plt.show()

# 📊 3. Treatment vs. No Treatment
treatment_counts = df['treatment'].value_counts()
plt.figure(figsize=(6, 4))
treatment_counts.plot(kind='bar', color='teal')
plt.title("Seeking Mental Health Treatment")
plt.xlabel("Response")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 🥧 4. Optional: Pie chart - mental health consequence
consequence_counts = df['mental_health_consequence'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(consequence_counts, labels=consequence_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Mental Health Consequences at Work")
plt.axis('equal')
plt.tight_layout()
plt.show()
