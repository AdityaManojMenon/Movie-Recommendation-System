# Movie-Recommendation-System
A content-based movie recommendation system that suggests movies based on user preferences using machine learning algorithms. Built with Python, Scikit-learn, Streamlit, and MongoDB.

# 🚀 Features
✅ Personalized Recommendations – Suggests movies based on user ratings and metadata. <br> ✅ User Authentication – Register and log in using MongoDB & bcrypt encryption.  <br> ✅ Content-Based Filtering – Uses KNN with cosine similarity on weighted movie features.  <br> ✅ Interactive UI – Built with Streamlit for an intuitive and dynamic user experience.  <br> ✅ Secure Storage – User data and recommendations are stored in a MongoDB database.  <br> ✅ Pickle Serialization – Trained models are saved and loaded efficiently for real-time inference.




# ⚙️ Tech Stack
Programming Language: Python <br> Libraries & Frameworks: Scikit-learn, NumPy, Pandas, Streamlit <br> Machine Learning Algorithm: K-Nearest Neighbors (KNN) with cosine similarity <br> Data Storage: MongoDB <br> Security: bcrypt for password hashing <br> Deployment: Local/Cloud (can be extended using Docker & cloud services)


📂 Project Structure
bash
Copy
Edit
├── models/                   # Serialized model files
│   ├── knn_model.pkl         # Trained KNN model
│   ├── mlb_genres.pkl        # MultiLabelBinarizer for genres
│   ├── mlb_directors.pkl     # MultiLabelBinarizer for directors
│   ├── mlb_actors.pkl        # MultiLabelBinarizer for actors
│
├── data/
│   ├── movie_data.csv        # Movie dataset
│
├── app.py                    # Streamlit web application
├── recommend.py              # Recommendation logic
├── train_model.py            # Model training script
├── .env                      # Environment variables (MongoDB URI)
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation
🚀 Installation & Setup
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/AdityaManojMenon/Movie-Recommendation-System.git
cd Movie-Recommendation-System
2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set up MongoDB (if applicable)

Create a .env file and add your MongoDB URI:

ini
Copy
Edit
MONGO_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/
4️⃣ Train the model

bash
Copy
Edit
python train_model.py
5️⃣ Run the Streamlit app

bash
Copy
Edit
streamlit run app.py
🎯 How It Works
User logs in or registers.

Selects and rates movies from the dataset.

System computes a user profile based on selected movies.

KNN model finds the nearest neighbors and recommends similar movies.

Recommended movies are displayed with details (title, genres, director, actors, etc.).

Recommendations are saved to the user's profile in MongoDB.

🛠 Model Training Details
Dataset: movie_data.csv (contains movie titles, genres, directors, actors).

Preprocessing: Used MultiLabelBinarizer to one-hot encode categorical features.

Feature Engineering: Applied weights to different features:

Genres: 1.5x weight

Actors: 1.2x weight

Directors: 1.1x weight

Algorithm: K-Nearest Neighbors (KNN) with cosine similarity.

Model Persistence: Trained model and encoders are stored as .pkl files.

📜 Example Usage
User selects movies and rates them.

System computes recommendations.

Example output:

yaml
Copy
Edit
🎥 Recommended Movies:
1️⃣ Inception (2010)
   🎭 Genres: Action, Sci-Fi, Thriller
   🎬 Director: Christopher Nolan
   🎭 Actors: Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page
   ⭐ Rating: 8.8
2️⃣ The Dark Knight (2008)
   ...
🛡 Security Features
User Authentication: MongoDB stores hashed passwords using bcrypt.

Session Management: Streamlit’s session state prevents unauthorized access.

🌟 Future Improvements
✅ Improve recommendation accuracy using NLP-based embeddings (TF-IDF or Word2Vec).

✅ Add collaborative filtering to enhance recommendations.

✅ Deploy using Docker & Cloud platforms (AWS, Heroku, or Streamlit Cloud).

✅ Enhance UI with better visualizations and movie posters.

📌 Contributing
Feel free to fork this repository and contribute! 🚀

📧 Contact
📩 Aditya Manoj Menon
📍 GitHub: AdityaManojMenon
📧 Email: (your email)

