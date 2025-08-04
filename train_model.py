import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("rainfall_india.csv")



# Filter Karnataka regions
df = df[df['SUBDIVISION'].str.contains("Karnataka", case=False, na=False)]

# Drop rows with missing monthly data
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
          'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
df.dropna(subset=months, inplace=True)

# Calculate annual rainfall
df['Annual'] = df[months].sum(axis=1)

# Features and target
X = df[['YEAR']]
y = df['Annual']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("rainfall_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as rainfall_model.pkl")
