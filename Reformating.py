# # import pandas as pd
# #
# # def make_columns_adjacent(input_file, output_file):
# #     # Read the Excel file
# #     df = pd.read_excel(input_file)
# #
# #     # Drop columns that are entirely empty
# #     df = df.dropna(axis=1, how='all')
# #
# #     # Rearrange columns to be adjacent (in the order they appear)
# #     columns = df.columns.tolist()
# #     df = df[columns]
# #
# #     # Write the new DataFrame to a new Excel file
# #     df.to_excel(output_file, index=False)
# #
# # # Example usage
# # input_file = r'E:\learning python\japanese adjacent.xlsx'
# # output_file = 'output_japanese.xlsx'
# # make_columns_adjacent(input_file, output_file)
# import pandas as pd
#
# # Load the Excel file
# input_file = r'E:\learning python\japanese adjacent.xlsx'
# output_file = 'Check_Japanese.xlsx'
# df = pd.read_excel(input_file)
#
# # Print the initial dataframe
# print("Initial DataFrame:")
# print(df)
#
# # Remove columns that are completely empty
# df = df.dropna(axis=1, how='all')
#
# # Save the updated dataframe back to an Excel file
# df.to_excel(output_file, index=False)
#
# # Print the updated dataframe
# print("Updated DataFrame:")
# print(df)
import pandas as pd

def retain_first_six_columns(input_file, output_file):
    # Load the Excel file
    df = pd.read_excel(input_file)

    # Print the initial dataframe
    print("Initial DataFrame:")
    print(df)

    # Retain only the first six columns
    df = df.iloc[:, :6]

    # Save the updated dataframe back to an Excel file
    df.to_excel(output_file, index=False)

    # Print the updated dataframe
    print("Updated DataFrame:")
    print(df)

# Example usage
input_file = r'E:\learning python\Check_Japanese.xlsx'
output_file = 'Check_file(Updated japanese).xlsx'
retain_first_six_columns(input_file, output_file)
