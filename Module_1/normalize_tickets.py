import pandas as pd
import re

# Load the dataset
df = pd.read_csv('customer_support_data.csv')
print(df.head())

#"Ticket ID" to "ticket_id"
df.columns = [col.lower().replace(' ', '_').strip() for col in df.columns]
print("New Columns:", df.columns)

# Fill 'NaN' (Not a Number/Empty) with "No description provided"
df['ticket_description'] = df['ticket_description'].fillna('no description')

# Create a dictionary of 'Wrong Name': 'Right Name'
status_map = {
    'Pending': 'OPEN',
    'Open': 'OPEN',
    'Resolved': 'CLOSED',
    'Closed': 'CLOSED'
}

# Apply the map to the status column
df['ticket_status'] = df['ticket_status'].map(status_map)

def clean_text(text):
    text = text.lower() # Make everything lowercase
    text = re.sub(r'[^a-z0-9\s]', '', text) # Remove special characters like @, #, !
    text = text.strip() # Remove extra spaces at start/end
    return text

# Apply this function to the description column
df['ticket_description'] = df['ticket_description'].apply(clean_text)

# 1. Print the first few rows to see the new cleaned data
print("--- CLEANED DATA SNEAK PEEK ---")
print(df[['ticket_id', 'ticket_status', 'ticket_description']].head())

# 2. Check how many of each status we have now
print("\n--- STATUS COUNTS ---")
print(df['ticket_status'].value_counts())

# 3. Save your hard work to a new file so you can use it later
df.to_csv('cleaned_support_data.csv', index=False)
print("\nSuccess! Your cleaned data has been saved to 'cleaned_support_data.csv'.")
