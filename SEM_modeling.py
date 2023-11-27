import semopy
import pandas as pd

# Load the CSV data into a pandas DataFrame
csv_file_path = 'files/survey_data_standardized.csv.csv'
df = pd.read_csv(csv_file_path)

# Define your structural equation model
model = '''
    # Define observed variables
    commute_time =~ total_commute_minutes 
    sleep_time =~ total_sleep_minutes
    work_time =~ total_work_minutes
    income =~ ADQ3E
    time_with_family =~ AQ37_1 + AQ37_2 + AQ37_3 + AQ37_4 + AQ37_5
    # Define paths
    work_time ~ a_1*commute_time
    sleep_time ~ r*work_time +a_2*commute_time
    income ~ b_1*sleep_time +b_2*time_with_family+c*commute_time 
    
'''

# Create a semopy model
model_object = semopy.Model(model)

# Fit the model to the data
fit = model_object.fit(df)

# Print the results
# Access fit indices
print(fit)
print(fit.x)