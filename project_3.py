import pandas as pd
import numpy as np

# Start coding here...

# Read in csv
df = pd.read_csv("bank_marketing.csv")

# Clean job column
df['job'] = df['job'].str.replace(".","_")

# Clean education column
df['education'] = df['education'].str.replace(".","_")
df.loc[df['education'] == "unknown", 'education'] = np.nan

# Clean and convert credit_default columns to bool data type
df.loc[df['credit_default'] == "yes", 'credit_default'] = 1
df.loc[df['credit_default'] != 1, 'credit_default'] = 0
df['credit_default'] = df['credit_default'].astype('bool')

# Clean and convert mortgage columns to bool data type
df.loc[df['mortgage'] == "yes", 'mortgage'] = 1
df.loc[df['mortgage'] != 1, 'mortgage'] = 0
df['mortgage'] = df['mortgage'].astype('bool')

# Clean and convert previous_outcome columns to bool data type
df.loc[df['previous_outcome'] == "success", 'previous_outcome'] = 1
df.loc[df['previous_outcome'] != 1, 'previous_outcome'] = 0
df['previous_outcome'] = df['previous_outcome'].astype('bool')

# Clean and convert campaign_outcome columns to bool data type
df.loc[df['campaign_outcome'] == "yes", 'campaign_outcome'] = 1
df.loc[df['campaign_outcome'] != 1, 'campaign_outcome'] = 0
df['campaign_outcome'] = df['campaign_outcome'].astype('bool')

# Add year column
df['year'] = "2022"
# Convert day to string and add last_contact_date column
date = df['year'] + "-" + df['month'] + "-" + df['day'].astype("str")
df['last_contact_date'] = pd.to_datetime(date)
# Convert to datetime
df['last_contact_date'] = df['last_contact_date'].dt.strftime("%y-%m-%d")

# Split into the three tables
client = df[['client_id','age','job','marital','education','credit_default','mortgage']]
campaign = df[['client_id','number_contacts','contact_duration','previous_campaign_contacts',
               'previous_outcome','campaign_outcome','last_contact_date']]
economics = df[['client_id','cons_price_idx','euribor_three_months']]

# Save tables to individual csv files
client.to_csv("client.csv", index = False)
campaign.to_csv("campaign.csv", index = False)
economics.to_csv("economics.csv", index = False)

