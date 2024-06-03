# import pandas as pd
# from googletrans import Translator
# import time
#
# def translate_japanese_to_english(input_file, output_file):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(input_file)
#
#     # Initialize Google Translator
#     translator = Translator()
#
#     # Function to translate Japanese text to English with retry
#     def translate_text_with_retry(text, retries=3):
#         for _ in range(retries):
#             try:
#                 translated_text = translator.translate(text, src='ja', dest='en').text
#                 return translated_text
#             except Exception as e:
#                 print(f"Error translating text: {e}")
#                 print("Retrying after 1 second...")
#                 time.sleep(1)
#         # If all retries fail, return original text
#         return text
#
#     # Apply translation to all columns
#     df = df.apply(lambda x: x.apply(lambda y: translate_text_with_retry(y) if isinstance(y, str) else y))
#
#     # Save the translated DataFrame to a new CSV file
#     df.to_csv(output_file, index=False)
#
# if __name__ == "__main__":
#     input_file = r"E:\learning python\person_dataaaaa(sa).csv"  # Specify the input CSV file
#     output_file = "outputdata(sa).csv"  # Specify the output CSV file
#     translate_japanese_to_english(input_file, output_file)

# import pandas as pd
# from googletrans import Translator
# import time
#
# def translate_japanese_to_english(input_file, output_file):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(input_file)
#
#     # Initialize Google Translator
#     translator = Translator()
#
#     # Function to translate Japanese text to English with retry
#     def translate_text_with_retry(text, retries=3):
#         for _ in range(retries):
#             try:
#                 translated_text = translator.translate(text, src='ja', dest='en').text
#                 return translated_text
#             except Exception as e:
#                 print(f"Error translating text: {e}")
#                 print("Retrying after 1 second...")
#                 time.sleep(1)
#         # If all retries fail, return original text
#         return text
#
#     # Apply translation to all elements in the DataFrame using map
#     df = df.map(lambda y: translate_text_with_retry(y) if isinstance(y, str) else y)
#
#     # Save the translated DataFrame to a new CSV file
#     df.to_csv(output_file, index=False)
#
# if __name__ == "__main__":
#     input_file = r"E:\learning python\person_dataaaaa(sa).csv"  # Specify the input CSV file
#     output_file = "outputdata(sa).csv"  # Specify the output CSV file
#     translate_japanese_to_english(input_file, output_file)
# import pandas as pd
# from googletrans import Translator
# import time
#
# def translate_japanese_to_english(input_file, output_file):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(input_file)
#
#     # Initialize Google Translator
#     translator = Translator()
#
#     # Function to translate Japanese text to English with retry
#     def translate_text_with_retry(text, retries=3):
#         if pd.isnull(text) or not isinstance(text, str) or not text.strip():
#             return text
#         for _ in range(retries):
#             try:
#                 translated_text = translator.translate(text, src='ja', dest='en').text
#                 return translated_text
#             except Exception as e:
#                 print(f"Error translating text: {e}")
#                 print("Retrying after 1 second...")
#                 time.sleep(1)
#         # If all retries fail, return original text
#         return text
#
#     # Apply translation to all elements in the DataFrame using map
#     df = df.applymap(translate_text_with_retry)
#
#     # Save the translated DataFrame to a new CSV file
#     df.to_csv(output_file, index=False)
#
# if __name__ == "__main__":
#     input_file = r"E:\learning python\work_data.csv"  # Specify the input CSV file
#     output_file = "work(sa).csv"  # Specify the output CSV file
#     translate_japanese_to_english(input_file, output_file)
import pandas as pd
from deep_translator import GoogleTranslator
import time
from multiprocessing import Pool, cpu_count
import numpy as np
import csv

# Initialize Google Translator from deep-translator
translator = GoogleTranslator(source='ja', target='en')

def translate_text_with_retry(text, retries=3):
    if pd.isnull(text) or not isinstance(text, str) or not text.strip():
        return text
    for attempt in range(retries):
        try:
            translation = translator.translate(text)
            print(f"Attempt {attempt + 1}: Translation result: {translation}")
            if translation:
                return translation
            else:
                raise ValueError("Translation result is None or empty")
        except Exception as e:
            print(f"Error translating text: {e} on attempt {attempt + 1}")
            time.sleep(1)
    return text

def translate_chunk(df_chunk):
    for column in df_chunk.columns:
        df_chunk[column] = df_chunk[column].map(lambda y: translate_text_with_retry(y) if isinstance(y, str) else y)
    return df_chunk

def count_columns(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        first_row = next(reader)
        return len(first_row)

def translate_japanese_to_english(input_file, output_file):
    num_columns = count_columns(input_file)

    try:
        df = pd.read_csv(input_file, usecols=range(num_columns), on_bad_lines='skip')
    except pd.errors.ParserError as e:
        print(f"Error reading the CSV file: {e}")
        return

    num_chunks = cpu_count()
    df_chunks = np.array_split(df, num_chunks)

    with Pool(num_chunks) as pool:
        translated_chunks = pool.map(translate_chunk, df_chunks)

    translated_df = pd.concat(translated_chunks)
    translated_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = r'E:\learning python\works_diff(PN).csv'
    output_file = "works_dff(Complete).csv"
    translate_japanese_to_english(input_file, output_file)
# import pandas as pd
# from deep_translator import GoogleTranslator
# import time
# from multiprocessing import Pool, cpu_count
# import numpy as np
# import csv
# import os
#
# # Initialize Google Translator from deep-translator
# translator = GoogleTranslator(source='ja', target='en')
#
# def translate_text_with_retry(text, retries=3):
#     if pd.isnull(text) or not isinstance(text, str) or not text.strip():
#         return text
#     for attempt in range(retries):
#         try:
#             translation = translator.translate(text)
#             print(f"Attempt {attempt + 1}: Translation result: {translation}")
#             if translation:
#                 return translation
#             else:
#                 raise ValueError("Translation result is None or empty")
#         except Exception as e:
#             print(f"Error translating text: {e} on attempt {attempt + 1}")
#             time.sleep(1)
#     return text
#
# def translate_chunk(df_chunk, start_index, end_index):
#     for i in range(start_index, end_index):
#         for column in df_chunk.columns:
#             df_chunk.at[i, column] = translate_text_with_retry(df_chunk.at[i, column])
#     return df_chunk
#
# def count_columns(input_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         first_row = next(reader)
#         return len(first_row)
#
# def translate_japanese_to_english(input_file, output_file):
#     num_columns = count_columns(input_file)
#
#     try:
#         df = pd.read_csv(input_file, usecols=range(num_columns), on_bad_lines='skip')
#     except pd.errors.ParserError as e:
#         print(f"Error reading the CSV file: {e}")
#         return
#
#     num_chunks = cpu_count()
#     chunk_size = len(df) // num_chunks
#     df_chunks = [df.iloc[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
#
#     with Pool(num_chunks) as pool:
#         for i, df_chunk in enumerate(df_chunks):
#             start_index = i * chunk_size
#             end_index = min((i + 1) * chunk_size, len(df))
#             translated_chunk = translate_chunk(df_chunk, start_index, end_index)
#             translated_chunk.to_csv(output_file, mode='a', header=False, index=False)
#
# if __name__ == "__main__":
#     input_file = r'E:\learning python\work_data(all).csv'
#     output_file = "work_data(list).csv"
#
#     # Check if the output file exists
#     if os.path.exists(output_file):
#         # If the output file exists, read the last translated row
#         try:
#             df = pd.read_csv(output_file)
#             last_translated_row = len(df)
#             print(f"Resuming translation from row {last_translated_row + 1}")
#         except pd.errors.EmptyDataError:
#             last_translated_row = 0
#     else:
#         last_translated_row = 0
#
#     # Translate the data and append to the output file
#     translate_japanese_to_english(input_file, output_file)
