import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import hstack, csr_matrix
import pickle
import os

# Define paths
DATA_PATH = 'data/movie_data.csv'
MODELS_DIR = 'models'
MODEL_PATH = os.path.join(MODELS_DIR, 'knn_model.pkl')
MLB_GENRES_PATH = os.path.join(MODELS_DIR, 'mlb_genres.pkl')
MLB_DIRECTORS_PATH = os.path.join(MODELS_DIR, 'mlb_directors.pkl')
MLB_ACTORS_PATH = os.path.join(MODELS_DIR, 'mlb_actors.pkl')

# Ensure models directory exists
os.makedirs(MODELS_DIR, exist_ok=True)

# Load the dataset
movie_data = pd.read_csv(DATA_PATH)
df = pd.DataFrame(movie_data)

# Function to split strings based on a delimiter and strip whitespace
def split_and_strip(text, delimiter):
    if isinstance(text, str):  # Check if text is a string
        return [item.strip() for item in text.split(delimiter)]
    return []

# Split and clean the genres, director, and actors columns
df['genres'] = df['genres'].apply(lambda x: split_and_strip(x, ','))
df['director'] = df['director'].apply(lambda x: split_and_strip(x, ','))
df["actors"] = df["actors"].apply(lambda x: split_and_strip(x, ','))

# Initialize MultiLabelBinarizer for each feature
mlb_genres = MultiLabelBinarizer()
mlb_directors = MultiLabelBinarizer()
mlb_actors = MultiLabelBinarizer()

# Fit and transform the features
genres_encoded = mlb_genres.fit_transform(df['genres'])
directors_encoded = mlb_directors.fit_transform(df['director'])
actors_encoded = mlb_actors.fit_transform(df['actors'])

# Define weights for each feature category
weight_genres = 1.5
weight_actors = 1.2
weight_directors = 1.1

# Convert numpy arrays to sparse matrices and apply weights
genres_sparse = csr_matrix(genres_encoded * weight_genres)
directors_sparse = csr_matrix(directors_encoded * weight_directors)
actors_sparse = csr_matrix(actors_encoded * weight_actors)

# Horizontally stack all weighted feature matrices
feature_matrix = hstack([genres_sparse, directors_sparse, actors_sparse])

# Initialize the KNN model
knn_model = NearestNeighbors(n_neighbors=10, metric='cosine')  # using cosine similarity

# Fit the model on the feature matrix
knn_model.fit(feature_matrix)

print("Model trained successfully.")

# Serialize (pickle) the model and encoders
with open(MODEL_PATH, 'wb') as model_file:
    pickle.dump(knn_model, model_file)

with open(MLB_GENRES_PATH, 'wb') as genres_file:
    pickle.dump(mlb_genres, genres_file)

with open(MLB_DIRECTORS_PATH, 'wb') as directors_file:
    pickle.dump(mlb_directors, directors_file)

with open(MLB_ACTORS_PATH, 'wb') as actors_file:
    pickle.dump(mlb_actors, actors_file)

print("Model and encoders have been serialized and saved successfully.")
