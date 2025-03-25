# scripts/recommend.py

import pickle

def load_model(model_path="model.pkl"):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

def recommend_movies(user_id):
    # Load the trained model
    model = load_model()
    
    # Use the model to predict a rating for the user.
    # (This is a dummy prediction. In a real scenario, you would have a more advanced recommendation logic.)
    prediction = model.predict([[user_id]])
    
    # Dummy recommended movies list (this should be generated using more sophisticated logic)
    recommended_movies = [
        "The Shawshank Redemption (1994)",
        "The Godfather (1972)",
        "The Dark Knight (2008)"
    ]
    
    print(f"\nThe following movies are recommended for user {user_id}:")
    for movie in recommended_movies:
        print(movie)
    print(f"\nPredicted rating for user {user_id} is: {prediction[0]:.2f}")

if __name__ == "__main__":
    # Example: Recommend movies for user with ID 1
    user_id = 1
    recommend_movies(user_id)
