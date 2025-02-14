from flask import Flask, render_template, request
import pickle
import numpy as np

# Load saved data
movies = pickle.load(open('model/movie_data.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

app = Flask(__name__)

# Recommendation function
def recommend_movies(title, num_recommendations=5):
    if title not in movies['title'].values:
        return ["Movie not found in dataset."]
    
    idx = movies[movies['title'] == title].index[0]
    similarity_scores = list(enumerate(similarity[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_movie_indices = [i[0] for i in similarity_scores[1:num_recommendations+1]]
    
    return movies.iloc[recommended_movie_indices]['title'].tolist()

# Home page
@app.route('/')
def index():
    return render_template('index.html', movies=movies['title'].tolist())

# Recommendation API
@app.route('/recommend', methods=['POST'])
def recommend_movie():
    movie = request.form['movie']
    recommendations = recommend_movies(movie)
    return render_template('index.html', movies=movies['title'].tolist(), recommendations=recommendations, selected_movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
