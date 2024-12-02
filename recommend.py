import pandas as pd
import numpy as np
import pickle
from scipy.sparse import hstack, csr_matrix
import os

# Define paths
MODELS_DIR = 'models'
DATA_PATH = 'data/movie_data.csv'

MODEL_PATH = os.path.join(MODELS_DIR, 'knn_model.pkl')
MLB_GENRES_PATH = os.path.join(MODELS_DIR, 'mlb_genres.pkl')
MLB_DIRECTORS_PATH = os.path.join(MODELS_DIR, 'mlb_directors.pkl')
MLB_ACTORS_PATH = os.path.join(MODELS_DIR, 'mlb_actors.pkl')

# Function to load pickle files
def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Load the serialized model and encoders
def load_models():
    knn_model = load_pickle(MODEL_PATH)
    mlb_genres = load_pickle(MLB_GENRES_PATH)
    mlb_directors = load_pickle(MLB_DIRECTORS_PATH)
    mlb_actors = load_pickle(MLB_ACTORS_PATH)
    return knn_model, mlb_genres, mlb_directors, mlb_actors

knn_model, mlb_genres, mlb_directors, mlb_actors = load_models()

# Load the dataset
def load_data():
    df = pd.read_csv(DATA_PATH)
    # Function to split strings based on a delimiter and strip whitespace
    def split_and_strip(text, delimiter):
        if isinstance(text, str):
            return [item.strip() for item in text.split(delimiter)]
        return []
    
    # Split and clean the genres, director, and actors columns
    df['genres'] = df['genres'].apply(lambda x: split_and_strip(x, ','))
    df['director'] = df['director'].apply(lambda x: split_and_strip(x, ','))
    df["actors"] = df["actors"].apply(lambda x: split_and_strip(x, ','))
    return df

df = load_data()

# Compute the feature matrix with weights
def compute_feature_matrix(df, mlb_genres, mlb_directors, mlb_actors):
    genres_encoded = mlb_genres.transform(df['genres'])
    directors_encoded = mlb_directors.transform(df['director'])
    actors_encoded = mlb_actors.transform(df['actors'])
    
    # Define weights
    weight_genres = 1.5
    weight_actors = 1.2
    weight_directors = 1.1
    
    # Apply weights
    genres_sparse = csr_matrix(genres_encoded * weight_genres)
    directors_sparse = csr_matrix(directors_encoded * weight_directors)
    actors_sparse = csr_matrix(actors_encoded * weight_actors)
    
    # Combine
    feature_matrix = hstack([genres_sparse, directors_sparse, actors_sparse])
    return feature_matrix

feature_matrix = compute_feature_matrix(df, mlb_genres, mlb_directors, mlb_actors)

# Recommendation Function
def recommend_movies(user_ratings, df, feature_matrix, knn_model, top_n=5):
    """
    Recommend movies based on user ratings.

    Parameters:
    - user_ratings: List of tuples [(movieId, rating), ...]
    - df: The DataFrame.
    - feature_matrix: The combined feature matrix.
    - knn_model: The trained KNN model.
    - top_n: Number of recommendations to return.

    Returns:
    - DataFrame of recommended movies.
    """
    if not user_ratings:
        raise ValueError("No user ratings provided.")
    
    # Create a DataFrame from user ratings
    user_df = pd.DataFrame(user_ratings, columns=['movieId', 'rating'])
    avg_rating = user_df['rating'].mean()

    # Select movies rated >= average
    selected_movies = user_df[user_df['rating'] >= avg_rating]['movieId']
    if selected_movies.empty:
        raise ValueError("No movies rated above or equal to the average rating.")
    
    # Get indices of the selected movies
    selected_indices = df[df["movieId"].isin(selected_movies)].index
    if selected_indices.empty:
        raise ValueError("No matching movies found for the provided movieIds.")
    
    # Extract feature vectors for the selected movies
    selected_features = feature_matrix[selected_indices]
    
    # Compute the mean feature vector to represent the user profile
    user_profile = selected_features.mean(axis=0)
    user_profile = np.asarray(user_profile)  # Convert to numpy array
    
    # Find nearest neighbors to the user profile
    distances, indices = knn_model.kneighbors(user_profile, n_neighbors=top_n + len(selected_movies))

    # Flatten indices and distances
    indices = indices.flatten()
    distances = distances.flatten()

    # Create a DataFrame of potential recommendations
    recommendations = df.iloc[indices].copy()
    recommendations["distance"] = distances

    # Exclude movies already rated by the user
    user_rated_ids = user_df["movieId"].tolist()
    recommendations = recommendations[~recommendations["movieId"].isin(user_rated_ids)]

    # Drop duplicates and sort by distance 
    recommendations = recommendations.drop_duplicates(subset='movieId').sort_values('distance')  # sort by distance for most to least similar

    return recommendations.head(top_n)
