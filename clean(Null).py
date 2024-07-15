import pandas as pd

def process_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Replace empty spaces with the string 'null'
    df.replace(r'^\s*$', 'null', regex=True, inplace=True)

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

# Example usage
input_file = 'E:\learning python\works_diff(PN).csv'
output_file = 'Japanese workdiff(uncom).csv'
process_csv(input_file, output_file)
