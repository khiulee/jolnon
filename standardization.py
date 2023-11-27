import pandas as pd

def standardize_column(df, column_name):
    mean_value = df[column_name].mean()
    std_value = df[column_name].std()
    df[column_name] = (df[column_name] - mean_value) / std_value
    return df

def main():
    # Get CSV file path from user input
    file_path = input("Enter CSV file path: ")
    # files/survey_data.csv
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # Get column names from user input
    columns_input = input("Enter Column Names (comma-separated): ")
    # total_commute_minutes,total_sleep_minutes,total_work_minutes,ADQ3E,AQ37_1,AQ37_2,AQ37_3,AQ37_4,AQ37_5
    columns_list = [col.strip() for col in columns_input.split(",")]

    # Check if columns exist in the DataFrame
    for column_name in columns_list:
        if column_name not in df.columns:
            print(f"Error: Column '{column_name}' not found.")
            return

    # Standardize specified columns
    for column_name in columns_list:
        df = standardize_column(df, column_name)

    # Save the standardized DataFrame to a new CSV file
    output_file_path = file_path.replace(".csv", "_standardized.csv")
    df.to_csv(output_file_path, index=False)

    print(f"File saved: {output_file_path}")

if __name__ == "__main__":
    main()
