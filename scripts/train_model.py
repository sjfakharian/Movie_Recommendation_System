# scripts/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
from scripts.data_preprocessing import load_and_clean_data

def train_and_save_model():
    df = load_and_clean_data("data/movie_ratings.csv")
    
    # For demonstration, we assume that the dataset contains a 'user_id' column and a 'rating' column.
    # We'll use 'user_id' as the sole feature (this is a placeholder – in a real system you'd use more features).
    X = df[['user_id']]
    y = df["rating"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    print("The model R2 score is", score)
    
    # Save the trained model to a file
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved as model.pkl")

if __name__ == "__main__":
    train_and_save_model()
