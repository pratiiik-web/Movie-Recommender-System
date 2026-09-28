# 🎬 Movie Recommender System

A content-based movie recommendation web app. Pick a movie you like, and the app suggests similar movies based on their content (overview, genres, keywords, cast, and crew).

🔗 **Live Demo:** [Add your deployed app link here]([https://your-app-link.streamlit.app](https://movie-recommender-system-bvzyn8lpzzgula3ezqjuxh.streamlit.app/))

---

## ✨ Features

- Select any movie from a searchable dropdown
- Get top 5 similar movie recommendations instantly
- Movie posters fetched dynamically via API
- Clean, simple interface built with Streamlit
- Precomputed similarity matrix for fast responses

---

## 🧠 How It Works

This project uses **content-based filtering**:

1. **Data preparation** – Movie metadata (overview, genres, keywords, cast, crew) is merged into a single `tags` column per movie.
2. **Text cleaning** – Tags are lowercased and stemmed to reduce word variations.
3. **Vectorization** – Tags are converted into vectors using `CountVectorizer` (bag-of-words).
4. **Similarity** – **Cosine similarity** is computed between every pair of movie vectors.
5. **Recommendation** – For a selected movie, the app returns the 5 movies with the highest similarity scores.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, NLTK
- **Web App:** Streamlit
- **Data Source:** TMDB 5000 Movies Dataset
- **API:** TMDB API (for movie posters)
- **Deployment:** Streamlit Community Cloud

---

## 📁 Project Structure

```
Movie-Recommender-System/
│
├── app.py             # Streamlit web application
├── api_tester.py      # Script to test the poster API
├── movies.pkl         # Processed movies dataframe
├── movie_dict.pkl     # Movie data as dictionary (used by the app)
├── similarity.pkl     # Precomputed cosine similarity matrix
├── requirements.txt   # Project dependencies
└── README.md
```

---

## 🚀 Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/pratiik-web/Movie-Recommender-System.git
   cd Movie-Recommender-System
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your TMDB API key** *(if the app fetches posters)*
   Create a `.streamlit/secrets.toml` file:
   ```toml
   TMDB_API_KEY = "your_api_key_here"
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

The app will open at # 🎬 Movie Recommender System

A content-based movie recommendation web app. Pick a movie you like, and the app suggests similar movies based on their content (overview, genres, keywords, cast, and crew).

🔗 **Live Demo:** [Add your deployed app link here](https://your-app-link.streamlit.app)

---

## ✨ Features

- Select any movie from a searchable dropdown
- Get top 5 similar movie recommendations instantly
- Movie posters fetched dynamically via API
- Clean, simple interface built with Streamlit
- Precomputed similarity matrix for fast responses

---

## 🧠 How It Works

This project uses **content-based filtering**:

1. **Data preparation** – Movie metadata (overview, genres, keywords, cast, crew) is merged into a single `tags` column per movie.
2. **Text cleaning** – Tags are lowercased and stemmed to reduce word variations.
3. **Vectorization** – Tags are converted into vectors using `CountVectorizer` (bag-of-words).
4. **Similarity** – **Cosine similarity** is computed between every pair of movie vectors.
5. **Recommendation** – For a selected movie, the app returns the 5 movies with the highest similarity scores.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, NLTK
- **Web App:** Streamlit
- **Data Source:** TMDB 5000 Movies Dataset
- **API:** TMDB API (for movie posters)
- **Deployment:** Streamlit Community Cloud

---

## 📁 Project Structure

```
Movie-Recommender-System/
│
├── app.py             # Streamlit web application
├── api_tester.py      # Script to test the poster API
├── movies.pkl         # Processed movies dataframe
├── movie_dict.pkl     # Movie data as dictionary (used by the app)
├── similarity.pkl     # Precomputed cosine similarity matrix
├── requirements.txt   # Project dependencies
└── README.md
```

---

## 🚀 Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/pratiik-web/Movie-Recommender-System.git
   cd Movie-Recommender-System
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your TMDB API key** *(if the app fetches posters)*
   Create a `.streamlit/secrets.toml` file:
   ```toml
   TMDB_API_KEY = "your_api_key_here"
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

The app will open at `https://movie-recommender-system-bvzyn8lpzzgula3ezqjuxh.streamlit.app/`.

---

## 📊 Dataset

[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle.

---

## 🔮 Future Improvements

- Add collaborative filtering and build a hybrid recommender
- Use TF-IDF or sentence embeddings instead of bag-of-words
- Add filters (genre, year, rating)
- Show movie details (rating, overview, cast) alongside recommendations

---

## 👤 Author

**Pratik Karale**
GitHub: [@pratiik-web](https://github.com/pratiik-web)

---

⭐ If you found this project useful, consider giving it a star!.

---

## 📊 Dataset

[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle.

---

## 🔮 Future Improvements

- Add collaborative filtering and build a hybrid recommender
- Use TF-IDF or sentence embeddings instead of bag-of-words
- Add filters (genre, year, rating)
- Show movie details (rating, overview, cast) alongside recommendations

---

## 👤 Author

**Pratik Karale**
GitHub: [@pratiik-web](https://github.com/pratiik-web)

---

⭐ If you found this project useful, consider giving it a star!
