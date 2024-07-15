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
    input_file = r'E:\Mangaseek.net\Japanese\1.Person_List(Japanese).csv'
    output_file = "confirm_file.csv"
    translate_japanese_to_english(input_file, output_file)
