import pandas as pd
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('coaster_db.csv')

# Function to extract the numerical value before the 'Â' symbol
def extract_length(row):
    if isinstance(row, str):  # Check if the entry is a string
        # Split the string by 'Â', take the first part, and extract the numerical value
        return row.split('Â')[0].split()[0]
    return np.nan  # Return NaN for non-string entries (floats, NaN, etc.)

# Apply the function to the 'Length' column for non-null entries
df['Length'] = df['Length'].apply(lambda x: extract_length(x) if pd.notnull(x) else x)

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_file.csv', index=False)
