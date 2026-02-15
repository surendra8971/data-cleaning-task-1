import pandas as pd

# Load dataset (tab-separated)
df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

object_cols = df.select_dtypes(include=['object']).columns
for col in object_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Convert date column
if "dt_customer" in df.columns:
    df["dt_customer"] = pd.to_datetime(df["dt_customer"], errors='coerce')

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("Cleaning Completed Successfully!")
