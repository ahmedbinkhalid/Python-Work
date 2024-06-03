# import pandas as pd
#
# # Load the CSV file
# df = pd.read_csv(r'C:\Users\AHMED\Desktop\work_data(Edit).csv')
#
# # Print the initial dataframe
# print("Initial DataFrame:")
# print(df)
#
# # Remove columns that are completely empty
# df = df.dropna(axis=1, how='all')
#
# # Save the updated dataframe back to a CSV file
# df.to_csv('Check_file.csv', index=False)
#
# # Print the updated dataframe
# print("Updated DataFrame:")
# print(df)
# import pandas as pd
# import random
#
# # Load the existing CSV file
# file_path = r'E:\learning python\Check_file.csv'  # Replace with your actual file path
# df = pd.read_csv(file_path)
#
# # Add the new columns with empty values for 'Thumbnail Picture' and random values for 'Reviews'
# df['Thumbnail Picture'] = ''
# df['Reviews'] = [random.randint(1, 5) for _ in range(len(df))]
#
# # Save the updated DataFrame to a new CSV file
# output_file_path = 'DoubleCheck_file.csv'  # Replace with your desired output file path
# df.to_csv(output_file_path, index=False)
#
# print(f"Columns added and reviews populated successfully! Output saved to {output_file_path}")
import csv

# Function to replace empty strings with 'NULL'
def replace_empty_with_null(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for row in rows:
            new_row = ['NULL' if field == '' else field for field in row]
            writer.writerow(new_row)

# Replace 'input.csv' with your input file path and 'output.csv' with your desired output file path
input_file = r'E:\learning python\Check(PN).csv'
output_file = 'Check Final.csv'
replace_empty_with_null(input_file, output_file)

print(f"Empty fields in {input_file} have been replaced with 'NULL' and saved to {output_file}.")
