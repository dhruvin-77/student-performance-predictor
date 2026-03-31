import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("data/student.csv")

# Select features
df = df[['studytime', 'failures', 'absences', 'G1', 'G2',
         'health', 'freetime', 'goout', 'Medu', 'Fedu', 'G3']]

# Split data
X = df.drop('G3', axis=1)
y = df['G3']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model
import joblib
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")