import streamlit as st
import pickle
import pandas as pd
import subprocess
import json
import os


API_KEY = os.getenv("TMDB_API_KEY")
print("API KEY EXISTS:", bool(API_KEY))


def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    result = subprocess.run(
        [
            "curl.exe",
            "-4",
            "-sS",
            "-G",
            url,
            "--data-urlencode",
            f"api_key={API_KEY}",
            "--data-urlencode",
            "language=en-US"
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=20
    )

    print("\n==============================")
    print("MOVIE ID:", movie_id)
    print("RETURN CODE:", result.returncode)

    if result.returncode != 0:
        print("CURL ERROR:", result.stderr)
        return None

    if not result.stdout:
        print("No response received from curl")
        return None

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print("JSON ERROR:", e)
        print("RAW RESPONSE:", result.stdout)
        return None

    poster_path = data.get("poster_path")

    print("POSTER PATH:", poster_path)

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path

    print("NO POSTER FOUND")
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


# Load data

movies_dict = pickle.load(
    open("movie_dict.pkl", "rb")
)

movie = pd.DataFrame(movies_dict)

similarity = pickle.load(
    open("similarity.pkl", "rb")
)


# Streamlit UI

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