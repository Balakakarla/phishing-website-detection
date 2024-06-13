import csv
import requests
from features_extraction import FeatureExtraction

# URL of the data feed
url = "https://openphish.com/feed.txt"

# Send a GET request to fetch the data
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Split the text data by newline character to get a list of URLs
    urls = response.text.split("\n")

    # Remove any empty strings from the list
    urls = [url for url in urls if url.strip()]

    # Specify the name of the CSV file
    csv_filename = "phishing_urls.csv"

    # Write the URLs into a CSV file
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
    
        # Write each URL as a row in the CSV file
        for url in urls:
            writer.writerow([url])

    print(f"CSV file '{csv_filename}' has been created successfully.")
else:
    print("Failed to fetch data from the URL.")

# Function to read URLs from a CSV file
def read_urls_from_csv(filename):
    urls = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            urls.append(row[0])  # Assuming the URL is in the first column
    return urls

# Function to write features into a CSV file
def write_features_to_csv(features_list, output_filename):
    with open(output_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'UsingIP','LongURL','ShortURL','Symbol@','Redirecting//','PrefixSuffix-','SubDomains','HTTPS','DomainRegLen','Favicon','NonStdPort','HTTPSDomainURL','RequestURL','AnchorURL','LinksInScriptTags','ServerFormHandler','InfoEmail','AbnormalURL','WebsiteForwarding','StatusBarCust','DisableRightClick','UsingPopupWindow','IframeRedirection','AgeofDomain','DNSRecording','WebsiteTraffic','PageRank','GoogleIndex','LinksPointingToPage','StatsReport'])
        for features in features_list:
            writer.writerow(features)

# Read URLs from the input CSV file
input_csv_filename = "phishing_urls.csv"  # Change this to the filename of your input CSV file
urls = read_urls_from_csv(input_csv_filename)

# Extract features for each URL
features_list = []
for url in urls:
    extractor = FeatureExtraction(url)
    features = [url] + extractor.getFeaturesList()  # Combine URL with extracted features
    features_list.append(features)

# Write the extracted features to a new CSV file
output_csv_filename = "extracted_features.csv"  # Change this to the filename for the output CSV file
write_features_to_csv(features_list, output_csv_filename)

print("Features extracted and saved to", output_csv_filename)
