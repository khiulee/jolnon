import pandas as pd

# Load your CSV data into a pandas DataFrame
csv_file_path = 'files/survey_data.csv'
df = pd.read_csv(csv_file_path)

# Create a new column 'total_commute_minutes' using the formula 60 * AQ10C_1 + AQ10C_2
df['total_work_minutes'] = 60 * df['ADQ3B_1'] + df['ADQ3B_2']

# Drop the original AQ10C_1 and AQ10C_2 columns
df = df.drop(['ADQ3B_1', 'ADQ3B_2'], axis=1)

# Save the updated DataFrame to the original CSV file, overwriting it
df.to_csv(csv_file_path, index=False)

print(f"DataFrame updated. Original CSV file updated at: {csv_file_path}")
