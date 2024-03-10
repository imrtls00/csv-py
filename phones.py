import pandas as pd
import os

def remove_duplicates(input_file, output_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Print duplicate rows before removing them
    duplicate_rows = df[df.duplicated(subset='Phone Number')]
    print("Duplicate rows being dropped:")
    print(duplicate_rows)

    # Remove duplicate rows based on the phone column
    df.drop_duplicates(subset='Phone Number', inplace=True)

    # Export the cleaned data to the output CSV file
    df.to_csv(output_file, index=False)
    
def merge_csv_files(folder_path, output_file):
    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Check if there are any CSV files in the folder
    if not csv_files:
        print("No CSV files found in the specified folder.")
        return

    # Initialize an empty list to store DataFrames
    dfs = []

    # Loop through each CSV file and read its data into a DataFrame
    for file in csv_files:
        try:
            # Read the CSV file
            df = pd.read_csv(os.path.join(folder_path, file))
            
            # Add a new column with the file name
            df['source_file'] = file
            
            # Append the DataFrame to the list
            dfs.append(df)
        except Exception as e:
            print(f"Error occurred while processing {file}: {str(e)}")
            continue

    # Check if any data was successfully read
    if not dfs:
        print("No data was read. Exiting.")
        return

    # Concatenate all DataFrames in the list
    merged_df = pd.concat(dfs, ignore_index=True)

    # Export the merged data to a new CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged data successfully saved to {output_file}.")

def find_duplicate_phones(input_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Group by 'phone' column and count occurrences
    phone_counts = df['Phone Number'].value_counts()

    # Get the phone numbers with more than two occurrences
    duplicate_phones = phone_counts[phone_counts > 2].index.tolist()

    # Initialize a list to store rows with duplicate phones
    duplicate_rows = []

    # Iterate through the DataFrame and find rows with duplicate phones
    for phone in duplicate_phones:
        duplicate_rows.extend(df[df['Phone Number'] == phone].index.tolist())

    # Print the rows with duplicate phones
    if duplicate_rows:
        print("Rows with duplicate phone numbers:")
        print(df.loc[duplicate_rows])
    else:
        print("No rows with duplicate phone numbers found.")

def remove_rows_with_number(input_file, string_to_remove):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Count the initial number of rows
    initial_rows = len(df)

    # Remove rows containing the number "19" in any column
    df = df[~df.astype(str).apply(lambda x: x.str.contains(string_to_remove)).any(axis=1)]

    # Count the final number of rows
    final_rows = len(df)

    # Calculate the number of rows removed
    rows_removed = initial_rows - final_rows

    # Export the cleaned data to the same CSV file
    df.to_csv(input_file, index=False)

    # Print the number of rows removed and the number of rows left
    print(f"Number of rows removed: {rows_removed}")
    print(f"Number of rows left: {final_rows}")
    
def remove_duplicates_multi_file(cleaned_file, exclude_file, output_file):
    cleaned_data = pd.read_csv(cleaned_file)
    exclude_data = pd.read_csv(exclude_file)
    
    cleaned_data = cleaned_data[~cleaned_data['phone'].isin(exclude_data['phone'])]
    
    cleaned_data.to_csv(output_file, index=False)

def drop_common_rows(file_a, file_b):
    # Read CSV files A and B
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)

    # Drop common rows based on 'phone' column
    common_phones = set(df_a['phone']).intersection(set(df_b['phone']))
    
    print(common_phones)
    
    df_a = df_a[~df_a['phone'].isin(common_phones)]
    df_b = df_b[~df_b['phone'].isin(common_phones)]

    # Save the updated CSV files
    df_a.to_csv(file_a, index=False)
    df_b.to_csv(file_b, index=False)
    


# Usage
cleaned_file = 'cleaned.csv'
exclude_file = 'to_exclude.csv'
output_file = 'ready.csv'

# remove_rows_with_number('Data.csv', '92 315 4314 776')
# drop_common_rows('rasians.csv', 'members.csv')
find_duplicate_phones('Data.csv')
# merge_csv_files('data', 'merged_data.csv')
