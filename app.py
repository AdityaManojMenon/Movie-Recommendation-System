import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from recommend import recommend_movies, df, feature_matrix, knn_model

# Load .env
load_dotenv()

# Get MongoDB URI from .env
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    st.error("MongoDB URI is not set in the .env file.")
    st.stop()

# Connect to MongoDB
client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
client.server_info()
db = client["user_database"]
users = db["users"]

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.message = None

# Callback for Login
def login_user(username, password):
    user = users.find_one({"username": username, "password": password})
    if user:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.message = f"Welcome, {username}!"
    else:
        st.session_state.message = "Invalid username or password"

# Callback for Logout
def logout_user():
    st.session_state.clear()

# User Registration Function
def register_user(username, password):
    if users.find_one({"username": username}):
        return False, "Username already exists."
    users.insert_one({"username": username, "password": password})
    return True, "User registered successfully!"

# Login system
if not st.session_state.logged_in:
    st.title("Login or Register")

    # Tabs for login and registration
    tab1, tab2 = st.tabs(["Login", "Register"])

    # Login Tab
    with tab1:
        uname = st.text_input("Username", key="login_username")
        pswd = st.text_input("Password", type="password", key="login_password")
        if st.button("Login", on_click=login_user, args=(uname, pswd)):
            pass
        if st.session_state.get("message"):
            st.success(st.session_state.message) if st.session_state.logged_in else st.error(st.session_state.message)

    # Register Tab
    with tab2:
        new_uname = st.text_input("New Username", key="register_username")
        new_pswd = st.text_input("New Password", type="password", key="register_password")
        if st.button("Register"):
            success, message = register_user(new_uname, new_pswd)
            if success:
                st.success(message)
            else:
                st.error(message)

# After login
# Main app
else:
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

    # Logout button
    if st.button("Logout", on_click=logout_user):
        pass