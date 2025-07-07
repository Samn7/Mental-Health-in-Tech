import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("survey.csv")

# Clean Gender and Age
def clean_data(df):
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
    return df

# Clean once at the start
df = clean_data(df)

# 1. Dataset Overview
def view_overview():
    print("\n📊 Dataset Info:")
    print(df.info())
    print("\n👀 Preview:")
    print(df.head())

# 2. Clean and Show Types
def show_types():
    print("\n📄 Column Data Types:")
    print(df.dtypes)
    print("\n❓ Missing Values:")
    print(df.isnull().sum())
    print("\n📈 Summary Stats:")
    print(df.describe(include='all'))

# 3. Matplotlib Visuals
def matplotlib_graphs():
    gender_counts = df['Gender'].value_counts()
    plt.figure(figsize=(6, 4))
    gender_counts.plot(kind='bar', color=['skyblue', 'pink', 'gray'])
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    plt.hist(df['Age'], bins=15, color='purple', edgecolor='white')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    treatment_counts = df['treatment'].value_counts()
    plt.figure(figsize=(6, 4))
    treatment_counts.plot(kind='bar', color='teal')
    plt.title("Seeking Treatment")
    plt.xlabel("Response")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# 4. Seaborn Relationship Exploration
def seaborn_relationships():
    sns.set(style="darkgrid")

    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Gender', hue='treatment')
    plt.title("Treatment by Gender")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x='treatment', y='Age', palette='Set2')
    plt.title("Age by Treatment")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(5, 4))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()

    sns.catplot(data=df, x='work_interfere', hue='treatment', kind='count', height=4, aspect=2)
    plt.title("Work Interfere vs Treatment")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# 🔘 Menu Loop
def main_menu():
    while True:
        print("\n========== Mental Health in Tech Survey ==========")
        print("1. View Dataset Overview")
        print("2. Clean and Show Data Types")
        print("3. Visualize Using Matplotlib")
        print("4. Explore Relationships Using Seaborn")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == '1':
            view_overview()
        elif choice == '2':
            show_types()
        elif choice == '3':
            matplotlib_graphs()
        elif choice == '4':
            seaborn_relationships()
        elif choice == '5':
            print("👋 Exiting... Stay mentally healthy!")
            break
        else:
            print("❌ Invalid input. Try again.")

if __name__ == "__main__":
    main_menu()
