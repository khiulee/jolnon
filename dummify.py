import pandas as pd

# Load your CSV file into a DataFrame
file_path = 'files/survey_data_standardized.csv'
df = pd.read_csv(file_path)

# Specify the columns to be dummified
columns_to_dummify = ['gu', 'ADQ3A', 'DEW8']

# Create dummy variables
df_dummies = pd.get_dummies(df, columns=columns_to_dummify, prefix=columns_to_dummify)

# Concatenate the dummy variables with the original DataFrame
df = pd.concat([df, df_dummies], axis=1)

# Drop the original categorical columns if needed
df = df.drop(columns=columns_to_dummify)

# Overwrite the original CSV file with the dummified data
df.to_csv(file_path, index=False)
