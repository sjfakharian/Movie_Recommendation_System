# scripts/data_preprocessing.py

import pandas as pd

def load_and_clean_data(filepath="data/movie_ratings.csv"):
    # Load the MovieLens dataset
    ratings_df = pd.read_csv(filepath)
    
    # Clean the dataset: remove missing values
    ratings_df.dropna(inplace=True)
    
    return ratings_df

if __name__ == "__main__":
    df = load_and_clean_data()
    print("Data loaded and cleaned. Sample:")
    print(df.head())
