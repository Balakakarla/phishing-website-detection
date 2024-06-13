import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv("extracted_features.csv")

# Drop the 'URL' column
df.drop(columns=['URL'], inplace=True)

# Save the DataFrame back to a CSV file
df.to_csv("extracted_features.csv", index=False)

def add_class_column(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Add the "Class" column with value -1 to the DataFrame
    df['class'] = 1

    # Write the modified DataFrame back to the original CSV file
    df.to_csv(file_path, index=False)

def add_index_column(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Add the "Index" column with values starting from 0 and incrementing by 1 for each row
    df.insert(0, 'Index', range(11054, 11054 + len(df)))

    # Write the modified DataFrame back to the original CSV file
    df.to_csv(file_path, index=False)

file_path = 'extracted_features.csv'

add_class_column(file_path)
add_index_column(file_path)
