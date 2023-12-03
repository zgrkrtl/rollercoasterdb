import pandas as pd

# Load the Excel file
file_path = 'coaster_db.xlsx'
df = pd.read_excel(file_path)

# Function to convert 'MM:SS' format to seconds
def convert_to_seconds(time_str):
    if isinstance(time_str, str) and ':' in time_str:
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    else:
        return time_str

# Apply the conversion function to the specific column
df['Duration(s)'] = df['Duration(s)'].apply(convert_to_seconds)

# Save the updated DataFrame back to Excel
df.to_excel('updated_file.xlsx', index=False)
