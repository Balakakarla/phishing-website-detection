import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier, AdaBoostClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.impute import SimpleImputer
import pickle
import csv
# df = pd.read_csv("extracted_features.csv")

# def remove_decimal_and_convert(x):
#     if isinstance(x, float) and x == -1.0:
#         return -1
#     elif isinstance(x, float) and x == 1.0:
#         return 1
#     elif isinstance(x, float) and x == 0.0:
#         return 0
#     return x

# # Apply the function to each element of the DataFrame
# df = df.map(remove_decimal_and_convert)

# # Save the modified DataFrame back to a CSV file
# df.to_csv("extracted_features.csv", index=False)

# def append_csv(existing_csv_path, extra_csv_path, output_csv_path):
#     # Read existing CSV file into a DataFrame
#     existing_df = pd.read_csv(existing_csv_path)

#     # Read extra CSV file into another DataFrame
#     extra_df = pd.read_csv(extra_csv_path)

#     # Append the extra DataFrame to the existing DataFrame
#     combined_df = pd.concat([existing_df, extra_df], ignore_index=True)

#     # Write the combined DataFrame to a new CSV file
#     combined_df.to_csv(output_csv_path, index=False)

# # Example usage:
# existing_csv_path = 'phishing.csv'
# extra_csv_path = 'extracted_features.csv'
# output_csv_path = 'combined.csv'

# append_csv(existing_csv_path, extra_csv_path, output_csv_path)

data=pd.read_csv('C:\\Users\\Bhavitha\\Desktop\\DeployModelProject\\DeployModel\\phishing.csv')


# Impute missing values with the most frequent value
imputer = SimpleImputer(strategy='most_frequent')
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Define features and target variable
X = data_imputed.drop(["class", "Index"], axis=1)
y = data_imputed["class"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid for GridSearchCV
param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.5]
}

# Initialize the Gradient Boosting Classifier
gbc = HistGradientBoostingClassifier()

# Perform GridSearchCV
grid_search = GridSearchCV(gbc, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_
print("Best Parameters:", best_params)

# Train the Gradient Boosting Classifier model with the best parameters
best_gbc = grid_search.best_estimator_
best_gbc.fit(X_train, y_train)

# Predict on the test set
y_pred = best_gbc.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate precision
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

# Calculate recall
recall = recall_score(y_test, y_pred)
print("Recall:", recall)

# Save the trained model as a pickle file
with open('gradient_boosting_model.pkl', 'wb') as f:
    pickle.dump(best_gbc, f)
