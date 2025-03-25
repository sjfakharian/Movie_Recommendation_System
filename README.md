
# Movie Recommendation System

This repository contains a simple movie recommendation system built using Python. The project leverages the MovieLens dataset from [MovieLens](https://grouplens.org/datasets/movielens/), which consists of over 20 million ratings of more than 50,000 movies by over 270,000 users.

## Project Structure

```
movie-recommendation/
├── data/
│   └── movie_ratings.csv        # Place your MovieLens ratings file here
├── scripts/
│   ├── data_preprocessing.py    # Script to load and clean the data
│   ├── train_model.py           # Script to train the LinearRegression model
│   └── recommend.py             # Script to recommend movies based on the model's prediction
├── requirements.txt             # List of dependencies
└── README.md                    # Project description and instructions
```

## How to Run the Project

1. **Data Preparation:**  
   Place your MovieLens ratings CSV (e.g., `movie_ratings.csv`) in the `data/` folder.

2. **Data Preprocessing:**  
   Run the following command to load and clean the dataset:
   ```bash
   python scripts/data_preprocessing.py
   ```

3. **Train the Model:**  
   Train the LinearRegression model using the cleaned data and save the model:
   ```bash
   python scripts/train_model.py
   ```

4. **Get Movie Recommendations:**  
   Use the trained model to recommend movies for a specific user:
   ```bash
   python scripts/recommend.py
   ```

## Project Overview

- **Data Preprocessing:** Loads the dataset and removes any missing or invalid values.
- **Model Training:** Splits the dataset into training and test sets, then trains a LinearRegression model to predict movie ratings based solely on user IDs (this is for demonstration purposes).
- **Recommendations:** The model is used to predict a rating for a given user, and a dummy list of movies is provided as recommendations.

## Acknowledgements

A big thank you to the [MovieLens](https://grouplens.org/datasets/movielens/) team for providing such a valuable dataset. Their contributions have enabled countless data scientists to build innovative recommendation systems.

For the complete code and detailed instructions, please visit my GitHub repository.

Happy recommending!
