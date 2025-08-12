import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('population_data.csv')  # make sure the CSV file name is correct

# Step 2a: Check data types and missing values
print("---- Data Types and Non-null Values ----")
print(df.info())

# Step 2b: Summary statistics
print("\n---- Summary Statistics ----")
print(df.describe(include='all'))  # include='all' to see object (string) columns too

# Step 2c: Count of missing values per column
print("\n---- Missing Values Count ----")
print(df.isnull().sum())

# Step 3: Optional - Look at unique values in a column (e.g., 'Continent')
if 'Continent' in df.columns:
    print("\n---- Unique Continents ----")
    print(df['Continent'].value_counts())  # or df['Continent'].unique()
else:
    print("\nColumn 'Continent' not found.")

# Step 4: Optional - Example for numeric column (e.g., 'Population')
if 'Population (2023)' in df.columns:
    print("\n---- Population Value Counts ----")
    print(df['Population (2023)'].value_counts().head())
else:
    print("\nColumn 'Population (2023)' not found.")
