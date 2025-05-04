import pickle
import streamlit as st
import requests

st.header("Movie Recommendation System")


movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    poster_path = data.get("poster_path")
    if poster_path:
        full_url = "https://image.tmdb.org/t/p/w500" + poster_path
        return full_url
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    
    return recommended_movies_name, recommended_movies_poster


if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_movies_name[i])
            st.image(recommended_movies_poster[i])
