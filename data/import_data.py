import pandas as pd


class Movies:
    def importDataMovies():
        lista_movies = []

        df_movies = pd.read_csv('../data/movie.csv')

        for key, value in enumerate(df_movies.values):
            title = value[0]
            year = value[2]
            img_url = value[6]
            genre = value[10]
            description = value[12]
            imdb_url = value[15]
            lista_movies.append({'title': title, 'year': year, 'img_url': img_url, 'genre': genre, 'description': description, 'imdb_url': imdb_url})

        return lista_movies
