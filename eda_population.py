import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("population_data.csv")

# Print column names to verify
print("Available columns:")
print(df.columns)

# Optionally: Strip all column names of extra spaces
df.columns = df.columns.str.strip()

# Check again after strip
print("Stripped column names:")
print(df.columns)

# Replace these column names with the correct ones from your CSV
# You may need to adjust these if your file has different headers
cols_to_convert = [
    'Population (2020)',
    'Yearly Change',
    'Net Change',
    'Density (P/Km²)',
    'Land Area (Km²)'
]

# Safely convert columns to numeric (with protection)
for col in cols_to_convert:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace('%', '').str.replace(',', ''), errors='coerce')
    else:
        print(f"Warning: Column '{col}' not found in data!")

# Display dataset info
print(df.info())
print(df.describe())

# --- Visualization 1: Top 10 most populated countries ---
if 'Population (2020)' in df.columns:
    top10 = df.sort_values('Population (2020)', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Population (2020)', y='Country (or dependency)', data=top10)
    plt.title("Top 10 Most Populated Countries (2020)")
    plt.tight_layout()
    plt.savefig("top10_population.png")

    plt.show()
else:
    print("Skipping population plot – 'Population (2020)' not found")

# --- Visualization 2: Population Density distribution ---
if 'Density (P/Km²)' in df.columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Density (P/Km²)'].dropna(), bins=30, kde=True)
    plt.title("Population Density Distribution")
    plt.xlabel("Density (P/Km²)")
    plt.tight_layout()
    plt.savefig("density_distribution.png")
    plt.show()
else:
    print("Skipping density plot – 'Density (P/Km²)' not found")
