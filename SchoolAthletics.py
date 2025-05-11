import pandas as pd

# Load the dataset
df = pd.read_csv("SchoolData.csv")

# Fill missing values with defaults
df_cleaned = df.fillna({
    "Age": 0,                      # Default age
    "Height (cm)": 0,              # Default height
    "School": "Unknown"            # Default school name
})

#Save the cleaned data to a new CSV
df_cleaned.to_csv("SchoolData_Cleaned.csv", index=False)

# Convert columns to numeric (in case there are empty strings or non-numeric values)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Height (cm)"] = pd.to_numeric(df["Height (cm)"], errors="coerce")
df["Grade"] = pd.to_numeric(df["Grade"], errors="coerce")

# Calculate the mean values
mean_age = df["Age"].mean()
mean_height = df["Height (cm)"].mean()
mean_grade = df["Grade"].mean()

# Display the results
print(f"Mean Age: {mean_age:.2f}")
print(f"Mean Height: {mean_height:.2f} cm")
print(f"Mean Grade: {mean_grade:.2f}")

import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the dataset
df = pd.read_csv("SchoolData.csv")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Grade"] = pd.to_numeric(df["Grade"], errors="coerce")

# Filter data for each school
sunrise = df[df["School"] == "Sunrise Academy"]
greenwood = df[df["School"] == "Greenwood High"]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(sunrise["Age"], sunrise["Grade"], marker='o', label="Sunrise Academy")
plt.plot(greenwood["Age"], greenwood["Grade"], marker='s', label="Greenwood High")

plt.title("Age vs Grade: Sunrise Academy vs Greenwood High")
plt.xlabel("Age")
plt.ylabel("Grade")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the dataset
df = pd.read_csv("SchoolData.csv")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Height (cm)"] = pd.to_numeric(df["Height (cm)"], errors="coerce")
df["Grade"] = pd.to_numeric(df["Grade"], errors="coerce")

# Set the index to 'Name' for better labeling in the graph
df.set_index('Name', inplace=True)

# Plotting
df[['Age', 'Height (cm)', 'Grade']].plot(kind='bar', figsize=(10, 6))

# Title and labels
plt.title("Grade, Age, and Height of Students")
plt.xlabel("Students")
plt.ylabel("Values")

# Display the chart
plt.tight_layout()
plt.show()