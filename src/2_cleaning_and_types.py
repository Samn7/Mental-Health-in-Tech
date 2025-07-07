# Part 2: Cleaning and Exploring Data Types

import pandas as pd

# Load the dataset
file_path = "survey.csv"
df = pd.read_csv(file_path)

print("🔧 Data Cleaning in Progress...\n")

# 1. Cleaning 'Gender' column — standardizing values
def clean_gender(gender):
    gender = str(gender).strip().lower()
    if gender in ['male', 'm', 'man', 'cis male']:
        return 'Male'
    elif gender in ['female', 'f', 'woman', 'cis female']:
        return 'Female'
    else:
        return 'Other'

df['Gender'] = df['Gender'].apply(clean_gender)

# 2. Cleaning 'Age' column — removing unrealistic ages
df = df[(df['Age'] >= 18) & (df['Age'] <= 65)]

# 3. Showing cleaned column types
print("📄 Cleaned Data Types:")
print(df.dtypes)

# 4. Show missing values per column
print("\n❓ Missing Values per Column:")
print(df.isnull().sum())

# 5. Summary of cleaned dataset
print("\n📈 Summary Statistics:")
print(df.describe(include='all'))
