# Movie-Recommendation-System
A content-based movie recommendation system that suggests movies based on user preferences using machine learning algorithms. Built with Python, Scikit-learn, Streamlit, and MongoDB.

# 🚀 Features
✅ Personalized Recommendations – Suggests movies based on user ratings and metadata. <br> ✅ User Authentication – Register and log in using MongoDB & bcrypt encryption.  <br> ✅ Content-Based Filtering – Uses KNN with cosine similarity on weighted movie features.  <br> ✅ Interactive UI – Built with Streamlit for an intuitive and dynamic user experience.  <br> ✅ Secure Storage – User data and recommendations are stored in a MongoDB database.  <br> ✅ Pickle Serialization – Trained models are saved and loaded efficiently for real-time inference.


# ⚙️ Tech Stack
Programming Language: Python <br> Libraries & Frameworks: Scikit-learn, NumPy, Pandas, Streamlit <br> Machine Learning Algorithm: K-Nearest Neighbors (KNN) with cosine similarity <br> Data Storage: MongoDB <br> Security: bcrypt for password hashing <br> Deployment: Local/Cloud (can be extended using Docker & cloud services)


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
