import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("flood_data.csv")

x = df[['distance', 'flow']]
y = df["label"]

X_train, X_test, Y_train, Y_test = train_test_split(x,y)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

print("Accuracy:", model.score(X_test, Y_test))

print("Dumping model")
joblib.dump(model, "flood_model.pkl")
