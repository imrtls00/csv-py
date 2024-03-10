import pandas as pd

def remove_duplicate_emails(input_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Get the initial number of rows
    initial_rows = len(df)

    # Remove duplicate rows based on the 'Emails' column
    df.drop_duplicates(subset='Emails', inplace=True)

    # Get the final number of rows
    final_rows = len(df)

    # Calculate the number of rows dropped
    rows_dropped = initial_rows - final_rows

    # Export the cleaned data to the same CSV file
    df.to_csv(input_file, index=False)

    # Print the total number of rows dropped and the total number of rows left
    print(f"Total rows dropped: {rows_dropped}")
    print(f"Total rows left: {final_rows}")

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

# Usage example
# remove_duplicate_emails('emails.csv')
remove_rows_with_number('emails.csv', '16')
