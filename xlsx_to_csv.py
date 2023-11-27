import pandas as pd
import openpyxl

# Replace 'files/2022 서울서베이_가구원조사(공개용).xlsx' with your actual Excel file path
excel_file_path = 'files/2022 서울서베이_가구원조사(공개용).xlsx'

# Read the first sheet of the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path, sheet_name=0)

# Replace 'output_file.csv' with the desired name for your CSV file
csv_file_path = 'files/survey_data.csv'

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Conversion successful. CSV file saved at: {csv_file_path}")