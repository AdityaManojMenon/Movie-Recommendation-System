import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from recommend import recommend_movies, df, feature_matrix, knn_model
import bcrypt


# Load Environment Variables
load_dotenv()

# Get MongoDB URI from .env
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    st.error("MongoDB URI is not set in the .env file.")
    st.stop()


# Connect to MongoDB
try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    client.server_info()  # Trigger exception if cannot connect
    db = client["user_database"]  # Database name
    users_collection = db["users"]  # Collection name
except Exception as e:
    st.error(f"Could not connect to MongoDB: {e}")
    st.stop()


# Initialize Session State for Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.message = None


# User Registration 
def register_user(username, password):
    if users_collection.find_one({"username": username}):
        return False, "Username already exists. Please choose a different one."
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Store user with hashed password and empty recommendations
    users_collection.insert_one({
        "username": username,
        "password": hashed_password,
        "recommendations": []  # To store user-specific recommendations
    })
    return True, "User registered successfully!"


# User Login Function
def login_user(username, password):
    user = users_collection.find_one({"username": username})
    if user:
        # Verify password
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.message = f"Welcome, {username}!"
        else:
            st.session_state.message = "Invalid username or password."
    else:
        st.session_state.message = "Invalid username or password."


# User Logout Function
def logout_user():
    st.session_state.clear()


# Display Past Recommendations
def display_past_recommendations(username):
    user = users_collection.find_one({"username": username})
    if user and user.get("recommendations"):
        st.header("📚 Your Previous Recommendations")
        for idx, rec in enumerate(user["recommendations"], 1):
            st.markdown(f"### {idx}. {rec['title']} ({rec['release_date']})")
            # Handle genres
            genres = ', '.join(rec['genres']) if isinstance(rec['genres'], list) else rec['genres']
            # Handle director
            director = ', '.join(rec['director']) if isinstance(rec['director'], list) else rec['director']
            # Handle actors
            actors = ', '.join(rec['actors']) if isinstance(rec['actors'], list) else rec['actors']
            st.write(f"**Genres:** {genres}")
            st.write(f"**Director:** {director}")
            st.write(f"**Actors:** {actors}")
            st.write(f"**Rating:** {rec['rating']}")
            st.markdown("---")
    else:
        st.info("You have no past recommendations.")


# Main Application
def main():
    # If not logged in, show login and registration
    if not st.session_state.logged_in:
        st.title("🎬 Movie Recommendation System")
        st.write("Please log in or register to continue.")

        # Tabs for Login and Register
        tab1, tab2 = st.tabs(["🔒 Login", "📝 Register"])
        
        # Login Tab
        with tab1:
            st.subheader("Login")
            with st.form("login_form"):
                login_username = st.text_input("Username", key="login_username")
                login_password = st.text_input("Password", type="password", key="login_password")
                submit_login = st.form_submit_button("Login")
                
                if submit_login:
                    if not login_username or not login_password:
                        st.error("Please enter both username and password.")
                    else:
                        login_user(login_username, login_password)
                        if st.session_state.message:
                            if st.session_state.logged_in:
                                st.success(st.session_state.message)
                            else:
                                st.error(st.session_state.message)

        # Register Tab
        with tab2:
            st.subheader("Register")
            with st.form("register_form"):
                register_username = st.text_input("Choose a Username", key="register_username")
                register_password = st.text_input("Choose a Password", type="password", key="register_password")
                register_confirm_password = st.text_input("Confirm Password", type="password", key="register_confirm_password")
                submit_register = st.form_submit_button("Register")
                
                if submit_register:
                    if not register_username or not register_password or not register_confirm_password:
                        st.error("Please fill out all fields.")
                    elif register_password != register_confirm_password:
                        st.error("Passwords do not match.")
                    else:
                        success, message = register_user(register_username, register_password)
                        if success:
                            st.success(message)
                        else:
                            st.error(message)
    else:
        # If logged in, show the main app
        st.title("🎬 Personalized Movie Recommendation System")
        st.write("### Welcome to your personalized movie recommendation dashboard!")

        # Display past recommendations
        display_past_recommendations(st.session_state.username)

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
                rating = st.sidebar.slider(f"Rate '{title}'", 1.0, 5.0, 3.0, step=0.5, key=title)
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

                        # Save recommendations to MongoDB
                        users_collection.update_one(
                            {"username": st.session_state.username},
                            {"$set": {"recommendations": recommendations.to_dict('records')}}
                        )
                        st.success("Your recommendations have been saved to your profile.")
                except ValueError as e:
                    st.error(str(e))

        # Logout button
        if st.sidebar.button("Logout"):
            logout_user()
            st.success("You have been logged out.")


# Run the main
if __name__ == "__main__":
    main()
