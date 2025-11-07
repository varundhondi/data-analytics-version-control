import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# 1. Handle Missing Values
# Fill missing numerical values with the mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing categorical values with the mode
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 2. Remove Duplicates
df.drop_duplicates(inplace=True)

# 3. Convert Data Types
# Convert date columns to datetime
date_columns = ['date_column_name']  # Replace with your actual column names
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Convert categorical columns to category type
categorical_columns = ['category_column_name']  # Replace with your actual column names
for col in categorical_columns:
    df[col] = df[col].astype('category')

# 4. Handle Outliers (Example: Capping numerical outliers)
for col in df.select_dtypes(include=['float', 'int']).columns:
    upper_limit = df[col].quantile(0.95)
    lower_limit = df[col].quantile(0.05)
    df[col] = np.clip(df[col], lower_limit, upper_limit)

# 5. Standardize Column Names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)

print("Data cleaning completed and saved as 'cleaned_dataset.csv'")
