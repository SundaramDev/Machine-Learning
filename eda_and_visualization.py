import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
df = pd.read_csv("population_data.csv")
print("Columns in the dataset:")
print(df.columns)

# -------------------------------
# 1. Bar Chart – Top 10 Countries
# -------------------------------
top10 = df.sort_values(by='Population 2025', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x='Country (or dependency)', y='Population 2025')
plt.title('Top 10 Countries by Population (2025)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_population.png")
plt.show()

# ---------------------------------------
# 2. Pie Chart – Countries per Continent
# ---------------------------------------
continent_counts = df['Continent'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(continent_counts, labels=continent_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Countries per Continent')
plt.axis('equal')
plt.tight_layout()
plt.savefig('countries_per_continent.png')
plt.show()

# -----------------------------------------
# 3. Histogram – Population Distribution
# -----------------------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df['Population 2025'], bins=30, kde=True)
plt.title('Population Distribution (2025)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.savefig('population_distribution.png')
plt.show()

# -------------------------------
# 4. Box Plot – Population by Continent
# -------------------------------
plt.figure(figsize=(12, 6))
sns.boxplot(x='Continent', y='Population 2025', data=df)
plt.title('Population Spread by Continent (2025)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('population_boxplot.png')
plt.show()
