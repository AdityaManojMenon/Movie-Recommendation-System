# Movie-Recommendation-System
A content-based movie recommendation system that suggests movies based on user preferences using machine learning algorithms. Built with Python, Scikit-learn, Streamlit, and MongoDB.

# 🚀 Features
✅ Personalized Recommendations – Suggests movies based on user ratings and metadata. <br> ✅ User Authentication – Register and log in using MongoDB & bcrypt encryption.  <br> ✅ Content-Based Filtering – Uses KNN with cosine similarity on weighted movie features.  <br> ✅ Interactive UI – Built with Streamlit for an intuitive and dynamic user experience.  <br> ✅ Secure Storage – User data and recommendations are stored in a MongoDB database.  <br> ✅ Pickle Serialization – Trained models are saved and loaded efficiently for real-time inference.




# ⚙️ Tech Stack
Programming Language: Python <br> Libraries & Frameworks: Scikit-learn, NumPy, Pandas, Streamlit <br> Machine Learning Algorithm: K-Nearest Neighbors (KNN) with cosine similarity <br> Data Storage: MongoDB <br> Security: bcrypt for password hashing <br> Deployment: Local/Cloud (can be extended using Docker & cloud services)


📂 Project Structure
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

