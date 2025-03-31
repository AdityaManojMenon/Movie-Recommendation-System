# Movie-Recommendation-System
A content-based movie recommendation system that suggests movies based on user preferences using machine learning algorithms. Built with Python, Scikit-learn, Streamlit, and MongoDB.

# 🚀 Features
✅ Personalized Recommendations – Suggests movies based on user ratings and metadata. <br> ✅ User Authentication – Register and log in using MongoDB & bcrypt encryption.  <br> ✅ Content-Based Filtering – Uses KNN with cosine similarity on weighted movie features.  <br> ✅ Interactive UI – Built with Streamlit for an intuitive and dynamic user experience.  <br> ✅ Secure Storage – User data and recommendations are stored in a MongoDB database.  <br> ✅ Pickle Serialization – Trained models are saved and loaded efficiently for real-time inference.


# ⚙️ Tech Stack

| Category	Tools  | Technologies |
| ------------- | ------------- |
| Programming Language  | Python  |
| Frameworks & Libraries  | Streamlit, Scikit-learn, Pandas, NumPy, SciPy  |
| Database  | MongoDB  |
| Machine Learning Model  | K-Nearest Neighbors (KNN)  |
| Security  | bcrypt (Password Hashing)  |
| Data Handling  | Pandas, MultiLabelBinarizer, Sparse Matrices  |
| Deployment  | Streamlit Cloud, Flask |
| Version Control  | Git, GitHub  |


 
📂 Project Structure <br>
├── models/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Serialized model files <br>
│ &nbsp;   ├── knn_model.pkl  &nbsp; &nbsp; &nbsp; &nbsp;       # Trained KNN model <br>
│ &nbsp;   ├── mlb_genres.pkl &nbsp; &nbsp; &nbsp; &nbsp;      # MultiLabelBinarizer for genres <br>
│ &nbsp;   ├── mlb_directors.pkl &nbsp; &nbsp;     # MultiLabelBinarizer for directors <br>
│ &nbsp;   ├── mlb_actors.pkl &nbsp; &nbsp; &nbsp; &nbsp;         # MultiLabelBinarizer for actors <br>
<br>
├── data/ <br>
│ &nbsp;   ├── movie_data.csv  &nbsp; &nbsp; &nbsp;      # Movie dataset <br>
<br>
├── app.py  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  # Streamlit web application <br>
├── recommend.py &nbsp; &nbsp; &nbsp;             # Recommendation logic <br>
├── train_model.py &nbsp; &nbsp; &nbsp;           # Model training script <br>
├── .env  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; # Environment variables (MongoDB URI) <br>
├── requirements.txt  &nbsp; &nbsp;    # Project dependencies <br>
├── README.md  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    # Documentation <br>

# 🚀 Installation & Setup

1️⃣ Clone the repository <br>
git clone https://github.com/AdityaManojMenon/Movie-Recommendation-System.git  <br>
cd Movie-Recommendation-System  <br>

2️⃣ Install dependencies <br>
pip install -r requirements.txt <br>

3️⃣ Set up MongoDB (if applicable) <br>
Create a .env file and add your MongoDB URI: <br>
MONGO_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/  <br>

4️⃣ Train the model <br>
python train_model.py   <br>

5️⃣ Run the Streamlit app <br>
streamlit run app.py  <br>


# 🎯 How It Works <br>
1. User logs in or registers. <br>
2. Selects and rates movies from the dataset. <br>
3. System computes a user profile based on selected movies. <br>
4. KNN model finds the nearest neighbors and recommends similar movies. <br>
5. Recommended movies are displayed with details (title, genres, director, actors, etc.). <br>
6. Recommendations are saved to the user's profile in MongoDB. <br>


# 🛠 Model Training Details <br>
* Dataset: movie_data.csv (contains movie titles, genres, directors, actors). <br>
* Preprocessing: Used MultiLabelBinarizer to one-hot encode categorical features. <br>
* Feature Engineering: Applied weights to different features: <br>
 &nbsp; &nbsp; * Genres: 1.5x weight <br>
 &nbsp; &nbsp; * Actors: 1.2x weight <br>
 &nbsp; &nbsp; * Directors: 1.1x weight <br>
* Algorithm: K-Nearest Neighbors (KNN) with cosine similarity. <br>
* Model Persistence: Trained model and encoders are stored as .pkl files. <br>


# 🛡 Security Features <br>
* User Authentication: MongoDB stores hashed passwords using bcrypt. <br> 
* Session Management: Streamlit’s session state prevents unauthorized access. <br>


# 🌟 Future Improvements <br>  
✅ Improve recommendation accuracy using NLP-based embeddings (TF-IDF or Word2Vec). <br>  
✅ Add collaborative filtering to enhance recommendations. <br>  
✅ Deploy using Docker & Cloud platforms (AWS, Heroku, or Streamlit Cloud). <br> 
✅ Enhance UI with better visualizations and movie posters. <br> 

# 📌 Contributing <br>
Feel free to fork this repository and contribute! 🚀 <br>

# 📧 Contact <br>
📩 Aditya Manoj Menon <br>
📍 GitHub: [AdityaManojMenon](https://github.com/AdityaManojMenon) <br>
📧 Email: menonad1@msu.edu <br>
