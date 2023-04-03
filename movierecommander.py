import streamlit as st 
from time import sleep
import pickle
import requests





def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=b9b4079d365999562ef382d38b17daa5".format(movie_id))
    if response.status_code == 404:
        return False
    
    data = response.json()
    
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]




def recommand(move):
    movie_index = movie_data[movie_data["title"] == move].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommanded_movie = []
    recommanded_movie_poster = []
    for i in movies_list:
        movie_id = movie_data.iloc[i[0]]["movie_id"]
        print(movie_id)
        recommanded_movie.append(movie_data.iloc[i[0]][1])
        recommanded_movie_poster.append(fetch_poster(movie_id))
    print(recommanded_movie)
    return recommanded_movie,recommanded_movie_poster



st.title("Movie Recommandation")

with open("movie.pkl","rb") as file:
    movie_data = pickle.load(file)

# print(movie_data)
choise  = st.selectbox("select a movie ",options= movie_data["title"])
st.write(choise)

with open("similarity.pkl","rb") as file:
    similarity = pickle.load(file)


if st.button('Recommand'):
    movie_list,movie_poster  = recommand(choise)
    cl0,cl1,cl2,cl3,cl4= st.columns(5)

    with cl0:
        st.text(movie_list[0])
        if movie_poster[0] == False:
            st.write("poster not found")
        else:    
            st.image(movie_poster[0])

    with cl1:
        st.text(movie_list[1])
        if movie_poster[0] == False:
            st.write("poster not found")
        else:    
            st.image(movie_poster[1])

    with cl2:
        st.text(movie_list[2])
        if movie_poster[0] == False:
            st.write("poster not found")
        else:    
            st.image(movie_poster[2])

    with cl3:
        st.text(movie_list[3])
        if movie_poster[0] == False:
            st.write("poster not found")
        else:    
            st.image(movie_poster[3])

    with cl4:
        st.text(movie_list[4])
        if movie_poster[0] == False:
            st.write("poster not found")
        else:    
            st.image(movie_poster[4])