import streamlit as st
import pickle
import pandas as pd
import requests
import subprocess
import json
import os


# Get API key
API_KEY = st.secrets["TMDB_API_KEY"]


def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    for attempt in range(3):

        try:

            result = subprocess.run(
                [
                    "curl.exe",
                    "-4",
                    "-sS",
                    "-G",
                    url,
                    "--connect-timeout", "10",
                    "--max-time", "30",
                    "--data-urlencode",
                    f"api_key={API_KEY}",
                    "--data-urlencode",
                    "language=en-US"
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=35
            )

            if result.returncode != 0:
                print("Curl failed:", result.stderr)
                continue

            if not result.stdout:
                continue

            data = json.loads(result.stdout)

            poster_path = data.get("poster_path")

            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path

            return None

        except subprocess.TimeoutExpired:
            print(f"TMDB timeout for movie {movie_id}. Attempt {attempt + 1}/3")

        except json.JSONDecodeError:
            print("Invalid JSON returned by TMDB")

        except Exception as e:
            print("Poster error:", e)

    return None

def recommend(movie_title):

    movie_index = movie[movie["title"] == movie_title].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:

        movie_row = movie.iloc[i[0]]

        movie_id = movie_row["movie_id"]

        recommended_movies.append(movie_row["title"])

        poster = fetch_poster(movie_id)

        recommended_movies_posters.append(poster)

    return recommended_movies, recommended_movies_posters


# --------------------------------
# Load data
# --------------------------------

movies_dict = pickle.load(
    open("movie_dict.pkl", "rb")
)

movie = pd.DataFrame(movies_dict)

similarity = pickle.load(
    open("similarity.pkl", "rb")
)


# --------------------------------
# Streamlit UI
# --------------------------------

st.title("Movies Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to recommend",
    movie["title"].values
)


if st.button("Recommend"):

    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):

        with col:

            st.text(name)

            if poster:
                st.image(poster)

            else:
                st.write("Poster unavailable")