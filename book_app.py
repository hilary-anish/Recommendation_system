import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender')

neighbor_model = pickle.load(open("./trained_models_data/neighbor_model.pkl", "rb"))
book_lib = pickle.load(open("./trained_models_data/book_library.pkl", "rb"))
collaborative_pivot = pickle.load(open("./trained_models_data/collaborative_pivot.pkl", "rb"))
final_data = pickle.load(open("./trained_models_data/final_data.pkl", "rb"))



def fetch_poster(suggestion):
    url_list = []
    for i in range(len(suggestion)):
        suggested_books = collaborative_pivot.index[suggestion[i]]
        for j in suggested_books:
            print(j)
            img_url = final_data.loc[final_data['Title'] == j, 'Img_url'].values[0]
            url_list.append(img_url)

    return url_list


def recommend_book(selected_book):
    book_list = []
    book_id = np.where(book_lib == selected_book)[0][0]
    distance, suggestion = neighbor_model.kneighbors(collaborative_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=5)
    
    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        suggested_books = collaborative_pivot.index[suggestion[i]]
        for j in suggested_books:
            book_list.append(j)


    return book_list, poster_url


selected_book = st.selectbox("Select a Book", book_lib)


if st.button('Show Recommendation'):
    books, posters = recommend_book(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(books[1])
        st.image(posters[1])

    with col2:
        st.text(books[2])
        st.image(posters[2])


    with col3:
        st.text(books[3])
        st.image(posters[3])

    with col4:
        st.text(books[4])
        st.image(posters[4])


