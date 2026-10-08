
import pandas as pd

# Read the messy dataset
df = pd.read_csv("messy_sales_data.csv")

print("===== ORIGINAL DATA =====")
print(df)

# Identify missing values
print("\nMissing values:")
print(df.isnull().sum())

# Identify duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Identify invalid numbers
print("\nInvalid prices:", (df["Price"] <= 0).sum())
print("Invalid quantities:", (df["Quantity"] <= 0).sum())


# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing important values
df = df.dropna(
    subset=["Product", "Price", "Quantity", "Date"]
)

print("\n===== AFTER BASIC CLEANING =====")
print(df)

# Keep only positive prices and quantities
df = df[
    (df["Price"] > 0) &
    (df["Quantity"] > 0)
].copy()

# Calculate revenue
df["Revenue"] = df["Price"] * df["Quantity"]

print("\n===== CLEANED DATA =====")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned data saved successfully!")

