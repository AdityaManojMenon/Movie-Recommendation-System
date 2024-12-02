import streamlit as st
from recommend import recommend_movies, df, feature_matrix, knn_model
import pandas as pd

# Streamlit App Layout
st.title("🎬 Personalized Movie Recommendation System")

st.write("""
### How it Works:
1. **Select and Rate Movies**: Choose up to 5 movies you've watched and rate them.
2. **Get Recommendations**: The system will suggest 5 movies based on your preferences.
""")

# Sidebar for user inputs
st.sidebar.header("Rate Your Favorite Movies")

# Display a multiselect widget for movies
movie_options = df['title'].tolist()
selected_titles = st.sidebar.multiselect("Select Movies You've Watched", movie_options, max_selections=5)

user_ratings = []

for title in selected_titles:
    # Fetch the movieId for the selected title
    movie_row = df[df['title'] == title]
    if not movie_row.empty:
        movie_id = movie_row['movieId'].values[0]
        # Create a slider for rating
        rating = st.sidebar.slider(f"Rate '{title}'", 1.0, 5.0, 3.0, step=0.5)
        user_ratings.append((movie_id, rating))
    else:
        st.sidebar.warning(f"Movie '{title}' not found in the dataset.")

# Button to get recommendations
if st.sidebar.button("Get Recommendations"):
    if not user_ratings:
        st.sidebar.warning("Please select and rate at least one movie.")
    else:
        try:
            with st.spinner("Generating recommendations..."):
                recommendations = recommend_movies(user_ratings, df, feature_matrix, knn_model, top_n=5)
            
            if recommendations.empty:
                st.warning("No recommendations found based on your ratings.")
            else:
                st.success("Here are your recommended movies:")
                for idx, row in recommendations.iterrows():
                    st.markdown(f"### {row['title']} ({row['release_date']})")
                    
                    # Handle genres
                    if isinstance(row['genres'], list):
                        genres = ', '.join(row['genres'])
                    else:
                        genres = row['genres']
                    
                    # Handle director
                    if isinstance(row['director'], list):
                        director = ', '.join(row['director'])
                    else:
                        director = row['director']
                    
                    # Handle actors
                    if isinstance(row['actors'], list):
                        actors = ', '.join(row['actors'])
                    else:
                        actors = row['actors']
                    
                    st.write(f"**Genres:** {genres}")
                    st.write(f"**Director:** {director}")
                    st.write(f"**Actors:** {actors}")
                    st.write(f"**Rating:** {row['rating']}")
                    st.markdown("---")
        except ValueError as e:
            st.error(str(e))
