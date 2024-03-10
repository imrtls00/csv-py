import pandas as pd

def update_member_teams(members_file, data_file):
    # Read Members.csv and Data.csv
    members_df = pd.read_csv(members_file)
    data_df = pd.read_csv(data_file)

    # Iterate through each row in Members.csv
    for index, member_row in members_df.iterrows():
        # Get the phone number of the current member
        phone_number = member_row['Phone Number']
        
        # Find matching row in Data.csv based on phone number
        matching_row = data_df[data_df['Phone Number'] == phone_number]
        
        # If a matching row is found
        if not matching_row.empty:
            # Get the team names from the matching row
            primary_team = matching_row.iloc[0]['Team Name']
            secondary_team = None
            if len(matching_row) > 1:
                secondary_team = matching_row.iloc[1]['Team Name']

            # Update the Primary Team and Secondary Team columns in Members.csv
            members_df.loc[index, 'Primary Team'] = primary_team
            members_df.loc[index, 'Secondary Team'] = secondary_team

            # Drop the matched row(s) from Data.csv
            data_df = data_df[data_df['Phone Number'] != phone_number]

    # Save the updated Members.csv and Data.csv
    members_df.to_csv('updated_members.csv', index=False)
    data_df.to_csv('updated_data.csv', index=False)

# Usage example
members_file = 'Members.csv'
data_file = 'Data.csv'
update_member_teams(members_file, data_file)
